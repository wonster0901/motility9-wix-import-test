import { chromium } from 'playwright';
import { execFileSync, spawn } from 'node:child_process';
import { mkdir, readFile, writeFile, cp } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const out = path.resolve(process.env.SITE_QA_OUTPUT || path.join(root, 'site-qa'));
const base = process.env.SITE_PREVIEW_URL || 'http://127.0.0.1:8750';
const baseline = '3497d2fab1c3f22aa5d08a075b4abcb839d31ea3';
const routes = ['/', '/motility9/', '/motility9/privacy/', '/motility9/support/',
  '/motility9/terms/', '/tasteroaming/', '/tasteroaming/privacy/',
  '/tasteroaming/support/', '/tasteroaming/terms/', '/privacy.html', '/support.html', '/terms.html'];
const widths = process.env.QA_FAST ? [320, 1280] : [320, 375, 430, 768, 1280, 1440];
const axe = await readFile(path.join(root, 'node_modules/axe-core/axe.min.js'), 'utf8');
await mkdir(path.join(out, 'screenshots'), { recursive: true });
const report = { baseline, productionDeployed: false, routes: routes.length, checks: [], issues: [], screenshots: [] };
const server = process.env.SITE_PREVIEW_URL ? null : spawn('python3', ['-m', 'http.server', '8750', '--bind', '127.0.0.1'], { cwd: root, stdio: 'ignore' });
let browser;
try {
  for (let i = 0; i < 80; i++) {
    try { if ((await fetch(base)).ok) break; } catch {}
    if (i === 79) throw Error('Local preview server did not start');
    await new Promise(resolve => setTimeout(resolve, 100));
  }
  browser = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH || undefined, headless: true, args: ['--no-sandbox'] });
  const context = await browser.newContext({ reducedMotion: 'reduce' });
  const page = await context.newPage();
  page.on('pageerror', error => report.issues.push({ kind: 'javascript', message: error.message }));
  page.on('request', request => {
    const url = request.url();
    if (!url.startsWith(base) && !url.startsWith('data:')) report.issues.push({ kind: 'external-request', url });
  });
  page.on('response', response => {
    if (response.status() >= 400) report.issues.push({ kind: 'http', url: response.url(), status: response.status() });
  });

  async function ready() {
    await page.evaluate(async () => {
      await document.fonts.ready;
      for (const img of document.images) {
        if (img.loading === 'lazy') {
          img.scrollIntoView({ behavior: 'instant' });
          await new Promise(requestAnimationFrame);
        }
        await img.decode();
      }
      window.scrollTo({ top: 0, behavior: 'instant' });
    });
  }
  async function screenshot(name) {
    await page.screenshot({ path: path.join(out, 'screenshots', name + '.png'), fullPage: true });
    report.screenshots.push(name + '.png');
  }
  async function zoomText() {
    await page.evaluate(() => {
      // Text-only 200% resizing, including original px-based typography. An
      // illustrative PDF preview has image semantics and retains its diagram.
      const sizes = [...document.querySelectorAll('html,body,body *')]
        .filter(el => !el.closest('[role="img"]'))
        .map(el => [el, parseFloat(getComputedStyle(el).fontSize)]);
      for (const [el, size] of sizes) el.style.fontSize = `${size * 2}px`;
    });
  }
  async function layout(route, width, scale, menu = false) {
    const result = await page.evaluate(() => {
      const visible = el => {
        const rect = el.getBoundingClientRect();
        const css = getComputedStyle(el);
        return rect.width > 0 && rect.height > 0 && css.visibility !== 'hidden' && css.display !== 'none' && rect.bottom > 0;
      };
      const smallTargets = [...document.querySelectorAll('a,summary,button')]
        .filter(visible).map(el => ({ text: el.textContent.trim(), rect: el.getBoundingClientRect() }))
        .filter(({ rect }) => rect.width < 47.5 || rect.height < 47.5)
        .map(({ text, rect }) => ({ text, width: rect.width, height: rect.height }));
      const clipped = [...document.querySelectorAll('main h1,main h2,main h3,main p,main a')]
        .filter(el => visible(el) && !el.closest('[role="img"]') && el.clientWidth > 0)
        .filter(el => el.scrollWidth > el.clientWidth + 1)
        .map(el => el.textContent.trim().slice(0, 160));
      return { overflow: document.documentElement.scrollWidth > innerWidth + 1, smallTargets, clipped,
        brokenImages: [...document.images].filter(img => (img.complete && !img.naturalWidth) || (!img.complete && img.loading !== 'lazy')).map(img => img.getAttribute('src')) };
    });
    report.checks.push({ route, width, scale, menu, ...result });
    if (result.overflow || result.smallTargets.length || result.clipped.length || result.brokenImages.length)
      report.issues.push({ kind: 'layout', route, width, scale, menu, ...result });
  }

  // Reviewable, real baseline screenshots; original HTML is served only inside
  // this browser route, without touching the production host or working tree.
  await page.route('**/__baseline__/**', async route => {
    const name = new URL(route.request().url()).pathname.split('/').pop() || 'index.html';
    if (!['index.html', 'privacy.html', 'support.html', 'terms.html'].includes(name)) return route.fulfill({ status: 404 });
    const body = execFileSync('git', ['show', `${baseline}:${name}`], { cwd: root, maxBuffer: 8 * 1024 * 1024 });
    return route.fulfill({ contentType: 'text/html; charset=utf-8', body });
  });
  await page.route('**/favicon.ico', route => route.fulfill({ status: 204 }));
  for (const width of [375, 1280]) {
    await page.setViewportSize({ width, height: 900 });
    for (const name of ['index.html', 'privacy.html']) {
      await page.goto(`${base}/__baseline__/${name}`);
      await ready();
      await screenshot(`before-${name.replace('.html', '')}-${width}`);
    }
  }
  await page.unroute('**/__baseline__/**');
  const shots = new Map([['/', 'brand'], ['/motility9/', 'motility9'], ['/tasteroaming/', 'tasteroaming'],
    ['/privacy.html', 'legacy-privacy'], ['/tasteroaming/privacy/', 'tasteroaming-privacy']]);
  let axeChecks = 0;
  for (const route of routes) {
    for (const width of widths) {
      await page.setViewportSize({ width, height: width < 768 ? 844 : 1000 });
      for (const scale of [1, 2]) {
        const response = await page.goto(base + route);
        if (response.status() !== 200) throw Error(`Route failed: ${route}`);
        await ready();
        if (scale === 2) await zoomText();
        await layout(route, width, scale);
        if ((width === 1280 && scale === 1) || (width === 320 && scale === 2)) {
          await page.addScriptTag({ content: axe });
          const result = await page.evaluate(async () => window.axe.run(document, {
            runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21aa', 'best-practice'] },
          }));
          axeChecks++;
          for (const v of result.violations) report.issues.push({ kind: 'axe', route, width, scale,
            id: v.id, impact: v.impact, nodes: v.nodes.map(n => ({ target: n.target, summary: n.failureSummary })) });
        }
        if (shots.has(route) && (([375, 1280].includes(width) && scale === 1) ||
            (width === 320 && scale === 2 && ['/', '/motility9/', '/tasteroaming/'].includes(route)))) {
          await screenshot(`after-${shots.get(route)}-${width}-${scale}x`);
        }
        if (width === 320 && scale === 1) {
          // Scrolling to decode lazy images changes the browser's sequential
          // focus starting point. Test first Tab on a fresh document instead.
          await page.goto(base + route + '?keyboard-review=1');
          await page.keyboard.press('Tab');
          if (!await page.locator('.skip-link').evaluate(el => el === document.activeElement))
            report.issues.push({ kind: 'keyboard-skip', route });
          await page.keyboard.press('Enter');
          if (!await page.locator('main').evaluate(el => el === document.activeElement))
            report.issues.push({ kind: 'keyboard-main-focus', route });
          const summary = page.locator('details summary:visible').first();
          if (await summary.count()) {
            await summary.focus();
            await page.keyboard.press('Enter');
            if (!await summary.evaluate(el => el.parentElement.open)) report.issues.push({ kind: 'menu-open', route });
            await layout(route, width, scale, true);
            await page.keyboard.press('Tab');
            if (!await page.evaluate(() => document.activeElement.matches('details[open] a')))
              report.issues.push({ kind: 'menu-keyboard-link', route });
            await summary.focus();
            await page.keyboard.press('Enter');
            if (await summary.evaluate(el => el.parentElement.open)) report.issues.push({ kind: 'menu-close', route });
          }
        }
      }
    }
  }
  report.axeChecks = axeChecks;
  report.status = report.issues.length ? 'FAIL' : 'PASS';
  await writeFile(path.join(out, 'browser-report.json'), JSON.stringify(report, null, 2));
  const images = report.screenshots.map(name => `<figure><figcaption>${name}</figcaption><a href="screenshots/${name}"><img src="screenshots/${name}" alt="${name}" loading="lazy"></a></figure>`).join('\n');
  await writeFile(path.join(out, 'review.html'), `<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>WONWINNIE review — not published</title><style>body{font:16px/1.5 sans-serif;margin:24px;color:#20251f}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,340px),1fr));gap:24px}figure{margin:0}img{max-width:100%;height:auto;border:1px solid #ddd}figcaption{padding:12px;overflow-wrap:anywhere}</style><h1>WONWINNIE website review</h1><p>Local browser captures only. Nothing has been published. Baseline: ${baseline}. Open an image for full resolution.</p><main>${images}</main></html>`);
  await mkdir(path.join(out, 'site'), { recursive: true });
  for (const name of ['index.html','privacy.html','support.html','terms.html','MOTILITY9_wix_import_test.html','assets','motility9','tasteroaming'])
    await cp(path.join(root, name), path.join(out, 'site', name), { recursive: true });
  await writeFile(path.join(out, 'README.txt'), 'REVIEW ONLY — NOT PUBLISHED\nOpen review.html for before/after captures.\nFor working root-relative website links: cd site; python3 -m http.server 8750 --bind 127.0.0.1\nOpen http://127.0.0.1:8750/ in a browser.\nCNAME is intentionally omitted from this preview bundle. Do not deploy or submit draft policy URLs to Play Console.\n');
  console.log(JSON.stringify({ status: report.status, layoutChecks: report.checks.length, axeChecks,
    screenshots: report.screenshots.length, issues: report.issues.length, out }, null, 2));
  if (report.issues.length) { console.error(JSON.stringify(report.issues.slice(0, 25), null, 2)); process.exitCode = 1; }
} finally {
  await browser?.close();
  server?.kill();
}

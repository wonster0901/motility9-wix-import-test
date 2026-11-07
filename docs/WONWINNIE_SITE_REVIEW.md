# WONWINNIE multi-app site — review handoff

**Staged source only. Do not merge or publish without owner approval.**

Branch: `site/multiapp-restructure-20261107` · existing Draft PR #1.
Production/source baseline: `3497d2fab1c3f22aa5d08a075b4abcb839d31ea3`.

## URL matrix

| URL | Before | Proposed branch | Preservation / gate |
| --- | --- | --- | --- |
| `/` | MOTILITY9 home | WONWINNIE brand home; two product cards, About, Support | Brand copy from approved deck |
| `/motility9/` | Not present | Original MOTILITY9 home | Original main copy, 11 image payloads/order and purple CSS preserved; publisher return link and accessibility corrections |
| `/motility9/privacy/` | Not present | MOTILITY9 privacy | Original 12 sections and 5 September 2026 effective date |
| `/motility9/support/` | Not present | MOTILITY9 support | Original setup, records, camera and PDF answers |
| `/motility9/terms/` | Not present | MOTILITY9 terms | Original wording and 23 August 2026 effective date |
| `/tasteroaming/` | Not present | TasteRoaming Coming Soon | 2,667 dishes, 184 destinations, HERE/TRIP/WORLD, offline collection and honest map handoff |
| `/tasteroaming/privacy/` | Not present | App-specific review draft | Visible not-effective notice, no effective date, noindex; **not ready for Play submission** |
| `/tasteroaming/support/` | Not present | Support and approved FAQ | No registration, offline browsing versus external maps, verified language fallback |
| `/tasteroaming/terms/` | Not present | App-specific review draft | No invented jurisdiction, price, refund waiver or operating purchase claim |
| `/privacy.html` | MOTILITY9 privacy | Same original policy body/date | Not redirected or replaced with a shared policy |
| `/support.html` | MOTILITY9 support | Same original support body | Navigation points to MOTILITY9, not the brand home |
| `/terms.html` | MOTILITY9 terms | Same original terms body/date | Not redirected or removed |
| `/MOTILITY9_wix_import_test.html` | Historical import | Byte-for-byte original | Retained as historical HTML; not added to new navigation |

All new/migrated navigation uses root-absolute URLs and directory `index.html`
pages. The retained historical import keeps its working original relative links.
No route relies on JavaScript routing or a pretend redirect.

## What changed and what did not

- Eleven existing inline image payloads were extracted without recompression.
  The shared icon is reused, and the actual Result Review/eye crops are retained.
  `docs/site-preservation.json` records original file/CSS/image digests.
- Original MOTILITY9 CSS was extracted unchanged. A separate accessibility
  stylesheet adds 48px targets, clear focus, a publisher return landmark, and
  readable meta/PDF-preview contrast. These are layout/contrast changes, not
  legal or medical-claim edits. Root legal files therefore have new HTML/CSS
  references, **not** identical whole-file bytes; their original main text,
  dates and image bytes are checked against the baseline Git objects.
- MOTILITY9's original whole HTML remains recoverable in Git. The historical
  import and `CNAME` remain byte-identical. Do not mistake the relocated page
  for a newly invented app screenshot or clinical feature.
- TasteRoaming deliberately has no gallery, fabricated app icon, food images,
  ratings, restaurant pins or download CTA. No approved TasteRoaming imagery was
  present in this website repository. Its own white/lime/red treatment is separate
  from MOTILITY9's purple design.
- There is no verified official MOTILITY9 store URL in the supplied website
  source, so no Google Play URL was invented for either product.
- Production HTML loads only local styles/images: no added JavaScript, forms,
  analytics, cookies, external fonts or third-party embeds. This source finding
  does not claim anything about hosting/server logs outside the repository.
- npm dependencies are QA-only (Playwright and axe-core); there is no frontend
  build framework or runtime dependency. No paid service was introduced.
- No Flutter/app code, Play Console, Wix draft, DNS, Zoho or deployment setting
  was changed. CI has read-only repository permissions and no deployment job.

## Reproduce checks and preview

From the repository root:

```sh
python3 tools/check_site.py
npm ci --ignore-scripts
npx playwright install --with-deps chromium
npm run test:browser
```

In the Codex environment, system Chromium can be reused by setting
`CHROMIUM_PATH=/usr/bin/chromium`. Browser tests start a loopback-only server
automatically unless `SITE_PREVIEW_URL` is provided.

For interactive local preview:

```sh
python3 -m http.server 8750 --bind 127.0.0.1
```

Open `http://127.0.0.1:8750/`. Serve the repository root, not a product subfolder,
because links intentionally start at the site root. Do not upload the branch to
the live host or change Pages/DNS settings to obtain a preview.

The **Website review only** Actions workflow publishes a review Artifact, not a
website. Its bundle contains:

- `review.html` and `screenshots/`: before/after captures from actual Chromium;
- `site/`: a locally servable HTML/CSS/image preview, with `CNAME` intentionally omitted;
- `static-report.json`, `browser-report.json`, `review-metadata.json`: results,
  exact source commit and file SHA-256 values.

Open `review.html` for comparisons. To test links from the extracted Artifact,
serve its `site/` folder with the same Python command. The Artifact is retained
for 30 days; screenshots can be regenerated from source.

## Automated review coverage

- Static: thirteen HTML routes, internal links/fragments/assets, metadata/lang,
  image alt attributes, no invented store links, draft-policy marking, exact
  original policy/main copy, original CSS/image hashes and unchanged CNAME/archive.
- Browser: twelve navigated pages at 320, 375, 430, 768, 1280 and 1440px;
  100%/200% text. Resizing includes original pixel-based typography; the PDF
  illustration retains image semantics. Images are scrolled into view so lazy
  loading is checked rather than incorrectly treated as a missing asset.
- Keyboard: first Tab skip link, focus transfer to main, native mobile menu
  opening, link focus and closing. Controls are measured at >=48px in both axes.
- Accessibility: axe WCAG A/AA/2.1 AA and best-practice checks on every navigated
  page at desktop and at 320px/200% text. No violation is waived to get PASS.
- Screenshots: original main/privacy at desktop/mobile; brand, migrated MOTILITY9,
  TasteRoaming, legacy privacy and TasteRoaming privacy after the change, plus
  200% text captures of the three landing pages.
- The retained historical import is byte-preserved and statically checked; it is
  not silently restyled or represented as a newly remediated accessibility page.

Live-host read-only HTTP probes on 2026-11-07 returned 200 for `/`, `/privacy.html`,
`/support.html`, `/terms.html`. This does not validate new, unpublished routes or
worldwide/mobile rendering. PC Work should confirm actual HTTPS routing after
an owner-approved publication; no live before/after deployment was performed.

## Remaining publication gates

1. Owner approves exact page/link/design changes and any final legal wording.
2. Complete the [TasteRoaming code/data-flow review](TASTEROAMING_PRIVACY_REVIEW.md):
   actual ads/UMP and purchase/server settings, retention/deletion, backups,
   support handling and Play Data safety consistency. Drafts must not be submitted
   as final policies or become effective merely by merging this website PR.
3. Confirm the exact released MOTILITY9 Play URL before adding a download link.
4. PC Work checks mobile/desktop appearance, browser zoom, keyboard/screen-reader
   behavior and existing legal URLs. Source/browser automation is not legal approval.
5. Only after explicit publish/merge approval: verify the new directory routes,
   legacy paths and HTTPS from actual browsers; test mailbox delivery separately
   with authorization. Keep Wix/DNS/Zoho/Play changes out of this implementation.

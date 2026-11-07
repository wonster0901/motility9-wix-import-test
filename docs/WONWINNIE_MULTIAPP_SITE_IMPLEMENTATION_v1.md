# WONWINNIE Multi-App Website — Implementation Brief v1.0
Date: 2026-11-07
Status: APPROVED DIRECTION / IMPLEMENTATION NOT YET STARTED
Base repository: wonster0901/motility9-wix-import-test
Base commit: 3497d2fab1c3f22aa5d08a075b4abcb839d31ea3

## 0. Purpose and ownership
Turn the existing MOTILITY9-only public website into WONWINNIE's multi-app product site, retaining all existing live MOTILITY9 content and compliance URLs. TasteRoaming has been created as a Google Play Console app but has not been released. This is a staged WEBSITE change, not an app-code change.

Roles:
- ChatGPT: IA, copy/design direction, review.
- Codex: implement in a non-production website branch; static checks and staging preview.
- PC Work: read-only public preview checks across desktop/mobile and legacy links.
- Owner: explicitly approves publishing/merging changes affecting the live site.

**Do not deploy, merge into main, change DNS, alter Wix or Zoho settings, or edit Play Console during this phase.**

## 1. Verified existing stack and content
- Live host by prior deployment records: GitHub Pages, custom domain wonwinnie.com. Wix handles DNS, not public page hosting.
- Existing GitHub branch main contains CNAME, index.html, privacy.html, support.html, terms.html and a historical MOTILITY9_wix_import_test.html.
- Current index.html: MOTILITY9 hero "Standardized 9-Gaze Documentation"; three feature cards (9-Gaze Capture, Patient Records, PDF Reports); Result Review/PDF example images; "does not provide automated diagnosis" qualification.
- Current privacy.html contains 12 MOTILITY9-specific sections about local clinical data, camera, pseudonymous wallet, Google Play purchases, security, retention and support.
- Current support.html describes English/Korean UI, examination workflow and PDF exports.
- Current terms.html describes MOTILITY9 professional responsibility, local records, PDF exports and conditional report-credit purchases.
- Current pages use embedded base64 images, purple visual identity, English text and relative links. Original HTML and imagery are source of truth; do not replace with invented screenshots or marketing claims.
- The Wix account has a separate draft "Wonwinnie" site with /home, /privacy-policy, /support, /terms-of-use. **Do not edit or publish this draft.**
- Public browsing was not available in the audit tool; validate deployed URLs using PC Work on its actual browser before publishing. GitHub source inspection is verified, public rendering currently unverified.

## 2. Final information architecture
Route                                Purpose
/                                    WONWINNIE brand home (new)
/motility9/                           Existing MOTILITY9 landing page preserved
/motility9/privacy/                   Copy/current audited MOTILITY9 privacy
/motility9/support/                   Copy/current audited MOTILITY9 support
/motility9/terms/                     Copy/current audited MOTILITY9 terms
/tasteroaming/                        TasteRoaming landing page (new)
/tasteroaming/privacy/                App-specific privacy policy (requires verified app/SDK data flows)
/tasteroaming/support/                App-specific support (new)
/tasteroaming/terms/                  App-specific terms (draft only until approved)

**Legacy URLs that must remain functional with readable original MOTILITY9 content**:
/privacy.html
/support.html
/terms.html

Also preserve CNAME, HTTPS behavior and any actual Play Console or third-party links found during the rollout audit. Do not convert legacy URLs into broken links, homepage redirects or a generic privacy policy. New app legal URLs should each display the respective single app's policy.

Static directory pages should use index.html within each route directory, with internal links absolute from site root (e.g. /motility9/privacy/). Verify GitHub Pages support for chosen routing from staging before merge. Never silently assume a redirect works.

## 3. Visual architecture
- WONWINNIE homepage: neutral light base, restrained simple sans-serif, generous spacing, app cards. Avoid technical clichés or inflated corporate credentials.
- MOTILITY9: reuse original purple design system, layout, app assets and unchanged product claims. Add a discreet "WONWINNIE / All apps" return link; current navigation remains working.
- TasteRoaming: white/light background; bright lime-green and restrained red accents; use platform-like sans-serif; actual approved 4:3 food photography and approved app screenshots only. No invented app UI or food photos. If approved imagery isn't available to this repo, use a deliberate no-image layout pending approved assets.
- Responsive: mobile 320px–430px, tablet ~768px, desktop 1280px+. Visible 48px+ interactive targets, accessible focus states, readable 200% text, suitable contrast, no sideways scrolling.
- No new third-party analytics, cookies, trackers, web fonts or dependency-heavy build system unless explicitly approved.
- Existing 1.9 MB inline-image homepage can be improved by extracting assets and shared CSS **without changing image content**; distinguish optimization from redesign, preserve accessible alt text.

## 4. Brand and product content rules
Authoritative English draft copy is in docs/WONWINNIE_SITE_COPY_v1.md in this branch.
- WONWINNIE stands for a developer/publisher of practical mobile apps, not a healthcare diagnosis service.
- MOTILITY9: standardized 9-gaze capture/documentation, patient-linked exam records, PDF report; explicit "does not provide automated diagnosis" statement.
- TasteRoaming: HERE / TRIP / WORLD; 2,667 dish entries, 184 destinations; curated/offline catalog; Maps handoff, not a verified restaurant listing, booking service or guarantee of menu availability.
- TasteRoaming maps providers: Google Maps default, NAVER/Kakao for Korean search context with configured preference. Avoid claims of universal provider support or guaranteed destination-only results.
- TasteRoaming is **Coming Soon**, not available to download as of this phase. MOTILITY9 Play Store URL must be taken from current Play Console listing or publicly verified store link; never invent a store URL.
- Exclude ReelRoaming until owner confirms a public announcement.
- English primary; Korean privacy/support translations may be added only after both language versions are checked for legal and factual parity.

## 5. Privacy, terms and contact — RELEASE BLOCKERS
- TasteRoaming privacy/terms are independent of MOTILITY9 and must be based on reviewed current Flutter release implementation and actual planned operational integrations.
- Before a TasteRoaming privacy page is published as final, verify: location permission and raw-coordinate handling, in-device Recent/settings persistence, maps intent/web fallback, AdMob + UMP SDK data handling, Google Play Billing non-consumable purchase verification and restore, data retention/deletion, security and the contact mechanism. Carefully distinguish functionality already active from features not yet configured for production.
- Cross-check all text against Google Play Data safety/ads declarations. Do not claim no collection, no sharing, guaranteed anonymous behavior, or in-app account deletion without evidence.
- All policy pages need app name, developer name WONWINNIE, privacy inquiry address support@wonwinnie.com, effective/update date, data categories, purposes, sharing parties, retention, deletion and security as applicable.
- Google Play requires app-specific public HTTPS privacy pages accessible worldwide, no login, standard non-editable HTML (not a PDF), linked both in the listing and within the app. New TasteRoaming policy is **NOT RELEASE-READY** until checked. See Google Play "User Data" and "Prepare your app for review" official policies.
- Keep MOTILITY9's original policy text in legacy route; do not silently rewrite healthcare claims or legal terms. Flag any differences between text and current app operations for owner review.

## 6. Implementation scope (Codex)
1. Record main SHA and create a development branch **other than main** (this specification branch is available). Preserve originals verbatim as recoverable source.
2. Build brand home at /, with two product cards; internal privacy/support navigation via their app-specific pages.
3. Place exact original MOTILITY9 home and policy/support/terms content into /motility9/... paths. Fix relative links under nested directories. Preserve the 3 original root legal pages and the historic test HTML.
4. Build /tasteroaming/ with approved copy and a Coming Soon state. No faux app screenshots, false restaurants or nonfunctional Play button.
5. Build /tasteroaming/support/ with support@wonwinnie.com and FAQ reflecting offline catalog vs external Maps. Build draft privacy/terms in source, but do NOT present the legal pages as reviewed or submit a URL until legal/data-flow verification is complete.
6. Add basic metadata, per-page <title> and description, favicon if original approved asset, navigation/focus/alt checks, shared styles as appropriate, minimal performance optimizations.
7. Add non-destructive link and content checks (path existence, no stale nested relative URLs, 404s, no broken asset refs, old legal page content) and produce a before/after URL matrix.
8. Publish only a **draft PR** / staging preview URL, not main. If GitHub Pages preview would require deploying to the production custom domain, skip it; provide local screenshots or static build artifacts instead.

## 7. Verification and release gates
- No modifications to app repos, existing MOTILITY9 product behavior, Google Play, Wix, DNS, Zoho or Cloud.
- Existing root legal links /privacy.html /support.html /terms.html remain reachable and still show MOTILITY9 (not shared generic policies).
- New homepage routes to both products correctly; main CTA includes no invented Play Store URL.
- Original MOTILITY9 hero, photos and 9-gaze disclaimer unchanged.
- TasteRoaming counts/features match approved frozen catalog/QA2674; copy does not promise actual dish sales or geofenced results.
- Desktop/mobile/200% font, contrast, keyboard navigation, contact links, HTML lang/title/meta checks.
- Policy text marked review-required until code and actual services reconciled. Verify actual HTTPS pages from a browser before entering any policy URL into Play Console.
- Owner approves exact pages and link diff before merging and making public.
- After approved publication, PC Work confirms all 3 legacy URLs, 9 proposed new routes, HTTPS and contact link. Only then is TasteRoaming privacy URL eligible for Play Console submission.

## 8. Handoff record
- Base SHA: 3497d2fab1c3f22aa5d08a075b4abcb839d31ea3
- Draft branch: site/multiapp-restructure-20261107
- Repo: wonster0901/motility9-wix-import-test
- This document is a specification, not deployed site code.

# TasteRoaming — WEBSITE LAUNCH SWITCH (staged; NOT published)

**As of 2026-11-17, v9 is under first-production-review on Google Play.** This branch is a **post-publication switch only**. Do NOT merge while the store page is inaccessible, or only the review submission is confirmed.

## What this draft changes, and no more
- WONWINNIE home TasteRoaming product status: `COMING SOON` -> `AVAILABLE`; add the Play Store URL `https://play.google.com/store/apps/details?id=com.wonwinnie.taste_roaming`.
- TasteRoaming landing: replace Coming Soon copy with Android/Google Play availability and install links. Keep the approved food photos, 2,667 dishes, 184 destinations, maps caveats and existing layout.
- TasteRoaming public Privacy/Terms/Delete/Support footers: update **only** the status phrase after first publication; preserve legal content/effective dates and disclosures.
- Add two Support FAQ entries on adult Remove Ads purchase and Restore, retaining original support/data-deletion guidance.
- Unchanged: MOTILITY9 pages and availability, app-ads.txt, site images, Google Play/app code, consent/legal policies, and original release artifacts.

## REQUIRED GO/NO-GO before merging this PR
1. Verify **public installability**, not merely Google approval or the Play Console's `under review` text. From a signed-out browser open https://play.google.com/store/apps/details?id=com.wonwinnie.taste_roaming and verify it is the real TasteRoaming listing with Android Install support for intended countries.
2. Confirm the Play listing publisher, app package `com.wonwinnie.taste_roaming`, v9 public version, and absence of misleading ad/purchase claims. Record reviewer/date.
3. Existing site source remains on GitHub Pages (CNAME `wonwinnie.com`). **Check actual deployed hosting** before merge. GitHub source changes may deploy automatically on main.
4. Validate this branch's `site-review` workflow; confirm links, 8 approved food-photo assets and policy language. Explicitly review no legal substance was rewritten.
5. Merge this PR only after (1)–(4); afterwards verify public `https://wonwinnie.com/`, `/tasteroaming/`, `/tasteroaming/support/`, Privacy, Terms, Delete Data, and `/app-ads.txt` using a fresh browser. Record timestamp/status and rollback path.

## Avoid confusion
- Open website PR #2 was created from an older base and already overlaps published policy cleanup; don't merge it automatically.
- No Wix draft site edit is needed for this GitHub Pages source. Wix's separately listed `Wonwinnie` Draft is not proof that the live domain uses Wix.
- Don't submit a new AAB, reconfigure billing/cloud, or alter app images/DB as part of this website switch.

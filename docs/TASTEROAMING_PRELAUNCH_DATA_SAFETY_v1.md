# TasteRoaming — Google Play Data safety & privacy alignment checklist (prelaunch)

Source of truth: TasteRoaming Flutter `daf23f467fdc854e941007b23134d27f952f5fb4`, AdMob set up 2026-11-07 as described by the owner, and Google Play User Data policy / Google Mobile Ads Android SDK disclosures.

**Status: review matrix only, NOT an actual Play Console declaration.** Only the app publisher can confirm current SDK runtime, purchases, consent and submitted disclosures.

| Potential Play Data safety category | Evidence and expected disclosure | Release action |
| --- | --- | --- |
| App activity / interactions | Google Mobile Ads SDK can collect ad/app activity and ad interactions for ad delivery and measurement; app keeps 20 visible Recent IDs locally. | Identify any GMA/UMP collection/sharing after production integration; do not mark no collection merely because Recent is local. |
| Device or other IDs | Google Mobile Ads SDK can collect advertising ID, app set ID and other eligible device identifiers for ads/security. | Inspect merged manifest and SDK configuration; disclose identifiers as applicable. |
| App info and performance / diagnostics | Google Mobile Ads SDK can transmit diagnostics and performance signals. | Disclose in Play Data safety per official SDK docs. |
| Approximate location | App uses Android COARSE_LOCATION for opt-in foreground country lookup; OS geocoder/external map may receive coordinates; AdMob IP may reveal approximate location. | Distinguish app use, external SDK/OS sharing, and provider-collected location; do not claim no location handling. |
| Purchase history | Future Google Play non-consumable Remove Ads and verification service may process tokens, SKU, status, entitlement/refund state. | Declare final purchase data handling only after actual Play SKU/server integration. |
| Support email | Voluntary email sent to `support@wonwinnie.com`; receives email address and support content. | Confirm retention/deletion procedure for mail account. |
| Data deletion | In-app account creation absent. Local data can be cleared via Android app storage, but platform backups may survive uninstall. | Check restore/backup flags and supported deletion process. |
| Encryption in transit | Google says GMA SDK transmits collected data using TLS; other providers apply own procedures. | Validate all configured app-to-server calls use TLS; cannot assert a new unconfigured server is encrypted. |

## User-facing candidate pages
- `/tasteroaming/privacy/` — 11-section end-user privacy candidate; not final until reviewed and approved.
- `/tasteroaming/terms/` — 7-section terms candidate; not final.
- These pages intentionally remain `noindex,nofollow` and display **Review draft — not effective**. This is NOT access control; do not publish these public routes without finalizing them.
- Google Play requires public non-editable HTTPS privacy URL in both Play Console and the app, with disclosure aligned to Data safety.

## AdMob details confirmed by user's screens 2026-11-07
- AdMob account created, review ongoing; payment setup red banner unresolved.
- TasteRoaming Android app created as not yet published; "Needs review".
- Banner (`TasteRoaming_Banner`) and Interstitial (`TasteRoaming_Interstitial`) units created.
- Europe GDPR / US State consent message drafts saved but NOT published.
- app-ads.txt seller line on website branch: `google.com, pub-7531346675720700, DIRECT, f08c47fec0942fa0`. This is not live until website deploy.

## Remaining release gates — one checklist
1. Configure production Ads SDK **app ID and ad unit IDs**, verify UMP messages/required consent and client privacy setting, test actual test-device behavior.
2. Decide whether Remove Ads will launch on day one; if yes, configure SKU, Google Play billing and trusted server purchase verifier, ownership/restore/refunds and a concrete retention/deletion policy. If not, do NOT enable the purchase function in production and keep policy accurately conditional.
3. Confirm support email retention/deletion practice and actual release Android backup permissions.
4. Finalize user-facing legal copy, privacy contact, effective date and all providers/transfers; obtain owner approval, remove draft/noindex markers, rerun static/browser CI.
5. Publish website by explicitly owner-approved merge, verify `https://wonwinnie.com/tasteroaming/privacy/` and `/app-ads.txt` plus all MOTILITY9 legacy URLs.
6. Enter privacy URL into Play Console and AdMob, publish UMP messages where ready, complete Play Data safety and ads declaration consistently.
7. Do not upload QA APK or grant Remove Ads before trusted purchase verification; production release remains gated.

Official reference URLs:
- https://support.google.com/googleplay/android-developer/answer/10144311
- https://support.google.com/googleplay/android-developer/answer/9859455
- https://developers.google.com/admob/android/privacy/play-data-disclosure
- https://developers.google.com/admob/flutter/privacy

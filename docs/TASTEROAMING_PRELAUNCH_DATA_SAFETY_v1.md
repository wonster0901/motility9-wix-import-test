# TasteRoaming — Google Play Data safety & privacy alignment checklist (prelaunch)

Sources: previously installed QA2674 source `daf23f467fdc854e941007b23134d27f952f5fb4`, the unmerged billing Draft PR #22 code `8981e71e6482a75edefb1cd6aefc4c329c4ea6b0`, AdMob setup records of 2026-11-07, and Play/Google Mobile Ads disclosures. Do not describe the draft backend as a deployed operating service.

**Status: review matrix only, NOT an actual Play Console declaration.** Only the app publisher can confirm current SDK runtime, purchases, consent and submitted disclosures.

**2026-11-09 state update (no policy approval):** Cloud Run `tr-billing` is deployed in Seoul with billing disabled, and a Google Play RTDN test message was received on a Pull-only subscription. No paid transaction, user entitlement, refund/revocation event processing, Push callback, scheduler, production advertising or operating retention/deletion procedure is verified by those tests. The earlier source sentence about an undeployed backend describes the dated design baseline, not the present disabled infrastructure. The candidate site PR remains Draft; `/tasteroaming/privacy/` and `/tasteroaming/terms/` remain review-only, not usable as effective Play privacy/terms URLs.


| Potential Play Data safety category | Evidence and expected disclosure | Release action |
| --- | --- | --- |
| App activity / interactions | Google Mobile Ads SDK can collect ad/app activity and ad interactions for ad delivery and measurement; app keeps 20 visible Recent IDs locally. | Identify any GMA/UMP collection/sharing after production integration; do not mark no collection merely because Recent is local. |
| Device or other IDs | Google Mobile Ads SDK can collect advertising ID, app set ID and other eligible device identifiers for ads/security. | Inspect merged manifest and SDK configuration; disclose identifiers as applicable. |
| App info and performance / diagnostics | Google Mobile Ads SDK can transmit diagnostics and performance signals. | Disclose in Play Data safety per official SDK docs. |
| Approximate location | App uses Android COARSE_LOCATION for opt-in foreground country lookup; OS geocoder/external map may receive coordinates; AdMob IP may reveal approximate location. | Distinguish app use, external SDK/OS sharing, and provider-collected location; do not claim no location handling. |
| Purchase history / app financial activity | PR #22 implements proposed non-consumable Play purchase/restore, SKU and status checks, owner-bound token hash/encrypted token, entitlement/ACK/refund ledger and signed proofs, but live billing remains disabled. | Confirm Play Data safety category and operating storage/retention based on actual service configuration and real production package. |
| User ID / authentication (billing-only) | A Google identity token is proposed for explicit purchase/restore, creating a pseudonymous owner binding; the app's normal offline food discovery does not require sign-in. Server/device flow also handles public-key proof and Play Integrity verdicts. No Google email/profile is stored as the purchase-owner claim in the PR design. | Confirm actual OAuth scopes, account-binding UX and any identity identifiers sent to Google and backend; disclose only verified operational practice. |\n| Device integrity / security | Proposed service verifies Play Integrity, device possession and signed proof; app/server process cryptographic identifiers and non-exportable Keystore keys. | Verify final provider SDK transmission, retention and classification in the submitted Data safety declaration. |\n| Support email | Voluntary email sent to `support@wonwinnie.com`; receives email address and support content. | Confirm retention/deletion procedure for mail account. |
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

# TasteRoaming website privacy review

Review date: 2026-11-07 (Asia/Seoul). **NOT A FINAL POLICY / DO NOT SUBMIT TO PLAY.**

**2026-11-09 operational reconciliation (draft review only):** Google Cloud Run `tr-billing` was deployed on 2026-11-08 in project `tasteroaming` with `BILLING_ENABLED=false`; the live deployment's `/health` returned 200 and its deliberately disabled `/ready` returned 503. The Play Console RTDN `testNotification` was received by the inert Pub/Sub Pull subscription and acknowledged. These are infrastructure/preparation proofs only, **not** live purchase verification, refund handling, actual Google Play entitlement, RTDN Push/Scheduler or operational privacy approval. The older code review table below records its historical 2026-11-07 baseline and must not be read as the current deployment state. The proposed legal pages remain not effective, noindex and unapproved for Play/UMP; server retention, deletion/backup, support-mail handling, identity binding and provider disclosures remain open.


Initial app baseline: `wonster0901/taste_roaming` QA2674 source
[`daf23f467fdc854e941007b23134d27f952f5fb4`](https://github.com/wonster0901/taste_roaming/tree/daf23f467fdc854e941007b23134d27f952f5fb4).
Billing implementation cross-reference: Draft PR #22 at
[`8981e71e6482a75edefb1cd6aefc4c329c4ea6b0`](https://github.com/wonster0901/taste_roaming/tree/8981e71e6482a75edefb1cd6aefc4c329c4ea6b0).
The latter is implemented and CI-tested but NOT merged, deployed, activated or approved as the production privacy contract.
The site pages are still drafts. No Android app, accounts, deployed systems or user data were changed.

The new `/tasteroaming/privacy/` and `/tasteroaming/terms/` are substantive,
app-specific **review drafts**, visibly marked not effective, with no effective
date and `noindex,nofollow`. Footer links explicitly say review draft. They are
not a claim of release readiness, a published legal policy or an approved Play URL.
MOTILITY9's Wallet/clinical policy is not reused for TasteRoaming.

| Topic | Confirmed in reviewed code | Source | Unresolved before final publication |
| --- | --- | --- | --- |
| Developer/contact | WONWINNIE and the approved support address come from the website brief; no personal account is required by the current discovery UI | Website brief; app `lib/main.dart`, `pubspec.yaml` | Owner identity/contact ownership and actual mailbox delivery/handling |
| Offline catalog | Catalog/images are packaged; 2,667 foods, 184 destinations; external maps are separate | `lib/data/repositories/catalog_repository.dart`, bundled mapping; QA2674 record | Actual final release must match these counts; no restaurant/menu verification inferred |
| Location permission | Android requests COARSE_LOCATION and INTERNET, no FINE/BACKGROUND permission in the app manifest | `android/app/src/main/AndroidManifest.xml` | Final merged manifest and all SDK disclosures must be reviewed |
| Country confirmation | Explicit Auto opt-in; manual choice; foreground lookup, bounded requests, OS geocoding; nearby handoff uses an existing permission, not a forced permission request | `lib/domain/home/country_locator.dart`, `home_mode_controller.dart`, `lib/domain/maps/physical_market_resolver.dart` | OS/geocoder provider-specific transmission, notices and final device behavior |
| Coordinates/country evidence | Session memory only; fix lifetime five minutes, country evidence thirty minutes. Suspend cancels lookup and invalidates coordinates. Manual recommendation country is separate | `physical_market_resolver.dart`, `search_market_policy.dart`, `recommendation_context.dart` | Do not claim OS/geocoder itself stores nothing; no first-party location backend is configured |
| Maps handoff | Food query and fresh coordinates where applicable; TRIP uses destination without device GPS. Google default; Korean providers only for KR-targeted context, with web fallback | `map_handoff.dart`, `map_launcher.dart`, `map_provider_policy.dart` | Provider/browser collection and policies; search relevance is not a privacy or restaurant-quality PASS |
| Recent/settings | Recent view uses twenty unique dish IDs; HERE mode/manual country, TRIP and map preference saved with SharedPreferences | `recent_repository.dart`, `trip_destination_repository.dart`, `map_preference_repository.dart` | No claim of app-level encryption or a persistent language preference |
| Recovery records | Bounded recovery copies of malformed earlier values may be retained | `local_state_migration.dart` | Do not promise only twenty IDs are ever stored or that replacing Recent deletes recovery copies |
| Ad records/proof cache | Completion/cap/day/last-ad state and an opaque verifier proof can be persisted | `monetization_repository.dart` | No production proof issuer is connected; no indefinite local entitlement claim |
| Ads/UMP | Official test IDs only, explicit test opt-in, non-Release native build; UMP gates requests and required Settings privacy options | `admob_gateway.dart`, `main_ads_qa.dart`, `monetization_controller.dart` | Operating AdMob IDs, UMP messages, jurisdiction/personalization behavior, current SDK data disclosures and actual consent QA remain gates |
| SDK networking | UMP and Google SDKs may communicate separately from food browsing. No separate first-party analytics/Crashlytics dependency identified | `pubspec.yaml`, `admob_gateway.dart` | SDK presence and disabled live serving do not prove zero collection/sharing; final SDK versions and merged permissions matter |
| Billing | PR #22 provides a guarded billing runtime, nonconsumable Play purchase verifier, account-owner binding and signed server proof; ordinary food browsing requires no account, but explicit buy/restore proposes Google identity authorization. Billing is disabled via `BillingRuntime.activationApproved=false`. | PR #22 `lib/domain/billing_runtime.dart`, `lib/domain/billing_http.dart`, `backend/purchase_verifier/README.md` | Owner approved Google sign-in only for explicit purchase/Restore and account-bound reinstall/new-device restoration on 2026-11-09. Still require real Play license tests, identity-provider disclosures, retention/deletion, and live-billing activation approval before publication |
| Purchase identity / integrity | The proposed billing-only flow uses Google ID-token verification to establish a pseudonymous owner HMAC, Play purchase-token hash, KMS-encrypted token, Android Keystore device public key, Play Integrity evidence and Firestore entitlement/ACK/refund ledger. No email/profile is stored as the ownership claim. | PR #22 `backend/purchase_verifier/README.md`, `service/core.py`, `service/ledger.py`, `service/proof.py` | Confirm actual server region/operators, collected data categories, cross-border transfers, service-account permissions, retention, deletion, device/account rebind, and public-facing disclosures |
| Offline entitlement | PR #22 has signed online purchase revalidation; production `EntitlementCachePolicy.disabled()` remains in effect. Neither a 14-day proposal nor earlier 24h/6h mock policy is approved. | `lib/domain/entitlement_cache_policy.dart`, `billing_runtime.dart`, PR #22 backend README | Explicit trusted-time/offline entitlement decision and actual network/clock/refund verification; do not claim offline purchased rights or a policy expiry |
| Deletion/backups | No dedicated Clear Recent/account-deletion screen identified. Android app-data controls remove app storage; manifest does not explicitly disable backup | `settings_screen.dart`, repositories, Android manifest | Platform backup/restore behavior and deletion guidance must be confirmed; uninstall is not asserted to erase backups |
| Email support | Only `mailto:support@wonwinnie.com` is provided; no new form or mailbox integration | Website support pages | Mail provider access, retention/deletion, support process and delivery are not verified by a mailto link |
| Public policy link | Settings reads `TASTEROAMING_PRIVACY_POLICY_URL`; missing value shows an accurate QA notice | `settings_screen.dart` | Configure an approved final public HTTPS page only after publication and real-browser checks |
| Release state | Production release is blocked; no operating signing/ads/verifier setup is implied | `android/app/build.gradle.kts` | Public policy approval, final SDK/Data safety reconciliation and release preparation are separate from this website PR |

## External policy references checked

- [Google Play User Data policy](https://support.google.com/googleplay/android-developer/answer/10144311)
- [Google UMP Flutter guidance](https://developers.google.com/admob/flutter/privacy)
- [Google Privacy Policy](https://policies.google.com/privacy)

These sources do not establish the owner's actual Console configuration. No
Data safety, consent, sale/sharing, retention period, jurisdiction or account-
deletion assertion is invented. Final wording requires owner/legal review and
actual operational configuration, including SDK data-handling documentation.

## MOTILITY9 boundary

The original MOTILITY9 main/legal copy, image payloads and effective dates are
migration baselines, not a fresh audit of its backend. The Wallet/clinical-data
claims (including anonymous/pseudonymous terminology and retention/deletion)
must be reconciled with its actual operations by its owner if they change.
This PR preserves them rather than silently rewriting the existing policy.

# TasteRoaming website privacy review

Review date: 2026-11-07 (Asia/Seoul). **NOT A FINAL POLICY / DO NOT SUBMIT TO PLAY.**

Read-only source reviewed: `wonster0901/taste_roaming` at
[`daf23f467fdc854e941007b23134d27f952f5fb4`](https://github.com/wonster0901/taste_roaming/tree/daf23f467fdc854e941007b23134d27f952f5fb4),
the QA2674 source. No app repository changes, SDK requests, account settings,
device operations or purchases were made for this website work.

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
| Billing | Non-consumable buy/restore, token verification interfaces; main uses `UnconfiguredPurchaseVerifier` and an empty default SKU | `play_purchase_gateway.dart`, `monetization_services.dart`, `main.dart` | Real SKU, server contract/owner, authenticated ownership, token ledger, acknowledgement, refund/revocation, security and retention/deletion |
| Offline entitlement | Bounded-cache interface exists but production policy is disabled; no operating cryptographic verifier | `entitlement_cache_policy.dart`, `monetization_controller.dart` | 24h/6h is only a proposal; proof authenticity, trusted time and replay defense are not operational |
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

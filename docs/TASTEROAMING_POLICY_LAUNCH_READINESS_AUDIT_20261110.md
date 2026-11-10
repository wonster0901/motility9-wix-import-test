# TasteRoaming 정책 최종검수 및 운영 연결 게이트 — 2026-11-10

**상태: 내부 검수 문서 / 사용자에게 공개되는 개인정보처리방침 아님 / Public release HOLD.**

본 문서는 2026-11-10까지의 실제 사용자/PC Work 콘솔 재조회 기록과 현재 웹사이트 Draft PR #1 및 TasteRoaming 앱 통합 소스를 대조한 **단일 최신 실행 기준**이다. 과거 시점 문서의 백업 OFF·Scheduler 없음·서명키 분실·출시 범위 미확정 등의 문구를 이번 작업의 현재 사실로 다시 취급하지 않는다. 실제 Google Cloud/Play/Zoho 콘솔에 직접 접근해 재검증한 보고서는 아니다.

## 1. 이미 완료되어 반복하지 않을 사항

| 범주 | 보존할 완료 기록 | 의미의 한계 |
| --- | --- | --- |
| 콘텐츠와 추천 | 2,667 음식·이미지, 승인 TRIP 관계. 새 추천 v1.1 Draft PR #26의 HEAD 12a374fc, Flutter 분석 오류 0건 및 1,164개 테스트 PASS | 실제 기기 QA는 PC Work 별도 진행 중. 원본 DB/이미지 수정 금지 |
| 기존 Play 앱 및 키 | 내부 테스트 versionCode 1 보존. 기존 upload keystore 비밀번호 확인, 기존 등록 업로드 인증서 지문 일치, 개인키 서명 PASS, 신규 키 재설정 요청 취소 | 이후 새 후보는 versionCode 2 이상·원래 upload key 사용. 암호·개인키 재요청 금지 |
| KMS/Play 권한 | Play Publisher 서비스 계정 앱별 권한, KMS proof/tokens 키, 실행 서비스 계정 권한, Play 앱 서명 인증서 확인 | 등록된 계정·키가 실제 Purchase API/서명 호출에 성공했다는 증명은 아님 |
| GCP 기초 설정 | Seoul Firestore 하루 1회·7일 보존 백업 일정 구성, PITR OFF, 두 요청/속도제한 TTL ACTIVE; Cloud Run billing disabled. RTDN Pull 전용, reconciliation Scheduler PAUSED | 마지막 검증에서 실제 백업 스냅샷 0건, 격리 복원 미실시. Scheduler/TTL/백업 일정을 재생성하지 않음 |
| 환불 증빙 | 같은 프로젝트의 private staging bucket, 독립 서명·해시 체인/복구 검증 소스, Draft PR #25 RTDN 점검 테스트 25 PASS | staging은 별도 관리된 원본/복구 불가능 불변 증빙이 아님 |
| 광고/상품 | AdMob App ID 및 배너/전면 단위 생성, UMP 유럽/미국 메시지 Draft, Play remove_ads/standard 상품 생성 이력 | 실제 게시·활성화·과금·라이선스 구매/환불 미검증 |
| 웹 소스 | Draft PR #1에 Privacy/Terms/Delete/Support 작성, website CI 42782320229 PASS | main에 미배포, Review draft - not effective 및 noindex/nofollow 유지; Play 제출 가능 URL 아님 |

**최초 공개 Android 출시 범위는 광고 + 비소모성 Remove Ads 구매 및 Restore 포함으로 확정됐다.** 구형 문서의 출시 시점 포함 여부 결정 요청은 다시 질문하지 않는다. 그러나 이는 실제 서비스 활성화 승인과 다르다.

## 2. 페이지별 검수 판정

| 페이지/절 | 현행 초안의 타당한 부분 | 최종 공개 전에 필요한 변경/확인 |
| --- | --- | --- |
| Privacy §1, §11 | 앱명 TasteRoaming, WONWINNIE, 한국, support@wonwinnie.com 표기 | 실제 Play 게시자·법적 개인정보처리자·책임 부서/연락 방법 정확히 일치. 회사 법인명·주소·책임자 임의 추정 금지 |
| Privacy §2–4 | 로컬 Recent 최대 가시 20개·설정·선택형 전경 위치·외부 지도 사업자 독립 처리 설명 | 실제 권한/데이터 흐름과 위치 원산지 오인 방지 문구 최종 대조. 단순 오프라인 앱이라고 모든 제3자 데이터 처리를 부정하지 말 것 |
| Privacy §5 | AdMob/UMP의 IP, 기기 식별자, 광고/앱 상호작용, 진단 데이터 가능성 명시 | 광고 동의 메시지 게시·거부/재선택/Privacy Options 기기 QA, 최종 Data safety와 일치 여부 확인. 사용자가 보는 정책에서 내부 개발 시기 표현 정리 |
| Privacy §6 | 평상시 무계정, 구매/Restore에서만 Google 인증, Google Play 결제, 소유권 검증과 복원·반환/회수 구분 | 실제 라이선스 구매/ACK/Restore/환불/권한회수 후 운영 사실로 수정. 2026-11-09 승인일, prerelease disabled, backend preview 등 내부 개발 경과는 최종 사용자용 정책에서 제거 |
| Privacy §7 | 기존 Zoho Mail Lite와 해결 후 90일 일반 문의, 법적 보존 예외·Zoho Trash 복구 한계 | 담당 운영자 배정, 현재 무해한 송수신 테스트 1회, 문의 분류/해결일/90일 주간 폐기 검수 실제 절차 확정 |
| Privacy §8 | Google/Android/NAVER/Kakao/Zoho 등 제3자 범주 및 국외처리 가능성 고지 | 법적으로 요구되는 수탁자/제3자, 목적, 국외 이전 국가/방식/보유기간/근거를 실제 제공자와 법 적용 사실에 맞춰 완성. '추후 추가 고지 예정'만으로 확정 금지 |
| Privacy §9 | 로컬 데이터 삭제·기기백업 한계, 결제 유효권 보존·법적 보존 예외 구분, 실제 스냅샷 0건 설명 | 백업 첫 실제 사본과 격리 복원, 원본과 독립된 환불 회수 기록, 본인 인증/열람/삭제/기기해지 운영 처리 실재성. 최종 정책에서 내부 미완료 시험/스냅샷 0·초안 상태 표현은 실제 운영 문장으로 재작성 |
| Privacy §10 | 전면적 보안을 과장하지 않는 설명 | HTTPS/TLS, 최소 접근, 결제 서버·KMS·로그의 최종 실제 보호 조치에 맞게 확정 |
| Terms §1,2,4–7 | 음식/지도 결과 비보증, 무료 탐색/제3자 조건·문의 경로 구분 적절 | 최종 책임 주체·지원 경로와 게시된 Privacy 내용 일치 |
| Terms §3 | 일회성 비소모성 Remove Ads, Google Play 현재 가격, 구매 복원 및 소비자 환불 권리 | 이미 확정된 출시 범위에 맞춰 planned/offline preview 표현을 공개 시 현재 운영 문구로 변경; 구매·환불·복원 실제 구현을 확인한 뒤 최종화 |
| Delete | 로컬 앱 데이터 제거와 서버 구매자 정보 삭제 구분, 유효 구매권·법적 예외 명시 | 본인 인증된 삭제 요청 처리와 응답 가능 절차. Google Play의 앱 내 계정 생성 해당 여부 결정; 해당하면 앱 내부·웹 외부 양쪽에서 계정 삭제 요청 경로 필요 |
| Support | 기초 FAQ, 문의 메일과 삭제 요청 링크 작성 | 사용자가 효력 없는 Draft 페이지에서 신청이 완료됐다고 혼동하지 않도록 최종 고객 안내 정리 |

**현재 페이지는 문안 구조 검토 PASS이나 대외 공개 운영 정합성은 HOLD이다.** 효력일만 정하거나 Draft 배너를 제거해서 게시하면 안 된다.

## 3. 소스와 이전 문서 간 구체적인 차이

1. 현재 Android 앱 통합 소스 Manifest에는 allowBackup=false, tr_backup_rules.xml 및 tr_data_extraction_rules.xml가 **이미 존재**하며 Android 11 이하와 12 이상의 백업·기기전송 제외를 설계했다. 따라서 'backup exclusion code를 새로 작성해야 한다'는 과거 문구는 최신 소스 기준 잘못됐다. 단, 실제 설치 v1에 반영됐다고 주장하거나 Android OEM 클라우드/D2D 실기기 검수 완료로 간주하지 않는다.
2. BillingRuntime.activationApproved=false, AdMobConfiguration.productionActivationApproved=false; Cloud Run BILLING_ENABLED=false. 앱·광고 식별자 및 Cloud Run 배포 사실만으로 구매/실광고 운영을 주장하지 않는다.
3. 설정의 TASTEROAMING_PRIVACY_POLICY_URL은 승인된 공개 HTTPS URL이 Release에 지정돼야 한다. 지금 경로가 미공개이고, QA 안내문으로 대체되는 설정을 공표 완료로 취급하지 않는다.
4. 구매자 소유권 HMAC, 암호화 Play 토큰, 서버 회수 tombstone 및 기기 binding은 과금 연결 코드에 있으나 **고객용 삭제 API·전체 보관만료·실제 법적 보존 분리 운영이 없다**. 내부 minimize_revoked 및 unlink_verified_owner_device helper는 관리자 인증/법률 허가가 아닌 코드 도구일 뿐이다.
5. 현재 동일 프로젝트의 환불 증빙 저장소는 staging. 별도 백업 영역 외부의 독립 custody·단조 sequence·실 Google Play 환불 소스 유입과 격리 복원 재검증이 없어 권한회수 보장은 미입증이다.
6. 웹사이트 PRELAUNCH_DATA_SAFETY_v1의 이전 'Remove Ads를 최초 출시 때 넣을지 결정' 항목은 **폐기**. 최초 공개 광고+구매/복원은 확정. Data safety 실제 신고 범주는 최종 SDK·billing 동작 및 provider 처리 범주로 정한다.

## 4. 미완료 항목 — 실행 순서와 권한 구분

| 선행도 | 실제 남은 작업 | 완료 정의 | 재작업·승인 방침 |
| --- | --- | --- | --- |
| A1 | PC Work 추천 v1.1 실제 기기 QA | 연결 기기·설치 빌드·모드/국가 전환·반복·Recent/지도/오프라인 결과가 PASS, FAIL, NOT_VERIFIED로 기록됨 | 이번 정책 검수에서 기기 설치/1,164 테스트 반복 금지 |
| A2 | 개인정보/약관/삭제 운영 문구 최종 확정 | 검증된 데이터 흐름·정확한 운영자·국외 이전·보존/삭제 근거·실제 처리책임자 확정 | 사용자 법적 확인 필요한 사실은 임의 작성하지 않음; 원문 Draft 유지 |
| A3 | Zoho 지원·정보주체 요청 실제 절차 | 지원 무해한 송수신 확인, 분류/권한/90일+법정 예외 실무 담당과 감사기록 정립 | 기존 Mail Lite 재설정·사업자 변경 불필요 |
| B1 | Firestore 첫 예약 백업 및 격리 복원 | 스냅샷 최소 1개, 원 DB 영향 없는 별도 DB 복원, TTL/권한/환불 tombstone 비교, 연습 결과 | 마지막 0건이므로 지정 일정 후 한 번만 재조회; 백업 일정 중복 생성 금지. 복원/과금 별도 승인 |
| B2 | 독립 환불 이력 custody·서명/보관·실환불 이벤트 | 실제 Play 환불/voided 이벤트부터 독립 서명·불변 head, 원본 복구와 대조하여 환불 권한 재부여 없음 증명 | 새 독립 리소스/키/과금·실서비스 연결 별도 승인; 합성 단위테스트 재실행만으로 대체 불가 |
| B3 | AdMob/UMP 활성화 전 검증 | UMP 게시·동의/거부/설정 Privacy Options·광고 빈도/SDK·Data safety 일치 | 실제 메시지 게시/광고 활성화는 별도 승인 |
| B4 | Google Play remove_ads/standard + 실제 라이선스 결제 검증 | 상품 가격/지역·상태 확정, 실구매·ACK·Restore·환불·회수, 서비스 API 호출 성공 | 상품 활성화/Cloud Run/RTDN Push·Scheduler 작동 별도 승인 |
| C1 | 최종 서명된 versionCode≥2 내부 후보 | PR #26 QA 통과 및 운영 안전장치 확인 후 원래 업로드 키로 단일 서명 후보 | 기존 내부 v1 보존. AAB 생성/업로드·PR 병합 별도 승인 |
| C2 | 웹 게시와 Google Play 제출 | 운영 완료 사실 기반 Privacy/Terms/Delete 효력일, 리뷰 배너 제거 및 승인; 실제 공개 HTTPS URL 및 app-ads.txt 검증; Data safety/앱 내부 URL | 실제 사이트 병합/배포, Play/UMP 공개·양도된 사용자 정보 변경은 별도 승인 |

### 공개 판정

- **앱 개발·콘텐츠:** 현재 기반 소스와 자동검증 자료 존재. PR #26 실기기 QA 기다림.
- **정책 문안:** 초안 구조 PASS, 실제 서비스 확정/법률 고지/효력일 HOLD.
- **실운영 결제/환불 복구:** 실제 복원·독립회수 증빙·Play 라이선스 테스터 HOLD.
- **광고/UMP:** 메타데이터·초안 존재, 실제 게시/QA/신고 HOLD.
- **PUBLIC RELEASE:** HOLD. Draft PR #1, app PR #22/#25/#26은 병합/배포하지 않는다.

## 5. 기준 링크

- 웹사이트 Draft PR #1: https://github.com/wonster0901/motility9-wix-import-test/pull/1
- Stage7 이슈 #21: https://github.com/wonster0901/taste_roaming/issues/21
- 추천 v1.1 PR #26 및 자동검증: https://github.com/wonster0901/taste_roaming/pull/26 / https://github.com/wonster0901/taste_roaming/actions/runs/42806131641
- RTDN 점검 PR #25: https://github.com/wonster0901/taste_roaming/pull/25
- Google Play 개인정보: https://support.google.com/googleplay/android-developer/answer/10144311
- Google Play 공개 Privacy URL 요건: https://support.google.com/googleplay/android-developer/answer/9859455
- Google UMP Flutter: https://developers.google.com/admob/flutter/privacy
- 대한민국 개인정보 보호법 제30조(2026-09-11 시행): https://www.law.go.kr/LSW/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1029332621

**개인정보 본문·신원자료·키/비밀번호·실제 거래내역은 이 문서에 기재하지 않음.**
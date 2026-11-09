# TasteRoaming — Zoho Mail Lite customer-support retention SOP
**Prepared:** 2026-11-09 · **Status:** owner review / NOT operating verified / NOT public.

## Existing confirmed setup, not a new mail provider
The project setup records identify `support@wonwinnie.com` as an existing **Zoho Mail Lite, 5 GB / one-user** mailbox. The 2026-09-05 project handoff records successful mail send/receive and SPF/DKIM/DMARC configuration. **These are historical handoff observations, not proof of current 2026-11-09 access, delivery or policy settings.** Do not create a duplicate Gmail, Google Workspace or Hostinger address; do not request mailbox passwords or MX changes.

## Relevant Zoho product distinction (checked 2026-11-09)
- Zoho's **eDiscovery/advanced organization-wide retention and legal-hold** is specified for **Mail Premium / Workplace Professional**, not Mail Lite. Do not present it as enabled or available without a plan change and verification. Official: https://www.zoho.com/mail/help/adminconsole/ediscovery-setup.html
- Zoho's current deletion help (updated 2026-11-03) states that mailbox-deleted messages move through **Trash** (5–180 days depending on the message received date and Junk Cleanup Interval), then may remain on Zoho servers **another 30 days**; specific admin recovery paths apply during that window. Therefore, moving a resolved ticket to Trash at +90 days **does not warrant a promise of physical deletion from all Zoho copies at +90 days**. Official: https://www.zoho.com/mail/help/data-deletion-policy.html
- Archiving is **not deletion** and does not automatically satisfy 90-day disposal: https://www.zoho.com/mail/help/archive-options.html
- Confirm current plan, Mail Settings → Junk Cleanup Interval (actual UI may vary), Trash/Spam policy, mailbox owner access, retention obligations and any independent mail client POP/IMAP copies. Nothing here changes live settings.

## Minimum operating workflow — retain only ordinary inquiry for 90 days after RESOLUTION
1. **Receive/triage:** Incoming email is either `OPEN`, `WAITING_FOR_CUSTOMER`, `RESOLVED`, `PRIVACY_REQUEST`, or `STATUTORY_HOLD`. These can initially be Zoho folders/tags or a small **restricted-access** operator case log. **Do not** put sender addresses, message content, device proofs, receipts or tokens in public GitHub issues or shared spreadsheets.
2. **Open/awaiting:** Keep only while needed for response. Do not auto-delete on the message received date; a ticket can stay open longer than 90 days.
3. **Resolution timestamp:** Record the date the final response was sent and the inquiry resolved, not the email's arrival date. Assign `delete_review_due = resolved_at + 90 calendar days`. Reopen only for genuine continuing response; record a new resolution event rather than silently resetting every old thread.
4. **Formal disputes/transactions:** Before deletion, segregate only the necessary records under applicable Korean e-commerce 3-year consumer-dispute / 5-year contract-payment rules (or different applicable law) after legal review. Mail is not automatically statutory evidence merely because the email is from a buyer. Retention request/legal hold takes precedence, with date and basis recorded.
5. **Weekly review:** A designated privacy operator checks cases with `delete_review_due <= today`; verifies resolved, no active hold, no reopened conversation, no incident response. Delete from Inbox/Sent/custom folders and record **operator, case ID, local deletion date, exception**. Never delete every mail older than 90 days and never auto-empty Trash until the exact Zoho behavior is understood and legal holds are safeguarded.
6. **Provider recovery:** Record Zoho Junk Cleanup Interval and additional server recovery duration separately from the operator's 90-day business-retention rule. Tell users that provider deletion occurs according to Zoho's separate lifecycle; do not claim instant erasure from backups, mail clients or third-party providers.
7. **Privacy requests:** Respond under approved case triage; verify ownership of paid Remove Ads using an independent Google-account-backed flow. **Do not accept emailed raw Play purchase tokens/Google credentials**. A support mailbox case is not, by itself, a verified entitlement deletion authorization.

## Pre-launch operator evidence (no personal messages/screenshots)
Request a screenshot or written readback showing **only**:
- **Zoho Admin Console → Subscription:** Mail Lite 5 GB plan, one active user; redact account IDs/payment details.
- **Zoho Mail → Settings:** current Junk Cleanup Interval and relevant retention/backup settings; redact message content.
- Whether `support@wonwinnie.com` can currently receive and send a harmless test email; report only `send PASS/FAIL` and `receive PASS/FAIL` (no customer content).
- Who is responsible for weekly case review (role title, not private staff credentials); existence of IMAP/POP forwards/other backups, and whether a restricted-access case log exists.
- Do not change any setting merely to provide screenshots. Do not provide passwords, recovery codes, private DNS administration tokens, or raw mailbox export files.

## Reconciliation with the privacy page
Public **candidate** wording should distinguish: "ordinary support inquiries are normally retained until resolved and for up to 90 days after resolution unless a legal hold applies; Zoho may retain deleted messages for an additional provider-defined recovery period." Keep all legal pages `Review draft — not effective` until current account settings and actual operating procedure are verified.

**Remaining blockers:** current Zoho Admin/mailbox verification, operator-assigned review process, exceptions and case log, provider recovery behavior, Korean/global legal review, confirmation of final public wording and actual site publication. No external deletion or mailbox mutation occurred.

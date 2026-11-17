#!/usr/bin/env python3
"""Read-only external HTTPS evidence for TasteRoaming's three policy pages."""
import json
import re
import urllib.error
import urllib.request
from urllib.parse import urlsplit

PAGES = {
    "/tasteroaming/privacy/": "TasteRoaming Privacy Policy",
    "/tasteroaming/terms/": "TasteRoaming Terms of Use",
    "/tasteroaming/delete-data/": "TasteRoaming Data Deletion Requests",
}
BAD = ("privacy notice draft", "require final approval before public use",
       "drafts are not final notices")


class SameOriginRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, newurl):
        target = urlsplit(newurl)
        if target.scheme != "https" or target.hostname != "wonwinnie.com":
            raise urllib.error.HTTPError(newurl, code, "unexpected redirect", headers, fp)
        return super().redirect_request(request, fp, code, msg, headers, newurl)


def probe(opener, path, expected_title):
    result = dict(path=path, status="UNVERIFIED", http_code=None,
                  expected_page_title=False, effective_date_found=False,
                  support_contact_found=False, draft_mismatch_found=None)
    request = urllib.request.Request("https://wonwinnie.com" + path,
                                     headers={"User-Agent": "TasteRoamingReadOnlyQA/1.0",
                                              "Accept": "text/html"})
    try:
        with opener.open(request, timeout=12) as response:
            result["http_code"] = response.status
            final = urlsplit(response.geturl())
            if final.scheme != "https" or final.hostname != "wonwinnie.com":
                return result
            if "text/html" not in response.headers.get("Content-Type", "").lower():
                return result
            content = response.read(250_001)
            if len(content) > 250_000:
                return result
            html = content.decode("utf-8", errors="replace")
            title = re.search(r"<title>\s*([^<]+)</title>", html, re.IGNORECASE)
            result["expected_page_title"] = bool(title and expected_title in title.group(1))
            result["effective_date_found"] = "Effective: 10 November 2026" in html
            result["support_contact_found"] = "mailto:support@wonwinnie.com" in html
            result["draft_mismatch_found"] = any(bad in html.casefold() for bad in BAD)
            result["status"] = ("PUBLIC_PAGE_BODY_VERIFIED"
                                if response.status == 200
                                and result["expected_page_title"]
                                and result["effective_date_found"]
                                and result["support_contact_found"]
                                and not result["draft_mismatch_found"]
                                else "PUBLIC_PAGE_NEEDS_REVIEW")
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, OSError) as exc:
        if isinstance(exc, urllib.error.HTTPError):
            result["http_code"] = exc.code
        result["note"] = f"unable to independently verify HTTPS ({type(exc).__name__})"
    return result


def main():
    opener = urllib.request.build_opener(SameOriginRedirect())
    pages = [probe(opener, path, title) for path, title in PAGES.items()]
    print(json.dumps({
        "status": "READ_ONLY_HTTPS_OBSERVATION_NOT_PUBLICATION_APPROVAL",
        "pages": pages,
        "all_pages_verified": all(p["status"] == "PUBLIC_PAGE_BODY_VERIFIED" for p in pages),
        "no_deployment_or_submission": True,
    }, indent=2))


if __name__ == "__main__":
    main()

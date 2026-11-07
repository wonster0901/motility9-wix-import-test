#!/usr/bin/env python3
"""Read-only link, HTML and source-preservation checks; never deploys."""
import base64
import hashlib
import json
from html.parser import HTMLParser
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
BASE = "3497d2fab1c3f22aa5d08a075b4abcb839d31ea3"
PATCH_BASE = "53c71a0"
STORE_URL = "https://play.google.com/store/apps/details?id=com.wonwinnie.motility9"
ROUTES = ["/", "/motility9/", "/motility9/privacy/", "/motility9/support/",
          "/motility9/terms/", "/tasteroaming/", "/tasteroaming/privacy/",
          "/tasteroaming/support/", "/tasteroaming/terms/", "/privacy.html",
          "/support.html", "/terms.html", "/MOTILITY9_wix_import_test.html"]
VOID = set("area base br col embed hr img input link meta param source track wbr".split())


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def original(name):
    return subprocess.check_output(["git", "show", f"{BASE}:{name}"], cwd=ROOT)


def file_for(route):
    return ROOT / (route.lstrip("/") + "index.html" if route.endswith("/") else route.lstrip("/"))


class Document(HTMLParser):
    def __init__(self, text, name, omit_store=False):
        super().__init__(convert_charrefs=True)
        self.name = name
        self.stack = []
        self.elements = []
        self.ids = []
        self.main_text = []
        self.title_text = []
        self.main_depth = 0
        self.title_depth = 0
        self.omit_store = omit_store
        self.omit_depth = 0
        self.feed(text)
        check(not self.stack, f"{name}: unclosed elements {self.stack}")

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.elements.append((tag, attrs))
        if self.omit_depth and tag not in VOID:
            self.omit_depth += 1
        elif self.omit_store and tag == "a" and attrs.get("href") == STORE_URL:
            self.omit_depth = 1
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "main":
            self.main_depth += 1
        if tag == "title":
            self.title_depth += 1
        if tag in ["br", "p", "div", "section", "h1", "h2", "h3", "li"] and self.main_depth:
            self.main_text.append(" ")
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        check(self.stack and self.stack[-1] == tag,
              f"{self.name}: mismatched closing {tag}, stack={self.stack}")
        self.stack.pop()
        if self.omit_depth:
            self.omit_depth -= 1
        if tag == "main":
            self.main_depth -= 1
        if tag == "title":
            self.title_depth -= 1
        if self.main_depth:
            self.main_text.append(" ")

    def handle_data(self, data):
        if self.main_depth and not self.omit_depth:
            self.main_text.append(data)
        if self.title_depth:
            self.title_text.append(data)

    @property
    def main(self):
        return re.sub(r"\s+", " ", "".join(self.main_text)).strip()


def image_digest(value):
    if value.startswith("data:image/"):
        return sha(base64.b64decode(value.split(",", 1)[1]))
    return sha((ROOT / unquote(urlsplit(value).path).lstrip("/")).read_bytes())


def webp_size(data):
    """Read actual WebP dimensions without an image-library CI dependency."""
    check(data[:4] == b"RIFF" and data[8:12] == b"WEBP", "Not a WebP file")
    check(int.from_bytes(data[4:8], "little") + 8 == len(data), "Truncated WebP")
    offset = 12
    while offset + 8 <= len(data):
        kind = data[offset:offset + 4]
        length = int.from_bytes(data[offset + 4:offset + 8], "little")
        chunk = data[offset + 8:offset + 8 + length]
        check(len(chunk) == length, "Truncated WebP chunk")
        if kind == b"VP8X":
            return (int.from_bytes(chunk[4:7], "little") + 1,
                    int.from_bytes(chunk[7:10], "little") + 1)
        if kind == b"VP8 ":
            check(chunk[3:6] == b"\x9d\x01\x2a", "Invalid VP8 frame")
            return (int.from_bytes(chunk[6:8], "little") & 0x3fff,
                    int.from_bytes(chunk[8:10], "little") & 0x3fff)
        if kind == b"VP8L":
            check(chunk[0] == 0x2f, "Invalid VP8L frame")
            bits = int.from_bytes(chunk[1:5], "little")
            return ((bits & 0x3fff) + 1, ((bits >> 14) & 0x3fff) + 1)
        offset += 8 + length + length % 2
    raise AssertionError("WebP has no dimension header")


def main():
    manifest_path = ROOT / "docs/TASTEROAMING_WEBSITE_IMAGES_v1.json"
    manifest_raw = manifest_path.read_bytes()
    check(sha(manifest_raw) == "45c3af9c4ed535a5b91ded32b597c1643fc760c238417fab95a15a295c8236df",
          "Approved image manifest changed; obtain explicit image approval")
    images = json.loads(manifest_raw)["selection"]
    approved = {"/" + row["path"]: row for row in images}
    check(len(images) == len(approved) == 8, "Exactly eight approved food photos required")
    check({"/" + str(p.relative_to(ROOT)) for p in (ROOT / "assets/tasteroaming").rglob("*") if p.is_file()} == set(approved),
          "Unapproved or missing food asset")
    for path, row in approved.items():
        data = (ROOT / row["path"]).read_bytes()
        check(sha(data) == row["sha256"] and len(data) == row["bytes"], f"{path}: original image hash/size")
        check(webp_size(data) == (row["width"], row["height"]) == (640, 480), f"{path}: original WebP dimensions")
    docs = {route: Document(file_for(route).read_text(), route) for route in ROUTES}
    references = 0
    external = set()
    for route, doc in docs.items():
        tags = doc.elements
        stores = [a for t, a in tags if t == "a" and a.get("href") == STORE_URL]
        check(len(stores) == (1 if route in {"/", "/motility9/"} else 0), f"{route}: approved store CTA must be retained only on its two approved pages")
        for a in stores:
            check(a.get("target") == "_blank" and {"noopener", "noreferrer"} <= set(a.get("rel", "").split()), f"{route}: store link safety")
        check(len(doc.ids) == len(set(doc.ids)), f"{route}: duplicate IDs")
        check(sum(t == "h1" for t, _ in tags) == 1, f"{route}: exactly one h1 required")
        check(any(t == "html" and a.get("lang") == "en" for t, a in tags), f"{route}: language")
        check(bool("".join(doc.title_text).strip()), f"{route}: title")
        check(any(t == "meta" and a.get("name") == "description" and a.get("content") for t, a in tags), f"{route}: description")
        check(any(t == "meta" and a.get("name") == "viewport" for t, a in tags), f"{route}: viewport")
        check(not any(t in ["script", "iframe", "form"] for t, _ in tags), f"{route}: no new scripts, frames or forms")
        for tag, attrs in tags:
            if tag == "img":
                check("alt" in attrs, f"{route}: missing image alternative")
                if attrs.get("src", "").startswith("/assets/tasteroaming/"):
                    check(route in {"/", "/tasteroaming/"} and attrs["src"] in approved, f"{route}: unapproved food image")
                    check(attrs.get("width") == "640" and attrs.get("height") == "480", f"{route}: food image aspect attributes")
                    check(route == "/" or bool(attrs["alt"].strip()), f"{route}: food image must have a useful alternative")
            value = attrs.get("href") if tag in ["a", "link"] else attrs.get("src") if tag == "img" else None
            if not value or value.startswith("data:"):
                continue
            if value.startswith("mailto:"):
                check(value == "mailto:support@wonwinnie.com", f"{route}: unexpected contact")
                continue
            if urlsplit(value).scheme:
                check(urlsplit(value).scheme == "https", f"{route}: insecure external link")
                if "play.google.com" in value:
                    check(
                        value == STORE_URL
                        and route in {"/", "/motility9/"},
                        f"{route}: unverified or misplaced store CTA",
                    )
                external.add(value)
                continue
            if route != "/MOTILITY9_wix_import_test.html":
                check(value.startswith(("/", "#")), f"{route}: nested relative URL {value}")
            target = urlsplit(urljoin("https://preview.invalid" + route, value))
            dest = file_for(target.path)
            check(dest.is_file() and dest.resolve().is_relative_to(ROOT), f"{route}: missing {value}")
            if target.fragment:
                target_doc = docs.get(target.path) or Document(dest.read_text(), target.path)
                check(unquote(target.fragment) in target_doc.ids, f"{route}: missing anchor {value}")
            references += 1
        if "/tasteroaming/" in route and any(x in route for x in ["privacy/", "terms/"]):
            text = file_for(route).read_text()
            check('content="noindex, nofollow"' in text, f"{route}: review indexing gate")
            check("Review draft — not effective" in text and "Effective date: not set" in text,
                  f"{route}: legal draft must be unmistakable")
        if "/tasteroaming/" in route:
            check(all(a.get("src") in approved for t, a in tags if t == "img"), f"{route}: no unapproved screenshots/photos")

    used = {a["src"] for t, a in docs["/tasteroaming/"].elements if t == "img"}
    check(used == set(approved), "TasteRoaming must display all eight approved food images")

    preservation = json.loads((ROOT / "docs/site-preservation.json").read_text())
    check((ROOT / "CNAME").read_bytes() == original("CNAME"), "CNAME changed")
    check((ROOT / "MOTILITY9_wix_import_test.html").read_bytes() == original("MOTILITY9_wix_import_test.html"), "historical HTML changed")
    for old, new in [("index.html", "/motility9/"), ("privacy.html", "/motility9/privacy/"),
                     ("support.html", "/motility9/support/"), ("terms.html", "/motility9/terms/")]:
        raw = original(old)
        baseline = Document(raw.decode(), old)
        check(sha(raw) == preservation["original_files"][old], f"{old}: baseline digest")
        # Only the approved store anchor is excluded; all other original copy
        # and every policy body still match exactly. No blanket substring waiver.
        current = Document(file_for(new).read_text(), new, omit_store=old == "index.html")
        check(baseline.main == current.main, f"{new}: original wording/effective dates changed")
        before = [image_digest(a["src"]) for t, a in baseline.elements if t == "img"]
        after = [image_digest(a["src"]) for t, a in docs[new].elements if t == "img"]
        check(before == after, f"{new}: original image bytes/order changed")
        if old != "index.html":
            legacy = docs["/" + old]
            check(legacy.main == baseline.main, f"{old}: legacy legal content changed")
            check([image_digest(a["src"]) for t, a in legacy.elements if t == "img"] == before, f"{old}: legacy icon")
    for route in ROUTES:
        if route not in {"/", "/motility9/", "/tasteroaming/"}:
            rel = str(file_for(route).relative_to(ROOT))
            before = subprocess.check_output(["git", "show", f"{PATCH_BASE}:{rel}"], cwd=ROOT)
            check(file_for(route).read_bytes() == before, f"{route}: policy/support/archive page changed by finishing patch")
    for row in preservation["images"]:
        data = (ROOT / row["path"].lstrip("/")).read_bytes()
        check(sha(data) == row["sha256"] and len(data) == row["bytes"], row["path"])
    for name, path in [("index.html", "assets/motility9.css"), ("privacy.html", "assets/motility9-legal.css")]:
        check(sha((ROOT / path).read_bytes()) == preservation["original_css"][name], f"{path}: original visual CSS rewritten")
    for css in (ROOT / "assets").glob("*.css"):
        check(not re.search(r"@import|@font-face|https?://", css.read_text()), f"{css}: external resource")
    result = {"status": "PASS", "routes": len(docs), "local_references": references,
              "preserved_image_payloads": len(preservation["images"]),
              "approved_food_images": len(images), "approved_food_bytes": sum(row["bytes"] for row in images),
              "legacy_policy_bodies": 3, "baseline_commit": BASE,
              "external_links_syntax_only": sorted(external), "production_deployed": False}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Notify IndexNow (Bing, Yandex, Seznam, Naver...) about changed pages after a deploy.

    python3 scripts/indexnow.py <base-commit> <head-commit>   # pages changed between two commits
    python3 scripts/indexnow.py --all                          # every URL in the live sitemap

Runs in GitHub Actions (.github/workflows/indexnow.yml) after each successful deploy.
The key is the name of the static/<key>.txt file, which the site serves at /<key>.txt.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOST = "haklidir.github.io"
BASE = f"https://{HOST}"
ENDPOINT = "https://api.indexnow.org/indexnow"


def key() -> str:
    keys = [p.stem for p in (ROOT / "static").glob("*.txt")
            if re.fullmatch(r"[0-9a-f]{32}", p.stem) and p.read_text().strip() == p.stem]
    if len(keys) != 1:
        sys.exit(f"expected exactly one IndexNow key file in static/, found {keys}")
    return keys[0]


def url_for(path: str) -> str | None:
    """Map a changed repository file to the public URL it affects."""
    p = Path(path)
    if p.parts[0] == "static":
        return f"{BASE}/{'/'.join(p.parts[1:])}"
    if p.parts[0] != "content":
        return None
    rel = p.parts[1:]
    if rel == ("_index.md",):
        return f"{BASE}/"
    if len(rel) == 1 and p.suffix == ".md":                 # content/service.md
        return f"{BASE}/{p.stem}/"
    if len(rel) == 2 and rel[1] == "_index.md":            # content/<section>/_index.md
        return f"{BASE}/{rel[0]}/"
    if len(rel) >= 3:                                        # content/<section>/<slug>/...
        return f"{BASE}/{rel[0]}/{rel[1]}/"
    return None


def changed_urls(base: str, head: str) -> list[str]:
    out = subprocess.run(["git", "diff", "--name-only", "--diff-filter=AMR", base, head],
                         cwd=ROOT, capture_output=True, text=True, check=True).stdout.split()
    urls = {u for u in (url_for(f) for f in out) if u}
    if urls:
        urls.add(f"{BASE}/")
    return sorted(urls)


def sitemap_urls() -> list[str]:
    with urllib.request.urlopen(f"{BASE}/sitemap.xml", timeout=30) as r:
        xml = r.read().decode("utf-8")
    locs = re.findall(r"<loc>([^<]+)</loc>", xml)
    out = []
    for loc in locs:                                         # follow a sitemap index if present
        if loc.endswith(".xml"):
            with urllib.request.urlopen(loc, timeout=30) as r:
                out += re.findall(r"<loc>([^<]+)</loc>", r.read().decode("utf-8"))
        else:
            out.append(loc)
    return sorted(set(out))


def submit(urls: list[str]) -> None:
    if not urls:
        print("No changed pages; nothing to submit.")
        return
    k = key()
    body = json.dumps({"host": HOST, "key": k, "keyLocation": f"{BASE}/{k}.txt",
                       "urlList": urls[:10000]}).encode("utf-8")
    req = urllib.request.Request(ENDPOINT, data=body, method="POST",
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    with urllib.request.urlopen(req, timeout=30) as r:
        print(f"IndexNow HTTP {r.status}: submitted {len(urls)} URLs")
    for u in urls:
        print("  ", u)


if __name__ == "__main__":
    if sys.argv[1:] == ["--all"]:
        submit(sitemap_urls())
    elif len(sys.argv) == 3:
        submit(changed_urls(sys.argv[1], sys.argv[2]))
    else:
        sys.exit(__doc__)

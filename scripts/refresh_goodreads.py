#!/usr/bin/env python3
"""Refresh docs/_data/books.json from the public Goodreads profile.

Goodreads no longer serves the shelf RSS feed for this account and the shelf
list needs a login, so this reads the public profile page instead:
- "favorite books" box (Goodreads fills it with the top-rated reads)
- "currently reading" box (the profile shows up to 3)

The Books page shows only English titles: it uses "english_title" when set,
else the Goodreads title. Hand-added fields (like "english_title") are kept
across refreshes, matched by Goodreads book id. The script lists any book
whose title is not in Latin script and has no "english_title" yet, so you can
add one to docs/_data/books.json.

Usage: python3 scripts/refresh_goodreads.py
"""
import html
import json
import re
import urllib.request
from pathlib import Path

USER_ID = "61566656"
PROFILE_URL = f"https://www.goodreads.com/user/show/{USER_ID}"
OUT = Path(__file__).resolve().parent.parent / "docs" / "_data" / "books.json"
BASE = "https://www.goodreads.com"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8")


def full_cover(src):
    # Drop the size suffix (._SX50_, ._SY75_) to get the full cover image.
    return re.sub(r"\._S[XY]\d+_(?=\.\w+$)", "", src)


def book_id(href):
    return re.search(r"/book/show/(\d+)", href).group(1)


def section(page, start_marker, end_marker):
    start = page.find(start_marker)
    if start < 0:
        raise SystemExit(f"Marker not found: {start_marker!r}")
    end = page.find(end_marker, start)
    return page[start:end]


def parse_favorites(page):
    box = section(page, "favorite books</a></h2>", "actionLinks")
    books = []
    for href, alt, src in re.findall(
        r'<a href="(/book/show/[^"]+)"><img alt="([^"]+)"[^>]*src="([^"]+)"', box
    ):
        title, _, author = html.unescape(alt).rpartition(" by ")
        books.append({
            "id": book_id(href),
            "title": title,
            "author": author,
            "cover": full_cover(src),
            "url": BASE + href,
        })
    return books


def parse_currently_reading(page):
    box = section(page, 'id="currentlyReadingReviews"', "bigBoxBottom")
    books = []
    for block in box.split('class="firstcol"')[1:]:
        src = re.search(r'<img[^>]*src="([^"]+)"', block).group(1)
        title = re.search(r'class="bookTitle" href="([^"]+)">([^<]+)<', block)
        author = re.search(r'class="authorName"[^>]*>([^<]+)<', block)
        books.append({
            "id": book_id(title.group(1)),
            "title": html.unescape(title.group(2)),
            "author": html.unescape(author.group(1)),
            "cover": full_cover(src),
            "url": BASE + title.group(1),
        })
    return books


def keep_manual_fields(new, old):
    by_id = {b["id"]: b for b in old}
    for book in new:
        for key, value in by_id.get(book["id"], {}).items():
            book.setdefault(key, value)
    return new


def needs_english_title(book):
    return not book.get("english_title") and re.search(r"[^\x00-\x7F\u00C0-\u024F\u2018-\u201F]", book["title"])


def main():
    page = fetch(PROFILE_URL)
    old = json.loads(OUT.read_text()) if OUT.exists() else {}
    data = {
        "profile": f"{BASE}/user/show/{USER_ID}",
        "favorites": keep_manual_fields(parse_favorites(page), old.get("favorites", [])),
        "currently_reading": keep_manual_fields(
            parse_currently_reading(page), old.get("currently_reading", [])
        ),
    }
    if not data["favorites"]:
        raise SystemExit("No favourite books parsed; Goodreads markup may have changed.")
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(f"Wrote {len(data['favorites'])} favourites and "
          f"{len(data['currently_reading'])} current reads to {OUT}")
    missing = [b for k in ("favorites", "currently_reading") for b in data[k] if needs_english_title(b)]
    for book in missing:
        print(f"Needs english_title: {book['id']} {book['title']} ({book['author']})")
    if missing:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

import datetime
import feedparser
from pathlib import Path

FEEDS = [
    "https://tldr.tech/newsletter.xml",
    "https://feeds.arstechnica.com/arstechnica/index",
    "https://www.theverge.com/rss/index.xml",
    "https://hnrss.org/frontpage",
]

OUTPUT_DIR = Path("out")
OUTPUT_DIR.mkdir(exist_ok=True)

def fetch_feed(url, max_items=10):
    parsed = feedparser.parse(url)
    entries = parsed.entries[:max_items]
    items = []
    for e in entries:
        title = getattr(e, "title", "").strip()
        link = getattr(e, "link", "").strip()
        summary = getattr(e, "summary", getattr(e, "description", "")).strip()
        items.append((title, link, summary))
    return items

def main():
    today = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    outfile = OUTPUT_DIR / f"tech-news-{today}.txt"

    lines = []
    lines.append(f"Tech News Digest – {today} (UTC)\n")
    lines.append("=" * 60 + "\n\n")

    for url in FEEDS:
        lines.append(f"Source: {url}\n")
        lines.append("-" * 60 + "\n")
        items = fetch_feed(url)
        for title, link, summary in items:
            lines.append(f"Title: {title}\n")
            lines.append(f"Link: {link}\n")
            if summary:
                lines.append(f"Summary: {summary}\n")
            lines.append("\n")
        lines.append("\n")

    outfile.write_text("".join(lines), encoding="utf-8")
    print(f"Wrote {outfile}")

if __name__ == "__main__":
    main()

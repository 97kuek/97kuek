"""Build a clickable thumbnail card grid in README.md from the portfolio RSS feed.

Each card uses the portfolio's generated OG image (/og/blog/<slug>.png) as the
thumbnail and links to the article. The grid is injected between the
BLOG-POST-LIST markers so it can be regenerated automatically.
"""

import datetime
import pathlib
import re
import urllib.request

RSS_URL = "https://97kuek.github.io/rss.xml"
OG_BASE = "https://97kuek.github.io/og/blog"
MAX_POSTS = 6
COLUMNS = 3
THUMB_WIDTH = 300
README = pathlib.Path("README.md")
START = "<!-- BLOG-POST-LIST:START -->"
END = "<!-- BLOG-POST-LIST:END -->"


def unescape(text: str) -> str:
    return (
        text.replace("&amp;", "&")
        .replace("&lt;", "<")
        .replace("&gt;", ">")
        .replace("&quot;", '"')
        .replace("&#39;", "'")
    )


def escape_html(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def fetch_items() -> list[dict]:
    req = urllib.request.Request(RSS_URL, headers={"User-Agent": "readme-bot"})
    xml = urllib.request.urlopen(req, timeout=30).read().decode("utf-8")
    items = []
    for block in re.findall(r"<item>(.*?)</item>", xml, re.S)[:MAX_POSTS]:
        title_m = re.search(r"<title>(.*?)</title>", block, re.S)
        link_m = re.search(r"<link>(.*?)</link>", block, re.S)
        date_m = re.search(r"<pubDate>(.*?)</pubDate>", block, re.S)
        if not (title_m and link_m):
            continue
        link = link_m.group(1).strip()
        slug = link.rstrip("/").split("/")[-1]
        date = ""
        if date_m:
            try:
                date = datetime.datetime.strptime(
                    date_m.group(1).strip(), "%a, %d %b %Y %H:%M:%S %Z"
                ).strftime("%Y-%m-%d")
            except ValueError:
                date = ""
        items.append(
            {
                "title": escape_html(unescape(title_m.group(1).strip())),
                "link": link,
                "thumb": f"{OG_BASE}/{slug}.png",
                "date": date,
            }
        )
    return items


def build_table(items: list[dict]) -> str:
    rows = []
    for i in range(0, len(items), COLUMNS):
        cells = []
        for it in items[i : i + COLUMNS]:
            cells.append(
                f'<td align="center" width="33%" valign="top">'
                f'<a href="{it["link"]}">'
                f'<img src="{it["thumb"]}" width="{THUMB_WIDTH}" alt="{it["title"]}" />'
                f"</a><br/>"
                f'<a href="{it["link"]}"><b>{it["title"]}</b></a><br/>'
                f'<sub>{it["date"]}</sub></td>'
            )
        rows.append("<tr>" + "".join(cells) + "</tr>")
    return "<table>\n" + "\n".join(rows) + "\n</table>"


def main() -> None:
    items = fetch_items()
    table = build_table(items)
    text = README.read_text(encoding="utf-8")
    replacement = f"{START}\n{table}\n{END}"
    new_text = re.sub(
        re.escape(START) + r".*?" + re.escape(END), replacement, text, flags=re.S
    )
    README.write_text(new_text, encoding="utf-8")
    print(f"Updated {len(items)} article cards.")


if __name__ == "__main__":
    main()

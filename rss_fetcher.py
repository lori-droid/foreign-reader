"""
RSS Fetcher Module
Fetches article titles, summaries, and links from major English publications.
Only uses publicly available RSS feed data (titles + summaries).
"""

import feedparser
import html
import re
import socket
from datetime import datetime

# Set a global socket timeout so RSS fetches don't hang
socket.setdefaulttimeout(8)


# RSS feeds from major publications (publicly accessible)
RSS_FEEDS = {
    "The Economist": {
        "feeds": [
            "https://www.economist.com/the-world-this-week/rss.xml",
            "https://www.economist.com/leaders/rss.xml",
            "https://www.economist.com/briefing/rss.xml",
            "https://www.economist.com/international/rss.xml",
            "https://www.economist.com/business/rss.xml",
            "https://www.economist.com/finance-and-economics/rss.xml",
            "https://www.economist.com/culture/rss.xml",
        ],
        "category": "politics_economics",
        "icon": "📊",
    },
    "The Atlantic": {
        "feeds": [
            "https://www.theatlantic.com/feed/all/",
            "https://www.theatlantic.com/feed/channel/politics/",
            "https://www.theatlantic.com/feed/channel/technology/",
            "https://www.theatlantic.com/feed/channel/ideas/",
        ],
        "category": "editorial",
        "icon": "🌊",
    },
    "The New Yorker": {
        "feeds": [
            "https://www.newyorker.com/feed/everything",
            "https://www.newyorker.com/feed/news",
            "https://www.newyorker.com/feed/culture",
        ],
        "category": "literature",
        "icon": "🎭",
    },
    "The Guardian - Opinion": {
        "feeds": [
            "https://www.theguardian.com/commentisfree/rss",
            "https://www.theguardian.com/world/rss",
        ],
        "category": "editorial",
        "icon": "📰",
    },
    "NPR": {
        "feeds": [
            "https://feeds.npr.org/1001/rss.xml",
        ],
        "category": "politics_economics",
        "icon": "📻",
    },
    "BBC News": {
        "feeds": [
            "http://feeds.bbci.co.uk/news/rss.xml",
            "http://feeds.bbci.co.uk/news/world/rss.xml",
        ],
        "category": "politics_economics",
        "icon": "🇬🇧",
    },
}

CATEGORY_LABELS = {
    "politics_economics": "时政经济",
    "editorial": "社论评论",
    "literature": "文学文化",
}


def clean_html(text):
    """Remove HTML tags and decode entities."""
    if not text:
        return ""
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


class RSSFetcher:
    def __init__(self):
        self.cache = {}

    def fetch_feed(self, url, source_name, category, icon):
        """Fetch and parse a single RSS feed."""
        articles = []
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:5]:  # Limit to 5 per feed
                title = clean_html(entry.get("title", ""))
                summary = clean_html(entry.get("summary", entry.get("description", "")))
                link = entry.get("link", "")
                published = entry.get("published", entry.get("updated", ""))

                if not title:
                    continue

                # Truncate summary if too long
                if len(summary) > 500:
                    summary = summary[:500] + "..."

                articles.append({
                    "title": title,
                    "summary": summary,
                    "link": link,
                    "source": source_name,
                    "source_icon": icon,
                    "category": category,
                    "category_label": CATEGORY_LABELS.get(category, category),
                    "published": published,
                    "source_type": "rss",
                    "has_full_text": False,
                })
        except Exception as e:
            print(f"  [WARN] Failed to fetch {url}: {e}")
        return articles

    def fetch_all(self):
        """Fetch articles from all configured RSS feeds."""
        all_articles = []

        for source_name, config in RSS_FEEDS.items():
            icon = config["icon"]
            category = config["category"]
            for feed_url in config["feeds"]:
                articles = self.fetch_feed(feed_url, source_name, category, icon)
                all_articles.extend(articles)

        # Deduplicate by title
        seen_titles = set()
        unique_articles = []
        for article in all_articles:
            if article["title"] not in seen_titles:
                seen_titles.add(article["title"])
                unique_articles.append(article)

        # Sort by published date (newest first), then limit
        unique_articles.sort(key=lambda x: x.get("published", ""), reverse=True)

        # Return top articles per category for variety
        result = []
        by_category = {}
        for a in unique_articles:
            cat = a["category"]
            if cat not in by_category:
                by_category[cat] = []
            by_category[cat].append(a)

        for cat, articles in by_category.items():
            result.extend(articles[:5])  # Top 5 per category

        return result[:15]  # Max 15 total

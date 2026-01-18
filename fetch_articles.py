import feedparser
import requests
from bs4 import BeautifulSoup
from rss_sources import RSS_SOURCES

def fetch_articles():
    articles = []

    for url in RSS_SOURCES:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "summary": entry.get("summary", ""),
            })

    return articles


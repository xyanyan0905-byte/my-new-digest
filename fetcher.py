import feedparser

def fetch_news(rss_feeds, max_per_source=3):
    """从RSS源抓取新闻"""
    all_news = {}
    
    for category, urls in rss_feeds.items():
        all_news[category] = []
        for url in urls:
            try:
                feed = feedparser.parse(url)
                count = 0
                for entry in feed.entries:
                    if count >= max_per_source:
                        break
                    all_news[category].append({
                        "title": entry.get("title", "无标题"),
                        "link": entry.get("link", ""),
                        "summary": entry.get("summary", "")[:500],
                        "source": feed.feed.get("title", url)
                    })
                    count += 1
                print(f"✅ 抓取成功: {url} ({count}条)")
            except Exception as e:
                print(f"❌ 抓取失败: {url} - {e}")
    
    return all_news
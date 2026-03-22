import os

# API Key
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")

# 邮件配置
EMAIL_SENDER = os.environ.get("EMAIL_SENDER", "")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD", "")
EMAIL_RECEIVER = os.environ.get("EMAIL_RECEIVER", "")

# 新闻源
RSS_FEEDS = {
    "AI工具前沿": [
        "https://feeds.feedburner.com/aidaily",
        "https://www.artificialintelligence-news.com/feed/",
        "https://venturebeat.com/category/ai/feed/",
        "https://techcrunch.com/category/artificial-intelligence/feed/",
    ],
    "Web3": [
        "https://coindesk.com/arc/outboundfeeds/rss/",
        "https://cointelegraph.com/rss",
        "https://decrypt.co/feed",
    ],
    "金融": [
        "https://feeds.reuters.com/reuters/businessNews",
    ],
    "地缘政治": [
        "https://feeds.reuters.com/Reuters/worldNews",
        "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
    ]
}

import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_SENDER = os.getenv("GMAIL_USER")
EMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("GMAIL_USER")  # 发给自己

# API Key
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")

# 邮件配置



# 新闻源
RSS_FEEDS = {
    "AI工具前沿": [
        # 原有源
        "https://feeds.feedburner.com/aidaily",
        "https://www.artificialintelligence-news.com/feed/",
        "https://venturebeat.com/category/ai/feed/",
        "https://techcrunch.com/category/artificial-intelligence/feed/",
        # 新增：官方博客
        "https://openai.com/blog/rss/",
        "https://www.anthropic.com/rss.xml",
        "https://deepmind.google/blog/rss/",
        "https://huggingface.co/blog/feed.xml",
        "https://simonwillison.net/atom/everything/",
        # 新增：Google News
        "https://news.google.com/rss/search?q=AI+LLM+large+language+model&hl=en-US&gl=US&ceid=US:en",
        "https://news.google.com/rss/search?q=OpenAI+Anthropic+Gemini+Claude&hl=en-US&gl=US&ceid=US:en",
    ],
    "Web3": [
        # 原有源
        "https://coindesk.com/arc/outboundfeeds/rss/",
        "https://cointelegraph.com/rss",
        "https://decrypt.co/feed",
        # 新增：Google News
        "https://news.google.com/rss/search?q=crypto+blockchain+Web3&hl=en-US&gl=US&ceid=US:en",
        "https://news.google.com/rss/search?q=Bitcoin+Ethereum+DeFi&hl=en-US&gl=US&ceid=US:en",
    ],
    "金融": [
        # 原有源
       
        # 新增
        "https://news.google.com/rss/search?q=financial+market+economy&hl=en-US&gl=US&ceid=US:en",
    ],
    "地缘政治": [
        # 原有源
       
        "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
        # 新增
        "https://news.google.com/rss/search?q=geopolitics+international+relations&hl=en-US&gl=US&ceid=US:en",
    ],
}
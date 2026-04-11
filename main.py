from config import RSS_FEEDS
from fetcher import fetch_news
from summarizer import summarize_news
from sender import send_email

def run():
    print("🚀 开始运行每日新闻摘要...")
    
    print("\n📡 第一步：抓取新闻...")
    news = fetch_news(RSS_FEEDS)
    
    print("\n🤖 第二步：AI总结...")
    summaries, links = summarize_news(news)
    
    print("\n📧 第三步：发送邮件...")
    send_email(summaries, links)
    
    print("\n🎉 完成！")

if __name__ == "__main__":
    run()

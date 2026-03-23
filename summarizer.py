from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def summarize_news(all_news):
    """用AI把新闻总结成中文摘要，并打重要性评分"""
    summaries = {}
    
    for category, articles in all_news.items():
        if not articles:
            continue
        
        articles_text = ""
        for i, article in enumerate(articles, 1):
            articles_text += f"{i}. 标题：{article['title']}\n"
            articles_text += f"   来源：{article['source']}\n"
            articles_text += f"   摘要：{article['summary']}\n\n"
        
        prompt = f"""你是一个专业的{category}新闻分析师。
请将以下新闻整理成中文日报摘要，并对每条新闻打重要性评分。

评分标准（1-10分）：
- 9-10分：重大突破或影响全局的事件
- 7-8分：重要进展，值得关注
- 5-6分：一般资讯
- 1-4分：低价值信息

要求：
1. 只保留评分7分及以上的新闻
2. 每条新闻格式：【评分X分】标题 + 2句话说明为什么重要
3. 最后加一句今日趋势总结

新闻内容：
{articles_text}
"""
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        
        summaries[category] = response.choices[0].message.content
        print(f"✅ AI总结完成: {category}")
    
    return summaries
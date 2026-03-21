from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def summarize_news(all_news):
    """用AI把新闻总结成中文摘要"""
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
请将以下新闻整理成一份简洁的中文日报摘要。
要求：
1. 提炼3-5个最重要的信息点
2. 每个信息点2-3句话
3. 语言简洁专业
4. 最后加一句今日趋势总结

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
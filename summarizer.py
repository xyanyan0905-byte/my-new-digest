from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def summarize_news(all_news):
    """用AI把新闻总结成中文摘要，并打重要性评分"""
    summaries = {}
    links = {}

    for category, articles in all_news.items():
        if not articles:
            continue
        links[category] = [{"title": a["title"], "link": a["link"]} for a in articles]
        
        articles_text = ""
        for i, article in enumerate(articles, 1):
            articles_text += f"{i}. 标题：{article['title']}\n"
            articles_text += f"   来源：{article['source']}\n"
            articles_text += f"   摘要：{article['summary']}\n\n"
        
        prompt = f"""你是一个专业的{category}领域新闻分析师。你必须严格按照下面的格式输出，禁止压缩内容，每条新闻必须包含完整的四个部分。

请将以下新闻整理成中文日报摘要：

评分标准（1-10分）：
- 9-10分：重大突破或影响全局的事件
- 7-8分：重要进展，值得关注
- 5-6分：一般资讯
- 1-4分：低价值信息

要求（必须严格遵守，违反任何一条均为错误输出）：
1. 只保留评分7分及以上的新闻
2. 每条新闻必须按以下格式输出，每条不少于300字，禁止压缩：

【评分x分】新闻标题 [编号]

📌 背景（不少于60字）：这件事发生在什么背景下，涉及哪些人物、机构或行业趋势

📢 事件（不少于100字）：具体发生了什么，核心内容、关键数据、重要细节是什么

💥 影响（不少于80字）：对哪些人群、行业或市场有影响，短期和长期影响分别是什么

🔮 预判（不少于60字）：接下来可能会怎样发展，普通人或投资者需要注意什么

3. 编号和"新闻内容"里的序号一致，第1条新闻标 [1]，第3条标 [3]
4. 每条新闻之间用分隔线 --- 隔开
5. 最后加一句今日趋势总结

新闻内容：
{articles_text}
"""
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        
        summaries[category] = response.choices[0].message.content
        print(f"✅ AI总结完成: {category}")
    
        # 同时保存每个分类的文章链接
        
    
    return summaries, links
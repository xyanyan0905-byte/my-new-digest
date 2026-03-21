import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from config import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER

def build_email_html(summaries):
    """生成好看的HTML邮件"""
    today = datetime.now().strftime("%Y年%m月%d日")
    
    html = f"""
    <html><body style="font-family:Arial,sans-serif;max-width:700px;margin:auto;padding:20px">
    <h1 style="color:#1a1a2e;border-bottom:3px solid #e94560;padding-bottom:10px">
        📰 每日新闻摘要 · {today}
    </h1>
    """
    
    icons = {"AI工具前沿": "🤖", "Web3": "🔗", "金融": "💰", "地缘政治": "🌍"}
    colors = {"AI工具前沿": "#e94560", "Web3": "#6c63ff", "金融": "#00b894", "地缘政治": "#e17055"}
    
    for category, summary in summaries.items():
        icon = icons.get(category, "📌")
        color = colors.get(category, "#333")
        summary_html = summary.replace('\n', '<br>')
        
        html += f"""
        <div style="margin:20px 0;padding:20px;border-left:4px solid {color};background:#f9f9f9;border-radius:0 8px 8px 0">
            <h2 style="color:{color};margin-top:0">{icon} {category}</h2>
            <p style="line-height:1.8;color:#333">{summary_html}</p>
        </div>
        """
    
    html += """
    <p style="color:#999;font-size:12px;text-align:center;margin-top:30px">
        由你的 AI 新闻助手自动生成 · 每日早8点更新
    </p>
    </body></html>
    """
    return html

def send_email(summaries):
    """发送邮件"""
    msg = MIMEMultipart('alternative')
    today = datetime.now().strftime("%Y/%m/%d")
    msg['Subject'] = f"📰 每日新闻摘要 {today} | AI · Web3 · 金融 · 地缘政治"
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    
    html_content = build_email_html(summaries)
    msg.attach(MIMEText(html_content, 'html'))
    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        print("✅ 邮件发送成功！")
    except Exception as e:
        print(f"❌ 邮件发送失败: {e}")
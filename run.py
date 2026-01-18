from fetch_articles import fetch_articles
from summarize import summarize
from send_email import send_email
from utils import format_digest

def run():
    articles = fetch_articles()
    digest_items = []

    for art in articles[:10]:  # limit na start
        summary = summarize(art["summary"])
        digest_items.append({
            "title": art["title"],
            "summary": summary
        })

    email_body = format_digest(digest_items)
    send_email(email_body)

if __name__ == "__main__":
    run()


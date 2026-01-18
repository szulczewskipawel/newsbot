import smtplib
import os
from email.mime.text import MIMEText

def send_email(body):
    sender = "my_email@gmail.com"
    password = "my_secret_password"
    recipient = "recipient@whatever.com"

    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = "News Digest"
    msg["From"] = sender
    msg["To"] = recipient

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, recipient, msg.as_string())


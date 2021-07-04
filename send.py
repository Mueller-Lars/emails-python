import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


def send_email(data):
    email_add = data["email"]
    subject = data["subject"]
    message = data["message"]

    email = EmailMessage()  # email object
    email['from'] = (f"{email_add}")
    email['to'] = "<destination email>"
    email['subject'] = (f"{subject}")
    email.set_content(
        f"This message was sent by {email_add}:\n \n {message}")
    # log into gmail and send email
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()  # encryption mechanism
        smtp.login('<email address>', '<password>')  # log into your email
        smtp.send_message(email)
    print('Email has been sent')

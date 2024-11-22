
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os

def Sendresetpasswordlinkapi(site_url,receiver_email, token):
    msg = MIMEMultipart()
    msg['To'] = receiver_email
    msg['Subject'] = "Password Reset Email."

    message = f"{site_url}/reset-password/?email={receiver_email}&token={token}"
    msg.attach(MIMEText(message, 'plain'))
    try:
        server = smtplib.SMTP(os.getenv("NEW_EMAIL_HOST"), os.getenv("EMAIL_PORT"))
        server.starttls()
        server.login(os.getenv("NEW_EMAIL_HOST_USER"), os.getenv("NEW_EMAIL_HOST_PASSWORD"))
        server.sendmail(os.getenv("NEW_EMAIL_HOST_USER"), receiver_email, msg.as_string())
        print('Email sent successfully!')

    except Exception as e:
        print(f'Error sending email: {e}')

    finally:
        server.quit()
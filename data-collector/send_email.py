from email.mime.text import MIMEText
import smtplib


def send_email(email, height):
    from_email = "your@emailprovider.com"
    from_password = "password"
    to_email = email

    subject = "Height Data"
    message = "Hey there, you height data is {}".format(height)

    msg = MIMEText(message, "html")
    msg["Subject"] = subject
    msg["To"] = to_email
    msg["From"] = from_email

    server = smtplib.SMTP_SSL("smtp.server.com", 465)
    server.ehlo()
    server.starttls()
    server.login(from_email, from_password)
    server.send_message(msg)

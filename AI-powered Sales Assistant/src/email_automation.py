import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailAutomation:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def generate_email(self, recipient: str, subject: str, body: str) -> MIMEMultipart:
        message = MIMEMultipart()
        message["From"] = self.email
        message["To"] = recipient
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        return message

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        message = self.generate_email(recipient, subject, body)
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(self.email, self.password)
            server.send_message(message)

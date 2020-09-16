import pyinputplus as pyip
from validate_email import validate_email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from string import Template
from pathlib import Path
from getpass import getpass
import smtplib


# Html template object
template = Template(Path("template.htm").read_text())
# template.substitute()


email_info = "Please Enter Your Information"
print(email_info)
from_who = input("From: ")
email_to = pyip.inputEmail("To: ")
# email_to = input("To ")
# validate_email(
#     email_to,
#     check_regex=True,
#     check_mx=True,
#     smtp_timeout=10,
#     dns_timeout=10,
#     use_blacklist=True,
#     debug=False,
# )


message_text = "Please type Your Email and Password To sent Email"
print(message_text)
email = input("Email: ")
password = getpass("Type Your Password: ")


# print(f"{email}, {password}")

message = MIMEMultipart()
message["from"] = from_who
message["to"] = email_to
message["subject"] = "THis is a testing email"
body = template.substitute(name="Said")
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("saidshah.jpeg").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email, password)
    smtp.send_message(message)
    print("Sent...")

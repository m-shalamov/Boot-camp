import os
import smtplib
import imghdr
from email.message import EmailMessage


# 1
EMAIL_ADDRESS = os.environ.get("email")
EMAIL_PASSWORD = os.environ.get("email_pass")
email_to = "schumixer@list.ru"

# with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
# with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
#     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#     subject = "It is the subject"
#     body = "How are you, dear?"

#     message = f"{subject}\n\n{body}"

#     smtp.sendmail(from_addr=EMAIL_ADDRESS, to_addrs=EMAIL_ADDRESS, msg=message)
# 2
contacts = ["YourAddress@gmail.com", "test@example.com"]

msg = EmailMessage()
msg["Subject"] = "Check out Bronx as a puppy!"
msg["From"] = EMAIL_ADDRESS
msg["To"] = EMAIL_ADDRESS
# msg["To"] = "a, b"
msg.set_content("This is a plain text email")

with open(r"API/data/file.png", "rb") as image:
    file_data = image.read()
    file_type = imghdr.what(image.name)
    file_name = image.name
msg.add_attachment(file_data, maintype = 'image', subtype = file_type, filename = file_name)


with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
#Practice
#Send many images
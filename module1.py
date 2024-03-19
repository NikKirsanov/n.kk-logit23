import smtplib
import ssl
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

smtp_server = "smtp.gmail.com"
port = 587
sender_email = "nik.kirsanov17@gmail.com"
password = input("Kirjuta oma salasõna ja vajuta enter: ")
context = ssl.create_default_context()

msg = MIMEMultipart()
msg["Subject"] = "Kirja teema"
msg["From"] = "Nikita"
msg["To"] = "nik.kirsanov17@gmail.com"

text = "Tere tulemast! olen kirja keha!"
msg.attach(MIMEText(text, "plain"))

with open("eldar.jpg", "rb") as fp:
    img_data = fp.read()
    img = MIMEImage(img_data, name="eldar.jpg")
    msg.attach(img)

try:
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.send_message(msg)
    print("Email with embedded image sent successfully.")
except Exception as e:
    print(e)
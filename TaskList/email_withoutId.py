import smtplib
from email.mime.text import MIMEText

msg = MIMEText("Hello, this is anonymous.")
msg["Subject"] = "Anonymous Test"
msg["From"] = "pratibhasoni757@gmail.com"
msg["To"] = "artescapissm.com"

with smtplib.SMTP("smtp.sendgrid.net", 587) as server:
    server.login("apikey", "YOUR_SENDGRID_API_KEY")
    server.send_message(msg)

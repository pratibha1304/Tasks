import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Sender and Receiver Info
sender_email = "pratibhasoni757@gmail.com"
receiver_email = "artescapissm@gmail.com"
app_password = "jvyx xjvz sbsi zzjb"

# Email content
subject = "Hello from Python!"
body = "This is a test email sent using Python and Gmail SMTP."

# Create the email message
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject

msg.attach(MIMEText(body, "plain"))

# Send the email
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(msg)
        print("✅ Email sent successfully!")
except Exception as e:
    print("❌ Failed to send email:", e)

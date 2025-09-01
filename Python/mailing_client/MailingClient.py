import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Gmail SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
# Read password from file
with open("mailing_client/password.txt", "r") as f:
    password = f.read().strip()
print(repr(password))
print(f"DEBUG: Password length = {len(password)}")


# Login to Gmail (use App Password, not normal password)
server.login("senderemail@gmail.com", password)

# Create email
msg = MIMEMultipart()
msg["From"] = "senderemail@gmail.com" # type the sender's email address
msg["To"] = "testmails@spaml.de"
msg["Subject"] = "Just a Test"

# Read message from file
with open("mailing_client/message.txt", "r") as f:
    body = f.read()

msg.attach(MIMEText(body, "plain"))

# Attach file (example: image.png)
filename = "mailing_client/image.png"
with open(filename, "rb") as attachment:
    p = MIMEBase("application", "octet-stream")
    p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header("Content-Disposition", f"attachment; filename={filename}")
msg.attach(p)

# Send email
server.sendmail("senderemail@gmail.com", "testmails@spaml.de", msg.as_string())
server.quit()


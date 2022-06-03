import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create a SMTP object
server = smtplib.SMTP('smtp.gmail.com', 587)

# Start the SMTP server
server.ehlo()

# Login to the SMTP server
server.login('username@gmail.com', 'password')

# Create a message
message = MIMEMultipart()
message['From'] = 'User Name'
message['To'] = 'anotheruser@gmail.com'
message['Subject'] = 'Test Email'

# Add the body of the message
message.attach(MIMEText('This is a test email.', 'plain'))

# Attach a file
filename = '3dblue.png'
attachment = open(filename, 'rb')

# Create a MIMEBase object (Payload)
payload = MIMEBase('application', 'octet-stream')
payload.set_payload(attachment.read())

# Encode the payload
encoders.encode_base64(payload)
payload.add_header('Content-Disposition', f'attachment; filename={filename}')

# Add the payload to the message
message.attach(payload)

# Send the message
text = message.as_string()
server.sendmail('username@gmail.com', 'anotheruser@gmail.com', text)

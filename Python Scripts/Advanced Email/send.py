from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from smtplib import SMTP

import markdown

from settings import (HOST, PORT, SENDER,DISPLAY_NAME,PASSWORD, RECIPIENT, MESSAGE_FILE)

with open(MESSAGE_FILE) as file:
    message = file.read()


    server = SMTP('smtp.gmail.com',587)
    server.connect('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('sumanttulshibagwale@gmail.com','PasoXobaGozi3[')
    

    multipart_msg = MIMEMultipart("alternative")
    multipart_msg["Subject"] = message.splitlines(0)
    multipart_msg["From"] = DISPLAY_NAME + f'<sumanttulshibagwale@gmail.com>'
    multipart_msg["To"] = 'prernagpt131@gmail.com'

    text = message
    html = markdown.markdown(text)

    part1 = MIMEText(text,"plain")
    part2 = MIMEText(html,"html")

    multipart_msg.attach(part1)
    multipart_msg.attach(part2)

    server.sendmail(SENDER, RECIPIENT, multipart_msg.as_string())

    print("Sent email successfully")
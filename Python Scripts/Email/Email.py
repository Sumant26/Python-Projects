from smtplib import SMTP


# Email Infomartion of the sender 
SENDER = 'sumanttulshibagwale@gmail.com'

PASSWORD = 'PasoXobaGozi3['

# Creates an object of the smtp server
server = SMTP('smtp.gmail.com', 587)

# Connexts to the smtp server using the object
server.connect('smtp.gmail.com', 587)

# Extended Hello
server.ehlo()


server.starttls()
server.ehlo()

# Logs in using the Sender's meail information
server.login(user=SENDER, password=PASSWORD)

# Email Information of the receiver
RECIPIENT = ['prernagpt131@gmail.com','prerna@dentaldost.com']

MESSAGE = 'Hello, Prerna!'

# Sends the email to the receiver
server.sendmail(SENDER,RECIPIENT,MESSAGE,)
import smtplib
from getpass import getpass
server = smtplib.SMTP("smtp.gmail.com",587)
server.ehlo()
server.starttls()
username = 'christoncardoza33@gmail.com'
password = getpass()
server.login(username,password)
#msg = "Hi Man, Welcome to SMTP"
#server.sendmail(username,username,msg)
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
msg = MIMEMultipart()
msg['From'] = username
msg['To'] = username
msg['Subject'] = "Testing SMTP Connection"
text = 'Connection Successful. PFA'
msg.attach(MIMEText(text))
with open(r"C:\Users\Christon\Desktop\Untitled.png",'rb') as f:
    part = MIMEApplication(f.read())
    part.add_header('Content-Disposition', 'attachment', filename='mypic.png')
    msg.attach(part)
server.sendmail(msg['From'],msg['To'],msg.as_string())

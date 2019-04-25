import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from getpass import getpass
server = smtplib.SMTP("smtp.gmail.com",587)
server.ehlo()
server.starttls()
username= "christoncardoza33@gmail.com.com"
password = getpass()
server.login(username,password)
#msg = "Hi"
# server.sendmail(username,username, msg)
msg = MIMEMultipart()
msg['From'] = username
msg['To'] = 'christoncardoza96@gmail.com'
msg['Subject'] = 'logo'
text = 'check out the logo!'
msg.attach(MIMEText(text))
with open('logo.png','rb')as f: 
    part = MIMEApplication(f.read())
    part.add_header('Content-Disposition','attachment',filename="logo.png")
    msg.attach(part)
server.sendmail(msg['From'],msg['To'],msg.as_string())
     
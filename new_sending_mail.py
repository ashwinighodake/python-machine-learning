from email import message
import smtplib
from email.message import EmailMessage

msg=EmailMessage()
msg.set_content(input("Enter message here:"))
sender_mail=input("Enter sender mail-id:")
msg['Subject']=input("Enter subject:")
msg['From']=sender_mail
msg['To']=input("Enter receiver email id:")
password=input("Enter your gmail password:")


server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login(sender_mail,password)
server.send_message(msg)
server.quit()
import os
from email.message import EmailMessage
import ssl
import smtplib
email_sender='emailtesting1113@gmail.com'
email_password='lirk eevk tram iif'
email_reciever='anshikatripathi133@gmail.com'
subject='Hi there'
body="Welcome to this program"
em=EmailMessage()
em['From']=email_sender
em['To']=email_reciever
em['Subject']=subject
em.set_content(body)
context=ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.googlemail.com',465,context=context)as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_reciever,em.as_string())



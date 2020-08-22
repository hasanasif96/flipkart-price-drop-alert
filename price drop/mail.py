# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 15:35:14 2020

@author: Hasan
"""


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mails(email,name,url):
    email_password = 'Mrlonely@56'
    email_user = 'sahab.qwwnd@gmail.com'
    subject = 'alert'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email
    msg['Subject'] = subject

    body = f'Hi {name}. This mail is to inform you that your desired price is reached in flipkart.{url}'
    msg.attach(MIMEText(body,'plain'))

    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)


    server.sendmail(email_user,email,text)
    server.quit()
    
    
    
def send_price_low_mail(email,name):
    email_password = 'Mrlonely@56'
    email_user = 'sahab.qwwnd@gmail.com'
    subject = 'Price drop Alert'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email
    msg['Subject'] = subject

    body = f'Hi {name}. This mail is to inform you that your desired price is not reached but there is a drop in price.plz have a look.'
    msg.attach(MIMEText(body,'plain'))

    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)


    server.sendmail(email_user,email,text)
    server.quit()
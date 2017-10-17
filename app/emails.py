# -*- coding: utf-8 -*-
from flask_mail import Message
from app import app,mail
from flask import render_template
from config import ADMINS
from threading import Thread
from .decorators import async

@async
def async_send_email(app,msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender = sender, recipients = recipients)
    msg.body = text_body
    msg.html = html_body
    async_send_email(app, msg)


def follower_notification(followed, follower):
    send_email("[microblog] %s is now following you!" % follower.nickname,
        ADMINS[0],
        [followed.email],
        render_template("follower_email.txt",
            user = followed, follower = follower),
        render_template("follower_email.html",
            user = followed, follower = follower))





'''
def send_email(subject, sender, recipients, cc):
    msg = Message(subject, sender = sender, recipients = recipients,cc=cc)
    msg.body = 
#JAM,
#The password for your account has just been reset. 
#If you did not perform a password reset, please contact our support team here: https://www.twilio.com/help/contact?utm_source=console&utm_medium=email&utm_content=user&utm_campaign=consolegenemails
#- Team Twilio
    
    with app.open_resource('C:\\Users\\wang\\Desktop\\microblog\\tmp\\pic.jpg') as f:
    	msg.attach('pic.jpg','image/jpg',f.read())
    mail.send(msg)

if __name__ == '__main__':
	with app.app_context():
		send_email('toi best wishes~', ('Jam','wjian2580@163.com'),['501260495@qq.com'] ,  ['1505702756@qq.com','wangjian0414@rayootech.com'])
'''
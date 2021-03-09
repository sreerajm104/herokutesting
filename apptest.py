# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 20:44:41 2021

@author: sree
"""
from flask import Flask,  render_template,request
#import smtplib
from flask_mail import Mail, Message

apptest = Flask(__name__)

mail= Mail(apptest)

apptest.config['MAIL_SERVER']='smtp.gmail.com'
apptest.config['MAIL_PORT'] = 465
apptest.config['MAIL_USERNAME'] = 'code2deploy@gmail.com'
apptest.config['MAIL_PASSWORD'] = 'Admin@123'
apptest.config['MAIL_USE_TLS'] = False
apptest.config['MAIL_USE_SSL'] = True
mail = Mail(apptest)

@apptest.route('/')
def home():
    return render_template('index.html')
    # return "Appian Call Success"

@apptest.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    topic = [x for x in request.form.values()]
    output = topic[0]      
    return render_template('index.html', prediction_text=output)

@apptest.route('/appiancall')
def appiancall():
    # return render_template('index.html')
    email = 'processmodeluuido0001e604-162a-8000-49c6-7f0000014e7a@kpmgdemo.appiancloud.com'
    # email = "processmodeluuido002e604-15f2-8000-49c2-7f0000014e7a@kpmgdemo.appiancloud.com"
    # email = "sreeraj.m04@gmail.com"
#    message = "This is a reply to appian"
#    server = smtplib.SMTP("smtp.gmail.com",587)
#    server.starttls()
#    server.login("code2deploy@gmail.com","Admin@123")
#    server.sendmail("code2deploy@gmail.com",email,message)
    
    msg = Message('Hello', sender = 'code2deploy@gmail.com', recipients = [email])
    msg.body = "This is a return call to Appian"
    mail.send(msg)
    
    
    return "Appian APIs Call Success"

if __name__ == "__main__":
    apptest.run(debug=True)

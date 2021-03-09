# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 20:44:41 2021

@author: sree
"""
from flask import Flask,  render_template,request
import smtplib

apptest = Flask(__name__)


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
    email = "processmodeluuido002e604-15f2-8000-49c2-7f0000014e7a@kpmgdemo.appiancloud.com"
    message = "This is a reply to appian"
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("code2deploy@gmail.com","Admin@123")
    server.sendmail("code2deploy@gmail.com",email,message)
    return "Appian Call Success"

if __name__ == "__main__":
    apptest.run(debug=True)

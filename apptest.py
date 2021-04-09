# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 20:44:41 2021

@author: sree
"""
from flask import Flask,  render_template,request, jsonify, send_file
#import smtplib
# from flask_mail import Mail, Message
import requests
# import json
import cv2
import numpy as np
# from PIL import Image
# import base64
# import io

apptest = Flask(__name__)

addr = 'http://localhost:5000'
test_url = addr + '/detectface'
content_type = 'image/jpeg'
headers = {'content-type': content_type}
# mail= Mail(apptest)

# apptest.config['MAIL_SERVER']='smtp.gmail.com'
# apptest.config['MAIL_PORT'] = 465
# apptest.config['MAIL_USERNAME'] = 'code2deploy@gmail.com'
# apptest.config['MAIL_PASSWORD'] = 'Admin@123'
# apptest.config['MAIL_USE_TLS'] = False
# apptest.config['MAIL_USE_SSL'] = True
# mail = Mail(apptest)

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
    # email = 'processmodeluuido0001e604-162a-8000-49c6-7f0000014e7a@kpmgdemo.appiancloud.com'
    # email = "processmodeluuido002e604-15f2-8000-49c2-7f0000014e7a@kpmgdemo.appiancloud.com"
    # email = "sreeraj.m04@gmail.com"
#    message = "This is a reply to appian"
#    server = smtplib.SMTP("smtp.gmail.com",587)
#    server.starttls()
#    server.login("code2deploy@gmail.com","Admin@123")
#    server.sendmail("code2deploy@gmail.com",email,message)
    
    # msg = Message('Hello', sender = 'code2deploy@gmail.com', recipients = [email])
    # msg.body = "This is a return call to Appian"
    # mail.send(msg)
    
    
    return "Appian APIs Call Success"

@apptest.route('/generatefile',methods=['POST'])
def generatefromfile():
    '''
    For rendering results on HTML GUI
    '''
    try: 
        file = request.files['file']
        file.save(file.filename)    
        with open(file.filename,'r') as f:    
            str_text = f.read()
        output = str_text
        return output
        
    except requests.exceptions.RequestException as e:
        # app.logger.error(f"Error encountered in GenerateFile: {e}")
        return "Error"

@apptest.route('/detectface',methods=['POST'])
def detectface():
    '''
    For rendering results on HTML GUI
    '''
    face_classifier = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")

    file = request.files['image'].read() ## byte file
    npimg = np.fromstring(file, np.uint8)
    
    
    # decode image
    image = cv2.imdecode(npimg, 1)
    

    grayimg = cv2.imdecode(npimg, cv2.COLOR_RGB2GRAY)
    
        
    faces = face_classifier.detectMultiScale(grayimg,1.3,5)
    if faces != ():
        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),color=(0, 255, 0), thickness=3)
        
        image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
        cv2.imwrite("Return.jpg",image)
        # response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
        return send_file("Return.jpg", mimetype='image/gif',as_attachment=True)
        # finimg = Image.fromarray(image.astype("uint8"))
        # rawBytes = io.BytesIO()
        # finimg.save(rawBytes, "JPEG")
        # rawBytes.seek(0)
        # img_base64 = base64.b64encode(rawBytes.read())
        # return jsonify({'status':str(img_base64)})
    else:
        return jsonify({'status':"None"})
   
        

if __name__ == "__main__":
    apptest.run(debug=True)

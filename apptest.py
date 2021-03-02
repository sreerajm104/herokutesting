# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 20:44:41 2021

@author: sree
"""
from flask import Flask,  render_template


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
    return "Appian Call Success"

if __name__ == "__main__":
    apptest.run(debug=True)

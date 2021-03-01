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

@apptest.route('/appiancall')
def appiancall():
    # return render_template('index.html')
    return "Appian Call Success"

if __name__ == "__main__":
    apptest.run(debug=True)

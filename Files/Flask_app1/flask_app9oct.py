# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 17:17:44 2023

@author: harsh
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Harshman!"

@app.route('/harsh')
def hello_world():
    return "Hello Harshman Sharma!"

if__name__='__main__'
app.run()
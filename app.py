# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 15:21:21 2021

@author: AD20066041
"""

from flask import Flask

UPLOAD_FOLDER = 'C:/uploads'

app = Flask(__name__)
#app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

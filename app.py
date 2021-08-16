# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 15:33:38 2021

@author: AD20066041
"""


from main import app
from flask import  request, jsonify

ALLOWED_EXTENSIONS = set(['pdf', 'jpg', 'tif'])
#model= joblib.load(open("model.pkl", "rb"))

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def test():
    return {'message': 'Hello World!'}

@app.route('/test', methods=['GET'])
def test1():
    return {'hello': 'world'}


if __name__ == "__main__":
    app.run()

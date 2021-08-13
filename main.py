# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 15:33:38 2021

@author: AD20066041
"""

import os
import numpy as np
import joblib
from app import app
from flask import  request, jsonify
from werkzeug.utils import secure_filename
import Cad_Pdf_Match as Cad_Pdf_Match

ALLOWED_EXTENSIONS = set(['pdf', 'jpg', 'tif'])
model= joblib.load(open("model.pkl", "rb"))

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/test', methods=['GET'])
def test():
    return {'hello': 'world'}

@app.route("/predict", methods=["POST"])
def predict():
#specifying our parameters as data type float
    int_features= [float(x) for x in request.form.values()]
    final_features= [np.array(int_features)]
    prediction= model.predict(final_features)
    output= round(prediction[0], 2)
    resp = jsonify({'flower' : str(output) })
    return resp


@app.route('/cad-pdf-match', methods=['POST'])
def upload_file():
    
    # check if the post request has the file part
    if 'file1' and 'file2' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp
    
    file1 = request.files['file1']
    file2 = request.files['file2']
    
    
    if file1.filename == '' or file2.filename == '':
        resp = jsonify({'message' : 'No file selected for uploading'})
        resp.status_code = 400
        return resp
    
    if file1 and allowed_file(file1.filename) and file2 and allowed_file(file2.filename):
        print("I'm here")
        filename1 = secure_filename(file1.filename)
        filename2 = secure_filename(file2.filename)
        path1 = os.path.join(app.config['UPLOAD_FOLDER'], filename1)
        path2 = os.path.join(app.config['UPLOAD_FOLDER'], filename2)
        file1.save(path1)
        file2.save(path2)
        # Logic comes here
        match, score = Cad_Pdf_Match.read_imgs(path1, path2)
        
        resp = jsonify({'Match' : match, 'Score': score})
        resp.status_code = 201
        return resp
    
    else:
        resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
        resp.status_code = 400
        return resp

if __name__ == "__main__":
    app.run()

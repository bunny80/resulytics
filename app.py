# -*- coding: utf-8 -*-
"""
Created on Sun May 23 20:57:39 2021

@author: saiak
"""
from flask import Flask,request,render_template

import pickle
import numpy as np
app= Flask(__name__)
regressor=pickle.load(open('realestate.pkl','rb'))
@app.route('/')
def home():
    """Renders the home page."""
    return render_template('sign.html')
@app.route('/predict',methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = regressor.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('sign.html', prediction_text='Price of land is approximately $ {}'.format(output))

    """
    CRIM=int(request.form['CRIM'])
    ZN=int(request.form['ZN'])
    INDUS=int(request.form['INDUS'])
    CHAS=int(request.form['CHAS'])
    NOX=int(request.form['NOX'])
    RM=int(request.form['RM'])
    AGE=int(request.form['AGE'])
    DIS=int(request.form['DIS'])
    TAX=int(request.form['TAX'])
    PTRATIO=int(request.form['PTRATIO'])
    B=int(request.form['B'])
    LSTAT=int(request.form['LSTAT'])
    data=[[CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,TAX,PTRATIO,B,LSTAT]]
    if(CRIM==0 and ZN==0 and INDUS==0 and CHAS==0 and NOX==0 and RM==0 and AGE==0 and DIS==0 and TAX==0 and PTRATIO==0 and B==0 and LSTAT==0):
        my_prediction=[0]
    else:
        my_prediction=regressor.predict(data)
        return render_template('sign.html',prediction=my_prediction)

 """
       
if __name__=="__main__":
    app.run(debug=True)

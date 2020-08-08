# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 17:16:42 2020

@author: Himanshu
"""

from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('graph.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    prediction = list(dict(sorted(dict(model[request.form['Tag']]).items(),
                                  key = lambda x: x[1]['weight'], reverse = True)).keys())
    return render_template('index.html', prediction_text=str(prediction))


if __name__ == "__main__":
    app.run(debug=True)
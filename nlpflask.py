# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 11:49:02 2020

@author: ELCOT
"""

from flask import render_template, Flask, request,url_for,redirect
from keras.models import load_model
import pickle 
import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
graph = tf.get_default_graph()
cla = load_model('nlp.h5')
cla.compile(optimizer='adam',loss='categorical_crossentropy')
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict', methods = ['GET','POST'])
def page2():
    if request.method == 'POST':
        topic = request.form['TITLE']
        print("\n"+str(topic.shape)+"\n")
        with graph.as_default():
            y_pred = cla.predict_class(topic)
            print("pred is "+str(y_pred))
        index = ["Buisness","Entertainment","Health","Science and Technology"]
        text="The Given Headline is : "+index[y_pred]
        return text

if __name__ == '__main__':
    app.run(host = 'localhost', debug = True , threaded = False)
    

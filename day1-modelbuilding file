# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 15:44:19 2020

@author: ELCOT
"""


import numpy as np
import pandas as pd
dataset = pd.read_csv(r"C:\Users\ELCOT\Downloads\294_644_compressed_uci-news-aggregator.csv\uci-news-aggregator.csv")
dataset.head()
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
dataset['CATEGORY']=le.fit_transform(dataset['CATEGORY'])
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
data = []
for i in range(0,5500):
    review = dataset['TITLE'][i]
    review  = re.sub('[^a-zA-z]',' ',str(review))
    review = review.lower()
    review = review.split()
    review  = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    data.append(review)
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 10000)
x = cv.fit_transform(data).toarray()
y=dataset.iloc[:5500,4:5].values
x.shape
from sklearn.preprocessing import OneHotEncoder
one=OneHotEncoder()
z=one.fit_transform(y[:,0:1]).toarray()
y=np.delete(y,0,axis=1)
y=np.concatenate((z,y),axis=1)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test =train_test_split(x,y,test_size = 0.2,random_state = 0)
from keras.models import Sequential
from keras.layers import Dense
model = Sequential()
model.add(Dense(units = 4194,init = 'uniform',activation = 'relu'))
model.add(Dense(units = 16000,init = 'uniform',activation = 'relu'))
model.add(Dense(units = 4,init = 'uniform',activation = 'softmax'))
model.compile(optimizer = 'adam', loss = "categorical_crossentropy",metrics = ['accuracy'])
model.fit(x_train,y_train,epochs = 5,batch_size = 64)
model.save("nlp.h5")


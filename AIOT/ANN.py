# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 23:59:41 2019
@author: darshana
"""
# first neural network with keras tutorial
import sys
import numpy as np
import sklearn
from numpy import loadtxt
from sys import *
sys.path.insert(0,'/home/g8w4y/.local/bin')
import tensorflow
from tensorflow import keras
from keras import *
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
# load the dataset
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')
np.random.shuffle(dataset)
X = dataset[:,0:len(dataset[0])-1]
y = dataset[:,len(dataset[0])-1:len(dataset[0])]
# split into input (X) and output (y) variables
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
# define the keras model
model = Sequential()
model.add(Dense(10, input_dim=8, activation='relu'))
model.add(Dense(5, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='SGD', metrics=['accuracy'])
#binary_crossentropy refer following link
#https://towardsdatascience.com/understanding-binary-cross-entropy-log-loss-a-
visual-explanation-a3ac6025181a 
# fit the keras model on the dataset
model.fit(X_train, y_train, epochs=150, batch_size=20)
# evaluate the keras model
a, trainingAccuracy = model.evaluate(X_train, y_train)
b, testingAccuracy = model.evaluate(X_test, y_test)
print('Training accuracy: %.2f' % (trainingAccuracy*100))
print('Testing accuracy: %.2f' % (testingAccuracy*100))
predictions = model.predict_classes(X_test)
# summarize the first 5 cases
#for i in range(5):
# print('%s => %d (expected %d)' % (X_test[i].tolist(), predictions[i], 
#y_test[i]))
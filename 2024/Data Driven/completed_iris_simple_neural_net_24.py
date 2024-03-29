# -*- coding: utf-8 -*-
"""Completed Iris Simple Neural Net 24.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z4ErUA7RsTGTjUMMO6pliJrJHwBeHJN8
"""

from sklearn.datasets import load_iris

iris_data = load_iris()

print(iris_data['DESCR'])

iris_data['data'].shape

iris_data['target'].shape

iris_data['target']

from keras.models import Sequential
from keras.layers import Dense

model = Sequential()

model.add(Dense(8,activation='relu',input_shape = (None,4)))
model.add(Dense(6, activation='relu'))
model.add(Dense(3, activation='softmax'))

model.compile(loss = 'categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.summary()

from tensorflow.keras.utils import to_categorical

X = iris_data['data']
Y = iris_data['target']
Y_c = to_categorical(Y)

history = model.fit(X,Y_c,epochs=500)

from matplotlib import pyplot as py

py.plot(history.history['loss'])
py.plot(history.history['accuracy'])

from sklearn.model_selection import train_test_split

help(train_test_split)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y_c,test_size=  0.3)

model = Sequential()

model.add(Dense(8,activation='relu',input_shape = (None,4)))
model.add(Dense(6, activation='relu'))
model.add(Dense(3, activation='softmax'))

model.compile(loss = 'categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
hist2 = model.fit(X_train,Y_train, validation_data=(X_test,Y_test) , epochs=400)

py.plot(hist2.history['loss'])
py.plot(hist2.history['val_loss'])

help(model.predict)

Y_pred = model.predict(X_test,)

Y_pred

Y_test

from sklearn.metrics import confusion_matrix

import numpy as np

confusion_matrix( np.argmax(Y_pred, axis = 1), np.argmax(Y_test, axis = 1))

Y_train_Pred = model.predict(X_train)

confusion_matrix( np.argmax(Y_train_Pred, axis = 1), np.argmax(Y_train, axis = 1))
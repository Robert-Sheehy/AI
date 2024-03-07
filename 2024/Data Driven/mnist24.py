# -*- coding: utf-8 -*-
"""Mnist24.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HCk-YKo8H7ztBZuyakHbUysWsa8vXd1y
"""

from keras.datasets import mnist

help(mnist.load_data)

(x_train, y_train), (x_test, y_test) = mnist.load_data()

import matplotlib.pyplot as plt

x_train.shape

plt.imshow(x_train[3])

y_train[3]

import numpy as np
x_train_flat = np.reshape(x_train,(60000, 28*28))

x_train_flat.shape

from keras.layers import Dense, Convolution2D, MaxPool2D, Flatten
from keras.models import Sequential

x_train.shape

x_train_28_28_1 = np.reshape(x_train, (60000,28,28,1))

x_train_28_28_1.shape

from tensorflow.keras.utils import to_categorical
Y_train_cat = to_categorical(y_train)

Y_train_cat.shape

x_test_28_28_1 = np.reshape(x_test,(x_test.shape[0],28,28,1))

model = Sequential()
model.add(Convolution2D(32, (3,3), activation='relu', input_shape = (28,28,1)))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(128,activation='relu'))
model.add(Dense(10, activation='softmax'))

model.compile(loss = 'categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

hist = model.fit(x_train_28_28_1,Y_train_cat, epochs= 10)

y_test_cat = to_categorical(y_test)

y_pred = model.predict(x_test_28_28_1)

y_pred[4]

y_test[4]

from sklearn.metrics import confusion_matrix

confusion_matrix( np.argmax(y_pred, axis = 1), np.argmax(y_test_cat, axis = 1))

plt.plot(hist).history['loss'])

from sklearn.decomposition import PCA

x_train.shape

x_train_flattened = np.reshape(x_train, (60000, 28*28))

x_train_flattened.shape

pca = PCA()

pca.fit(x_train_flattened)

help(pca.transform)

x_train_pca = pca.transform(x_train_flattened)

x_train_pca

x_train_pca.shape

plt.imshow(np.reshape(x_train_pca[4],(28,28)))

pca.explained_variance_ratio_

np.sum(pca.explained_variance_ratio_)

plt.plot(np.cumsum(pca.explained_variance_ratio_))

x_train_pca[:,:200].shape

pca200 = PCA(n_components=200)

pca200.fit(x_train_flattened)

x_train_pca_200 = pca200.transform(x_train_flattened)

x_train_pca_200.shape

np.sum(pca200.explained_variance_ratio_)

x_train_pca_200[0].shape

x_train_pca_200_reconstructed = pca200.inverse_transform(x_train_pca_200)

x_train_pca_200_reconstructed.shape

plt.imshow(np.reshape(x_train_pca_200_reconstructed[4],(28,28)))

plt.imshow(x_train[4])


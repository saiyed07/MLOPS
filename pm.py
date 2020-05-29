# -*- coding: utf-8 -*-
"""Fashion_MNIST.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GG8DmNbT-VBet0r5ksbdqkrQIk7wIc1I
"""

import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd


fashion_mnist=keras.datasets.fashion_mnist

(train_images,train_labels),(test_images,test_lables)=fashion_mnist.load_data()

train_images=train_images/255.0
test_images=test_images/255.0

train_images[0].shape

train_images=train_images.reshape(len(train_images),28,28,1)
test_images=test_images.reshape(len(test_images),28,28,1)

train_images[1].shape


import imp
f = open("/workspace/input.txt","r")
global data
data = imp.load_source('data', '', f)
f.close()
epochs= int(data.epochs)

def build_model():
  model=keras.Sequential([keras.layers.Conv2D(filters=32,
                                              kernel_initializer="he_normal",
                                              kernel_size=(3,3),
                                              activation="relu",
                                              input_shape=(28,28,1)),
                                              ),
                          keras.layers.Flatten(),
                          keras.layers.Dense(units=32,activation="relu",kernel_initializer="he_normal"),
                          keras.layers.Dense(units=10,activation="softmax")
                          ])
  model.compile(keras.optimizers.Adam(0.001),loss="sparse_categorical_crossentropy",metrics=["accuracy"])
  return model

model=build_model()

model.summary()

model.fit(train_images,train_labels,epochs=epochs,validation_split=0.001)

y_pred=model.predict(test_images)

loss,accuracy=model.evaluate(train_images,train_labels)

file=open("/workspace/accuracy.txt","w")
file.write(str(accuracy))
file.close()

epochs=epochs +1
epochs=str(epochs)
str1="epochs= "+epochs
f=open("/workspace/input.txt","w")
file.write(str1)





# from keras.models import load_model

# model.save('mymoddel.h5')




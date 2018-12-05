# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 13:39:03 2018

@author: 大神悦
"""
from keras import backend as K
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import time
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Activation, Dropout
from keras.layers.advanced_activations import LeakyReLU
def reset_tf_session():
    K.clear_session()
    tf.reset_default_graph()
    s = K.get_session()
    return s 
mnist=input_data.read_data_sets("MNIST_data",one_hot=True)
X_train=mnist.train.images
y_train=mnist.train.labels
x_val=mnist.validation.images
y_val=mnist.validation.labels
x_test=mnist.test.images
y_test=mnist.test.labels
#y=tf.placeholder(tf.float32,[None,10])
x_train=np.reshape(X_train,[-1,28,28,1])
x_val=np.reshape(x_val,[-1,28,28,1])
x_test=np.reshape(x_test,[-1,28,28,1]) 
print(x_train.shape)
print(type(x_train))
print(y_train.shape)  #-1表示第一个维度由x确定
def make_model():
    model = Sequential()
    model.add(Conv2D(16,(3,3),padding='same',input_shape=(28,28,1)))
    model.add(Conv2D(32,(3,3),padding='same'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(64,(3,3),padding='same'))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(256))
    model.add(LeakyReLU(0.1))
    model.add(Dense(10))
    model.add(Activation("softmax"))
    return model
s = reset_tf_session()  # clear default graph
EPOCHS = 10
model = make_model()
model.summary()
model.compile(loss='categorical_crossentropy', optimizer='adagrad', metrics=['accuracy'])
start=time.time()
model.fit(x_train, y_train,epochs=10,batch_size=100)
score = model.evaluate(x_test, y_test, batch_size = 1000)
end=time.time()
print("总共耗时{}".format(end-start))
print('测试精度：{}'.format(score[1]))  #score[0] 代表loss  score[1] 表示accuracy






# -*- coding: utf-8 -*-
import tensorflow as tf

model=tf.keras.models.load_model('cnn.h5')
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
with open("cnn.tflite", 'wb') as o_:
    o_.write(tflite_model)
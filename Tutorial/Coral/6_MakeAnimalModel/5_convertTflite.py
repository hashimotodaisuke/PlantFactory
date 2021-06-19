# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np

def representative_data_gen():
  X_train, X_test, y_train, y_test = np.load("./dog_cat.npy", allow_pickle=True)
  X_train = X_train.astype("float32") / 255
  for input_value in tf.data.Dataset.from_tensor_slices(X_train).batch(1).take(100):
    yield [input_value]

model=tf.keras.models.load_model('cnn.h5')
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.representative_dataset = representative_data_gen
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.inference_input_type = tf.uint8
converter.inference_output_type = tf.uint8
converter.optimizations = [tf.lite.Optimize.DEFAULT]

tflite_model = converter.convert()
with open("cnn_IntegerQuantization.tflite", 'wb') as o_:
  o_.write(tflite_model)
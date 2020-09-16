# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

# Just disables the CPU instruction warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Training Data and Testing Data
train_signals = 
train_labels = 
test_signals = 
test_labels = 


class_names = ['5G', '4G LTE', '3G', '2G']

# Pre Processing of Signal Data --> Eventually handled Externally




# Define the ML model
model = keras.Sequential([
    # input layer (Flattens the Data, e.g a 2/3D array gets converted to a 1D)
    keras.layers.Flatten(input_shape=(28,28)), # Layer 1
    # Fully Connected layer - each neuron is connected to everyother 
    # .Desnse( number of neurons, activation function type)
    keras.layers.Dense(128, activation="relu"), # Layer 2
    keras.layers.Dense(4, activation = "softmax") # Layer 3
    ])

# Compile the ML Model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Train Model -> num epochs is the number of generations
model.fit(train_images, train_labels, epochs=10)

# Determines Accuracy of Model
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

# Prints accuracy to screen
print('\nTest accuracy:', test_acc)
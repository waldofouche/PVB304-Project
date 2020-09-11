import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Just disables the CPU instruction warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

data = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = data.load_data()

class_names = ['T-shirt/top','Trouser', 'Pullover', 'Dress',
                'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle Boot']

train_images = train_images/255.00
test_images = test_images/255.00

# Define the ML model
model = keras.Sequential([
    # input layer (Flattens the Data, e.g a 2/3D array gets converted to a 1D)
    keras.layers.Flatten(input_shape=(28,28)), # Layer 1
    # Fully Connected layer - each neuron is connected to everyother 
    # .Desnse( number of neurons, activation function type)
    keras.layers.Dense(128, activation="relu"), # Layer 2
    keras.layers.Dense(10, activation = "softmax") # Layer 3
    ])

# Compile the ML Model
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy",metrics=["accuracy"])

# Train Model -> num epochs is the number of generations
model.fit(train_images, train_labels, epochs=5)

# Determines Accuracy of Model
test_loss, test_acc = model.evaluate(test_images, test_labels)

# Prints accuracy to screen
print("Tested Acc: ",test_acc)

# Use the model to make a prediction
prediction = model.predict(test_images)

# The prediction is the nueron with the highest final value
# Using np.argmax gives the index of the nueron, thefore parse this
# to the class names to return the name of the predicted item
for i in range(5):
    plt.grid(False)
    plt.imshow(test_images[i], cmap=plt.cm.binary) # -> greyscale image
    plt.xlabel("Actual: " + class_names[test_labels[i]])
    plt.title("Prediction " + class_names[np.argmax(prediction[i])])
    plt.show()
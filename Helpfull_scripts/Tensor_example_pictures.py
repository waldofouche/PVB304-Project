#
# Copyright (c) 2017 François Chollet
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.


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


'''
The data must be preprocessed before training the network. If you inspect the first image in the training set, 
you will see that the pixel values fall in the range of 0 to 255:
'''
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()


# Scale these values to a range of 0 to 1 before feeding them to the neural network model.
train_images = train_images/255.00
test_images = test_images/255.00

# To verify that the data is in the correct format and ready to train the network - display the first 25 Images
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()


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
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Train Model -> num epochs is the number of generations
model.fit(train_images, train_labels, epochs=10)

# Determines Accuracy of Model
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

# Prints accuracy to screen
print('\nTest accuracy:', test_acc)

'''
With the model trained, you can use it to make predictions about some images. 
The model's linear outputs, logits. Attach a softmax layer to convert the logits to
probabilities, which are easier to interpret.
'''
probability_model = tf.keras.Sequential([model, 
                                         tf.keras.layers.Softmax()])

# Predict the label for each image in the testing set data
predictions = probability_model.predict(test_images)

# The first Prediction
print('\nRaw Data: ',predictions[0])

'''
A prediction is an array of 10 numbers. They represent the model's "confidence" that the image corresponds 
to each of the 10 different articles of clothing. You can see which label has the highest confidence value:
'''
print("\nLabel with the Highest Confidence Value: ",np.argmax(predictions[0]))

'''
So, the model is most confident that this image is an ankle boot, or class_names[9]
'''
print('\nLabel: ',test_labels[0],' Classification:', class_names[test_labels[0]])

# Show the plot of this image:
plt.grid(False)
plt.imshow(test_images[0], cmap=plt.cm.binary) # -> greyscale image
plt.xlabel("Actual: " + class_names[test_labels[0]])
plt.title("Prediction " + class_names[np.argmax(predictions[0])])
plt.show() 

# Show the full set of 10 predictions
def plot_image(i, predictions_array, true_label, img):
  true_label, img = true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  true_label = true_label[i]
  plt.grid(False)
  plt.xticks(range(10))
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')

# Plot the first X test images, their predicted labels, and the true labels.
# Color correct predictions in blue and incorrect predictions in red.
# The number gives the percentage (out of 100) for the predicted label.
num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(i, predictions[i], test_labels, test_images)
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(i, predictions[i], test_labels)
plt.tight_layout()
plt.show()

""" # Using the trained Model to predict a single Unkown images
# Grab an image from the test dataset.
img = test_images[1]
print(img.shape)

# tf.keras models are optimized to make predictions on a batch, or collection, 
# of examples at once. Accordingly, even though you're using a single image, you 
# need to add it to a list:

# Add the image to a batch where it's the only member.
img = (np.expand_dims(img,0))

print(img.shape)

# Predict the Image
predictions_single = probability_model.predict(img)

print('\n',predictions_single)

plot_value_array(1, predictions_single[0], test_labels)
_ = plt.xticks(range(10), class_names, rotation=45)

np.argmax(predictions_single[0]) """
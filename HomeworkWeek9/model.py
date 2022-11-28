# Module
import h5py

import numpy as np

import tensorflow as tf
from tensorflow import keras
import tensorflow.lite as tflite

from io import BytesIO
from urllib import request
from PIL import Image

# Model
filename = "dino_dragon_10_0.899.h5"

model = tf.keras.models.load_model(filename)

# Convert Model from Kers to tf-lite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)

tflite_model = converter.convert()

with open('model.tflite', 'wb') as f_out:
    f_out.write(tflite_model)

# Get index of input and output
interpreter = tflite.Interpreter(model_path='model.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

# Preparing the image
def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

# Define url
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Smaug_par_David_Demaret.jpg/1280px-Smaug_par_David_Demaret.jpg"

# Define target_size
target_size=(150, 150)

# Download image
img = download_image(url)

# Preparare image
img = prepare_image(img, target_size)

# Define Preprocessing
def preprocess_input(x):
    #x =1./255
    x /= 255
    return x

# Turn image in numpy-arry
x = np.array(img, dtype='float32')
X = np.array([x])

# Preprocess img
X = preprocess_input(X)

# Apply model to image
interpreter.set_tensor(input_index, X)
interpreter.invoke()
preds = interpreter.get_tensor(output_index)

print("The output of the model is: " ,preds[0])
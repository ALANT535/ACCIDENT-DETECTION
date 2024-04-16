import numpy as np
import cv2
import os
import tensorflow as tf
import pickle
from pickle_operations import *

directory=r"C:\Users\LENOVO\OneDrive\Desktop\DEVSOC\NEW_AP\DATASET\data\train"
pickle_path = r'C:\Users\LENOVO\Documents\Important_documents\VIT\HACK\DEVSOC\NEW_AP\devsoc\pickled data'

# X = pickle_read(pickle_path,'X.pickle')
# y = pickle_read(pickle_path,'y.pickle')

# X_normalised = np.array(X)/255.0

# pickle_dump(X_normalised,pickle_path,'normalized.pickle')

try:
    X_filename = 'normalized.pickle'
    y_filename = 'y.pickle'
    X_normalised = pickle_read(pickle_path,X_filename)
    y = pickle_read(pickle_path,y_filename)
except:
    print("File errors. Couldnt find files in the following directory - \n",os.path.join(pickle_path,pickle_path))

X_normalised = np.array(X_normalised)
y = np.array(y)

print(np.shape(y))
print(np.shape(X_normalised))

input_shape = (1280, 720, 1)

model = tf.keras.Sequential([
tf.keras.layers.Input(shape=input_shape),
tf.keras.layers.Conv2D(32, 3, activation='relu'),
tf.keras.layers.BatchNormalization(),
tf.keras.layers.MaxPooling2D(),
tf.keras.layers.Conv2D(64, 3, activation='relu'),
tf.keras.layers.MaxPooling2D(),
tf.keras.layers.Conv2D(128, 3, activation='relu'),
tf.keras.layers.MaxPooling2D(),
tf.keras.layers.Flatten(),
tf.keras.layers.Dense(256, activation='relu'),
tf.keras.layers.Dense(1, activation='sigmoid')
])

# print(model.summary())

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])   #binary_cross_entropy because there are only two classes

model.fit(X_normalised, y, batch_size = 32, epochs=10, validation_split=0.2)

model.save(os.path.join(pickle_path,'model.hd5'))
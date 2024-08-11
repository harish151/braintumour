import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras._tf_keras.keras.preprocessing.image import ImageDataGenerator

IMG_SIZE = 224
BATCH_SIZE = 32

# Data augmentation and preparation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)

train_generator = train_datagen.flow_from_directory(
    r'C:/Users/sathish rachuri/OneDrive/Desktop/project2/Brain_Tumor_Detection-20240301T070908Z-001/Brain_Tumor_Detection/Train',
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='binary',
    subset='training'
)

valid_generator = train_datagen.flow_from_directory(
    r'C:/Users/sathish rachuri/OneDrive/Desktop/project2/Brain_Tumor_Detection-20240301T070908Z-001/Brain_Tumor_Detection/Train',
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='binary',
    subset='validation'
)

# Define the model
model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_generator, validation_data=valid_generator, epochs=5)

# Save the model
model.save("Model.h5")

# Optionally, save labels to a text file
import os

labels = list(train_generator.class_indices.keys())
with open("label.txt", "w") as f:
    for label in labels:
        f.write(f"{label}\n")

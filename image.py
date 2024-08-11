import tensorflow as tf
from keras._tf_keras.keras.models import load_model
from keras._tf_keras.keras.preprocessing import image
import numpy as np

model=load_model("C:/Users/sathish rachuri/OneDrive/Desktop/project2/Model.h5")
model


#load and preprocess the test image
test_image_path='C:/Users/sathish rachuri/OneDrive/Desktop/project2/Brain_Tumor_Detection-20240301T070908Z-001/Brain_Tumor_Detection/Train/yes/y0.jpg'
img=image.load_img(test_image_path,target_size=(224,224))
img_array=image.img_to_array(img)
img_array=np.expand_dims(img_array,axis=0)

#add batch dimension
img_array/=255.#normalize the pixel values
#make predictions
prediction=model.predict(img_array)
#print the prediction
print(prediction)

if prediction < 0.5:
  print("prediction: No tumor(probability:",prediction[0][0])
else:
  print("prediction: Tumor present(probability:",prediction[0][0])

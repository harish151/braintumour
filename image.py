import tensorflow as tf
from keras._tf_keras.keras.models import load_model
from keras._tf_keras.keras.preprocessing import image
import numpy as np

def prediction(path):
    model=load_model("C:/Users/sathish rachuri/OneDrive/Desktop/project2/Model.h5")
    #load and preprocess the test image
    #C:\Users\sathish rachuri\OneDrive\Desktop\project2\uploads\y0.jpg
    modified_path = path.replace('\\', '/')
    #print(modified_path)
    test_image_path=f'C:/Users/sathish rachuri/OneDrive/Desktop/project2/'+f'{modified_path}'
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
        a=f'prediction: No tumor(probability:"{prediction[0][0]})'
    else:
        a=f'prediction: Tumor present(probability:{prediction[0][0]})'
    return a

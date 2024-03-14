import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas
import numpy as np
import tensorflow as tf
import gdown
import matplotlib.pyplot as plt

# Function to preprocess the image
def preprocess_image(image_data):
    image = Image.fromarray(image_data)
    
    # Resize using Lanczos resampling
    size = (28, 28)
    resized_image = image.resize(size, Image.LANCZOS)
    
    # Convert to grayscale
    resized_image = resized_image.convert('L')
    
    # Normalize pixel values to range [0, 1]
    resized_image_array = np.array(resized_image) / 255.0
    
    # Reshape to vector of size (1, 784)
    resized_image_vector = resized_image_array.reshape(1, -1)  # Reshape to row vector
    
    return resized_image_vector

# Function to load the trained model
def load_model():
    # Download model.h5 from Google Drive
    url = 'https://drive.google.com/uc?id=16m69DmL-r-x2bBNhKuyheDoUtFWxBFcq'
    output = 'model.h5'
    gdown.download(url, output, quiet=False)
    
    # Load the model
    model = tf.keras.models.load_model('model.h5')
    return model

# Function to make predictions
def predict_image(image_vector, model):
    prediction = model.predict(image_vector)
    return prediction

# Main function
def main():
    st.title("Handwritten Digit Recognition")

    # Load the trained model
    model = load_model()

    # Canvas for drawing
    st.write("Draw a digit on the canvas:")
    canvas_result = st_canvas(
        fill_color="#000000",  # Background color: black
        stroke_width=20,
        stroke_color="#FFFFFF",  # Drawing color: white
        background_color="#000000",  # Canvas color: black
        width=150,
        height=150,
        drawing_mode="freedraw",
        key="canvas",
    )

    # Make predictions on canvas image
    if canvas_result.image_data is not None:
        preprocessed_image_vector = preprocess_image(canvas_result.image_data)
        prediction = predict_image(preprocessed_image_vector, model)
        
        st.write("Prediction:")
        st.write(np.argmax(prediction))

if __name__ == "__main__":
    main()

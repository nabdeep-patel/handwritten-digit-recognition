import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas
import numpy as np
import requests
import tensorflow as tf
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
    url = 'https://drive.google.com/uc?id=16m69DmL-r-x2bBNhKuyheDoUtFWxBFcq&export=download'
    output = 'model.h5'
    
    # Download the file using requests
    response = requests.get(url)
    with open(output, 'wb') as f:
        f.write(response.content)
    
    # Load the model
    model = tf.keras.models.load_model(output)
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
        prediction = predict_image(canvas_result.image_data, model)
        st.write("Prediction:")
        st.write(prediction)

if __name__ == "__main__":
    main()

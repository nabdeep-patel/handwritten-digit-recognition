import streamlit as st
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import tensorflow as tf
import matplotlib.pyplot as plt

# Function to load the model from URL
@st.cache(allow_output_mutation=True)
def load_model(url):
    response = requests.get(url)
    model = tf.keras.models.load_model(BytesIO(response.content))
    return model

# Load the mode
model_url = "https://github.com/nabdeep-patel/handwritten-digit-recognition/tree/main/model/model.h5"  # Update this with your model's URL
model = load_model(model_url)

# Function to preprocess the drawn image
def preprocess_image(image):
    image = np.array(image)
    image = tf.image.resize(image, (28, 28))
    image = tf.image.rgb_to_grayscale(image)
    image = tf.reshape(image, (-1, 28, 28, 1))
    return image

# Streamlit app
def main():
    st.title("Handwritten Digit Recognition")
    st.write("Draw a digit on the canvas below and click on 'Predict'.")

    # Canvas to draw the digit
    canvas = st.image(np.zeros((150, 150)), caption='Draw Here', use_column_width=True, channels='L')

    # Prediction button
    if st.button("Predict"):
        # Get the drawn image
        img = canvas.image_data.astype(np.uint8)

        # Preprocess the image
        img = Image.fromarray(img)
        img = preprocess_image(img)

        # Predict
        prediction = model.predict(img).argmax(axis=1)[0]
        
        # Display prediction
        st.write(f"Predicted digit: {prediction}")

if __name__ == "__main__":
    main()

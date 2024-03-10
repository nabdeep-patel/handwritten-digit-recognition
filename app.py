import streamlit as st
import numpy as np
import requests
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image, ImageOps
import io
from streamlit_drawable_canvas import st_canvas

# Function to preprocess the drawn digit image
def preprocess_image(image_data):
    if image_data is None:
        return None
    # Convert the image to grayscale
    img = Image.fromarray(image_data).convert("L").resize((28, 28))
    # Invert the pixel values to match the MNIST dataset
    img = ImageOps.invert(img)
    # Convert image to array
    img_array = np.array(img) / 255.0  # Normalize pixel values
    img_array_flat = img_array.flatten()  # Flatten the image array
    img_array_flat = img_array_flat.reshape(1, -1)  # Reshape to match model input shape
    return img_array_flat

@st.cache_data
def load_digit_model():
    # Download model file
    model_url = 'https://drive.google.com/uc?export=download&id=16m69DmL-r-x2bBNhKuyheDoUtFWxBFcq'
    response = requests.get(model_url)
    model_path = 'model.h5'
    with open(model_path, 'wb') as f:
        f.write(response.content)
    # Load the pre-trained model
    model = load_model(model_path)
    return model

st.title('Handwritten Digit Recognition')

# Create a canvas for drawing digits
canvas_result = st_canvas(
    fill_color="#000000",  # Background color of the canvas
    stroke_width=12,  # Width of the brush stroke
    stroke_color="#FFFFFF",  # Color of the brush stroke
    background_color="#000000",  # Color of the background
    height=150,  # Height of the canvas
    width=150,  # Width of the canvas
    drawing_mode="freedraw",  # Drawing mode (freedraw or line)
    key="canvas",
)

# Load the model
model = load_digit_model()

# Add a submit button
if st.button('Recognize Digit'):
    if canvas_result.image_data is None:
        st.write("Please draw a digit.")
    else:
        try:
            # Convert drawn image to array
            img_array = preprocess_image(canvas_result.image_data)
            if img_array is not None:
                # Get model prediction
                prediction = np.argmax(model.predict(img_array), axis=-1)
                st.write(f"Predicted digit: {prediction[0]}")
            else:
                st.write("Please draw a digit.")
        except Exception as e:
            st.error(f"Error predicting digit: {e}")

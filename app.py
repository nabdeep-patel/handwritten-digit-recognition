import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import gdown
import os

# Function to download the model
def download_model():
    url = 'https://drive.google.com/uc?export=download&id=16m69DmL-r-x2bBNhKuyheDoUtFWxBFcq'
    output = 'model.h5'
    gdown.download(url, output, quiet=False)

# Function to load the trained model
def load_model():
    if not os.path.exists('model.h5'):
        download_model()
    model = tf.keras.models.load_model('model.h5')
    return model
    
def preprocess_image(image_data):
    image = Image.fromarray(image_data)
    
    # Resize using Lanczos resampling
    size = (28, 28)
    resized_image = image.resize(size, Image.LANCZOS)
    
    # Convert to numpy array
    resized_image_array = np.array(resized_image)
    resized_image_array = resized_image_array.astype('float32')
    
    return np.expand_dims(resized_image_array, axis=0)

def main():
    st.title("Hadwritten Digit Recognition")
    st.sidebar.header("Navigation")

    # Sidebar navigation links with bullets
    st.sidebar.markdown("- [app.py](#app)")
    st.sidebar.markdown("- [GitHub](#github)")
    st.sidebar.markdown("- [IPython Notebook](#ipython-notebook)")
    st.sidebar.write("---")
    
    # Connect with me section
    st.sidebar.markdown("Connect with me:")
    github_link = "[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?style=flat-square&logo=github)](https://github.com/nabdeep-patel)"
    linkedin_link = "[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/nabdeeppatel)"
    website_link = "[![Website](https://img.shields.io/badge/Personal-Website-blue?style=flat-square&logo=chrome)](https://linktr.ee/nabdeeppatel/store)"
    email_link = "[![Email](https://img.shields.io/badge/Google-Mail-blue?style=flat-square&logo=gmail)](mailto:nabdeeppatel@gmail.com)"
    
    st.sidebar.markdown(github_link + " " + linkedin_link + " " + website_link + " " + email_link)
    st.sidebar.markdown("Created by Nabdeep Patel")
    mycanvas()

def preprocess_image(image_data):
    image = Image.fromarray(image_data)
    size = (28, 28)
    resized_image = image.resize(size, Image.LANCZOS)
    resized_image = resized_image.convert('L')
    resized_image_array = np.array(resized_image) / 255.0
    resized_image_vector = resized_image_array.reshape(1, -1)  # Reshape to row vector
    
    return resized_image_vector

def mycanvas():
    st.write("Draw a digit on the canvas and click get prediction.")

    canvas_result = st_canvas(
        fill_color="#eee",
        stroke_width=20,
        stroke_color="white",
        background_color="black",
        update_streamlit=True,
        height=280,  
        width=280,   
        drawing_mode="freedraw",
    )
    
    st.write("Image of the canvas")
    if canvas_result.image_data is not None:
        preprocessed_image_vector = preprocess_image(canvas_result.image_data)
        
        # Plot and show the resized image
        
        fig = plt.figure(figsize=(3, 3))
        plt.imshow(preprocessed_image_vector.reshape(28, 28), cmap='gray')  # Reshape back to 28x28 for visualization
        plt.title('Resized Image')
        plt.axis('off')
        
        if st.button("Get Prediction"):
            st.write("Processed image")
            st.pyplot(fig)
            model = load_model()
            predictions = model.predict(preprocessed_image_vector)
            # Print the predictions
            st.write("Predictions:")
            st.write(predictions)
            predictions1 = model.predict(np.expand_dims(preprocessed_image_vector, axis=0))[0]
            predicted_digit = np.argmax(predictions1)
            st.write(f"Predicted Digit: {predicted_digit}")
            

if __name__ == "__main__":
    main()

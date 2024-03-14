import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas
import numpy as np
import tensorflow as tf
import gdown
import matplotlib.pyplot as plt

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
    st.title("Simple Streamlit App")
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
    
    # Resize using Lanczos resampling
    size = (28, 28)
    resized_image = image.resize(size, Image.LANCZOS)
    
    # Convert to grayscale
    resized_image = resized_image.convert('L')
    
    # Normalize pixel values to range [0, 1]
    resized_image_array = np.array(resized_image) / 255.0
    
    return np.expand_dims(resized_image_array, axis=0)

def mycanvas():
    st.write("Canvas")

    canvas_result = st_canvas(
        fill_color="#eee",
        stroke_width=16,
        stroke_color="white",
        background_color="black",
        update_streamlit=True,
        height=280,  # Increase canvas size to improve drawing quality
        width=280,   # Increase canvas size to improve drawing quality
        drawing_mode="freedraw",
    )
    
    st.write("Image of the canvas")
    if canvas_result.image_data is not None:
        st.image(canvas_result.image_data)
        preprocessed_image = preprocess_image(canvas_result.image_data)
        
        # Plot and show the resized image
        plt.imshow(preprocessed_image.squeeze(), cmap='gray')
        plt.title('Resized Image')
        plt.axis('off')
        st.pyplot()

        # Display shape of the resized image
        st.write(f"Resized image shape: {preprocessed_image.shape}")


if __name__ == "__main__":
    main()

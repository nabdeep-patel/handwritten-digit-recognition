import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas
import numpy as np
import tensorflow as tf
import gdown

def preprocess_image(image_data):
    """
    Preprocesses the image data obtained from the canvas.

    Parameters:
        image_data (numpy.ndarray): The image data obtained from the canvas.

    Returns:
        numpy.ndarray: The preprocessed image data.
    """
    # Convert image data to PIL Image
    image = Image.fromarray(image_data)

    # Resize the image to (100, 100) for downsampling
    resized_image = image.resize((100, 100))

    # Convert resized image to numpy array
    resized_image_data = np.array(resized_image)

    # Flatten the resized image data
    flattened_image_data = resized_image_data.reshape(10000, 4)

    return flattened_image_data

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

def mycanvas():
    st.write("Canvas")

    canvas_result = st_canvas(
        fill_color="#eee",
        stroke_width=10,
        stroke_color="white",
        background_color="black",
        update_streamlit=True,
        height=200,
        width=200,
        drawing_mode="freedraw",
    )
    
    st.write("Image of the canvas")
    if canvas_result.image_data is not None:
        st.image(canvas_result.image_data)
        preprocessed_image = preprocess_image(canvas_result.image_data)
        st.write("Preprocessed Image Shape:", preprocessed_image.shape)

        # Download the model file from Google Drive
        url = 'https://docs.google.com/uc?export=download&id=16m69DmL-r-x2bBNhKuyheDoUtFWxBFcq'
        output = 'model.h5'
        gdown.download(url, output, quiet=False)

        # Load the model
        model = tf.keras.models.load_model('model.h5')

        # Make predictions
        predicted_probs = model.predict(preprocessed_image.reshape(1, 10000, 4))
        predicted_classes = np.argmax(predicted_probs, axis=1)

        # Display predicted classes
        st.write("Predicted Classes:", predicted_classes)

if __name__ == "__main__":
    main()

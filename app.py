import streamlit as st
import pickle
import numpy as np
from PIL import Image

# Load the pre-trained model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Define the Streamlit app interface
st.title('Handwritten Digit Recognition')

option = st.sidebar.selectbox(
    'Choose an option:',
    ('Draw a digit', 'Upload an image')
)

if option == 'Draw a digit':
    drawing_mode = st.checkbox("Enable drawing mode", True)
    drawn_image = st.canvas(drawn_image=None, width=150, height=150, drawing_mode=drawing_mode, key="canvas")

    if st.button("Recognize"):
        # Convert the drawn image to a NumPy array
        image_array = np.array(drawn_image.image_data)

        # Resize the image to fit the model's input shape
        image_array = cv2.resize(image_array, (28, 28))

        # Convert to grayscale and flatten the image
        # Here's a simple example using OpenCV and NumPy
        image_array = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
        image_array = image_array.flatten()

        # Make prediction
        prediction = model.predict(image_array.reshape(1, -1))

        # Display the prediction
        st.write('Predicted Digit:', prediction[0])

else:
    uploaded_image = st.file_uploader("Upload an image of a handwritten digit", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Display the uploaded image
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Preprocess the image
        # You need to resize, convert to grayscale, and flatten the image
        # Here's a simple example with PIL and NumPy
        image_array = np.array(image)
        # image_array = your_preprocessing_function(image_array)

        # Make prediction
        prediction = model.predict(image_array.reshape(1, -1))

        # Display the prediction
        st.write('Predicted Digit:', prediction[0])

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
        stroke_width=10,
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

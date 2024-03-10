import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image

st.title("Drawable Canvas")
st.markdown("""
Draw on the canvas, get the image data back into Python!
* Double-click to remove the selected object when not in drawing mode
""")
st.sidebar.header("Configuration")

# Specify brush parameters and drawing mode
b_width = 12
b_color = "#FFFFFF"
bg_color = "#000000"
drawing_mode = "freestyle"

# Create a canvas component
image_data = st_canvas(
    b_width, b_color, bg_color, height=150, drawing_mode=drawing_mode, key="canvas"
)

# Do something interesting with the image data
if image_data is not None:
    # Convert the CanvasResult object to a PIL Image
    pil_image = Image.frombytes("RGBA", (image_data.shape[1], image_data.shape[0]), image_data)

    # Display the PIL Image using st.image
    st.image(pil_image)

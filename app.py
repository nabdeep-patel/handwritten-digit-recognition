import streamlit as st
from PIL import Image

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

def canvas():
    st.title("Drawable Canvas App")

    # Create a drawable canvas
    canvas = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Orange with opacity
        stroke_width=10,
        stroke_color="rgb(255, 165, 0)",
        background_color="#FFF",
        width=300,
        height=300,
        drawing_mode="freedraw",
        key="canvas"
    )

    # Convert the canvas data to an image
    if canvas.image_data is not None:
        image = Image.fromarray(canvas.image_data.astype("uint8"))

        # Display the canvas as an image
        st.image(image, caption="Your Drawing", use_column_width=True)

if __name__ == "__main__":
    main()

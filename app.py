import streamlit as st

def main():
    st.title("Simple Streamlit App")
    st.sidebar.header("Navigation")

    # Sidebar navigation links with bullets
    st.sidebar.markdown("- [app.py](#app)")
    st.sidebar.markdown("- [GitHub](#github)")
    st.sidebar.markdown("- [IPython Notebook](#ipython-notebook)")
    st.write("---")
    st.markdown(
        "[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nabdeeppatel)"
    )
    st.markdown(
        "[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/nabdeep-patel)
"
    )

    # Anchor tags for navigation
    st.markdown("<a id='app'></a>", unsafe_allow_html=True)
    st.write("## app.py")
    st.write("Content for app.py")

    st.markdown("<a id='github'></a>", unsafe_allow_html=True)
    st.write("## GitHub")
    st.write("Content for GitHub")

    st.markdown("<a id='ipython-notebook'></a>", unsafe_allow_html=True)
    st.write("## IPython Notebook")
    st.write("Content for IPython Notebook")

    # Footer LinkedIn button
    st.markdown(
        "[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/)"
    )

if __name__ == "__main__":
    main()

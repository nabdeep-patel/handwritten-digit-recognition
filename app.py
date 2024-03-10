import streamlit as st

def main():
    st.title("Simple Streamlit App")
    st.sidebar.header("Navigation")

    # Sidebar buttons
    if st.sidebar.button("app.py"):
        st.write("You clicked the app.py button")
    if st.sidebar.button("GitHub"):
        st.write("You clicked the GitHub button")
    if st.sidebar.button("IPython Notebook"):
        st.write("You clicked the IPython Notebook button")

    # Footer LinkedIn button
    st.markdown(
        "[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/)"
    )

if __name__ == "__main__":
    main()

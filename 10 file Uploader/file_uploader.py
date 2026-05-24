import streamlit as st

st.title("Streamlit Upload Fuctions")

# file uploader
file=st.file_uploader("Upload file here:",accept_multiple_files=True)


for x in file:
    # image file
    st.title("Image File")
    st.image(x)

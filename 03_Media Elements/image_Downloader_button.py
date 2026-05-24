import streamlit as st

# Image downloader Button
st.header("Image Downloader Button")


image="https://www.w3schools.com/w3css/img_lights.jpg"
st.image(image, width=300, caption="Beautiful Lights")

text=st.text_input("Name the Path of Image: ")
with open("https://www.w3schools.com/w3css/img_lights.jpg",'rb') as file:
    st.download_button(label="Download Image",data=file,file_name=text,mime='image/png')
    
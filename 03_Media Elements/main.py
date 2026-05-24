import streamlit as st


# Media Element
st.header("Media Elements in Streamlit")

st.subheader("Audio Element")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", start_time=2,end_time=10) # audio will Automatically start at 2 second and stop at 10 second

st.subheader("Video Element")
st.video("https://www.youtube.com/watch?v=ZtL2b9XjHkY", start_time=10) # video will Automatically start at 10 second


# image elements
st.subheader("Image Element")
st.image("https://www.w3schools.com/w3css/img_lights.jpg", width=300,caption="Beautiful Lights") # image with width and caption
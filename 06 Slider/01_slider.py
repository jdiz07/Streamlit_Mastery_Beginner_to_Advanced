import streamlit as st

st.header("Slider in Streamlit")

slider=st.slider("Select a range: ",0,100,25) # 0, 100 is the range, and 25 is the default value

st.write(f"You selected : {slider}")

sliderimage=st.slider("Select the size of the image:",100,400,200)
st.image("https://www.python.org/static/community_logos/python-logo.png", width=sliderimage, caption="Python Logo")
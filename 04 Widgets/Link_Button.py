import streamlit as st


st.header("Streamlit")

# link button
st.subheader("Link Button")
image="https://www.w3schools.com/w3css/img_lights.jpg"
st.image(image, width=300, caption="Beautiful Lights")
st.link_button("Visit Our Portfolio","https://www.linkedin.com/in/muhammadjunaidjaved07/")
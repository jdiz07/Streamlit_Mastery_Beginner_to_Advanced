import streamlit as st

# Widget

st.header("Widget Elements in Streamlit")

# text input 
name=st.text_input("Enter your name: ")

# Button
button =st.button("Press me")

if button==True:
    st.write(f'Welcome {name}')


# Selectbox
name=st.text_input("Enter a programming language: ")
available_languages=["Python","JavaScript","Java","C++"]
button=st.button("Check Availability")

if button==True:
    have_it=name.lower() in available_languages
    if have_it:
        st.write(f" {name} is available in the list")
    else:
        st.write(f" {name} is not available in the list")
import streamlit as st

# Text Input

st.header("Text Input in Streamlit")

text=st.text_input("Enter your name: ")
button=st.button("Submit")
if button:
    st.write(f"Hello {text}!")


# Number input
st.header("Number Input in Streamlit")

number1=st.number_input("Enter the first number: ",step=1)
number2=st.number_input("Enter the Second number: ",step=1)
col1, col2,col3,col4=st.columns(4)

with col1:
    if st.button("Add"):
        st.write(f"The sum is: {number1+number2}")

with col2:
    if st.button("Subtract"):
        st.write(f"The difference is: {number1-number2}")
with col3:
    if st.button("Multiplication"):
        st.write(f"The difference is: {number1*number2}")
with col4:
    if st.button("Division"):
        st.write(f"The difference is: {number1/number2}")
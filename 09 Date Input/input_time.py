import streamlit as st
import time

num=st.number_input("Enter a number:",step=1)

time1=st.time_input("Select a time: ",value=None)
if st.button("Submit"):
    st.write(f'Time Selected :{time1}')

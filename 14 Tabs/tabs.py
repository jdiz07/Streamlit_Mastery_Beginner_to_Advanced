import streamlit as st


# making the tabs

st.header("Making the Tabs")
t1,t2,t3=st.tabs(["Python","C++","Java"])

with t1:
    st.header("Python Language")
    st.text("Python is open source plateform")

with t2:
    st.header("C++")
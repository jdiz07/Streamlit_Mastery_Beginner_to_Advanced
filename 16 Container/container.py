import streamlit as st
import time

# Empty are used to delete the iterations
st.header("Empty")

time1=st.text_input("Enter the Time")
button=st.button("Start")
if button:
    with st.empty():
        for s in range(int(time1)):
            st.write(f"{s}")
            time.sleep(1)
        st.image("https://www.python.org/static/community_logos/python-logo.png", width=300, caption="Python Logo")
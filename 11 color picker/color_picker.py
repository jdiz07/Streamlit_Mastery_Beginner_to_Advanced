import streamlit as st

st.title("Streamlit Colorpicker Elements")


color=st.color_picker("Pick a color:","#00FFAA")
# text=st.markdown(f"<span-style-color:{color}> Welcome to my site! </span>",unsafe_allow_html=True)

st.write(f"Your color code :   **{color}**")
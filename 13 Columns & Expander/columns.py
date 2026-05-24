import streamlit as st

# Columns
st.header("Making the column in Streamlit")

c1,c2,c3=st.columns(3)

with c1:
    st.header("Python")
    st.image("https://www.python.org/static/community_logos/python-logo.png", width=200,caption="Python")
    st.link_button("Click to Enter my site","https://www.linkedin.com/in/muhammadjunaidjaved07/")
with c2:
    st.header("Streamlit")
    st.image("https://www.python.org/static/community_logos/python-logo.png", width=200,caption="Python")
    st.link_button("Click to Enter my site","https://www.linkedin.com/in/muhammadjunaidjaved07/")
with c3:
    st.header("Flask")
    st.image("https://www.python.org/static/community_logos/python-logo.png", width=200,caption="Python")
    st.link_button("Click to Enter my site","https://www.linkedin.com/in/muhammadjunaidjaved07/")
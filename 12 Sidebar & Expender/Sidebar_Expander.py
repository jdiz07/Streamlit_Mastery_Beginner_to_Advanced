import streamlit as st


# making the sidebar
st.header("Making the Sidebar in Streamlit")
with st.sidebar:
    text=st.text('SideBar')
    box=st.selectbox("Select your Favorite Car: ",["BMW","Audi","Mercedes"])
    radio=st.radio("Select your color:",["A","B","C","D"] )


# Expender

with st.expander("Unknown Facts............."):
    st.write("Mostly People who are interested in the cars having age between 15 - 35 ")
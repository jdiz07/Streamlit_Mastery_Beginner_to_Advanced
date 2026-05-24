import streamlit as st
import pandas as pd



# Displaying the matrics
st.subheader("Metrics")
st.metric(label="Temperature",value='25°C',delta='-2°C') 


# making the table
st.subheader("Making the table")

data=({
    "col1":[1,2,3],
    "col2":[4,5,6]
})
st.table(data)


st.header("DataFrame table")
# Dataframe
st.dataframe(data)


# Adding the Emojis
st.subheader("Emojis")
st.write("Here are some emojis :joy:")
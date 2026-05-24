# Loan Calculation using Streamlit Slider
import streamlit as st


st.header("Loan Calculation using Streamlit using select slider")
import streamlit as st

st.markdown("### Select your Amount")
amount_money=st.select_slider("Select the money you want to borrow:",options=[0,1000,3000,5000,6000,70000,8000,9000,10000],value=5000)
st.markdown("### Select your Durations: ")
num_months=st.select_slider("Select the number of Months for the loan:",options=[1,2,3,4,5,6,7,8],value=3)

calculation=((amount_money/100)*(1/12)*(num_months*30)+amount_money)
st.markdown("### Calculation: ")
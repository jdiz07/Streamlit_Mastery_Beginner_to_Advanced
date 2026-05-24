import streamlit as st
import datetime

st.header("Streamlit Data Input Elements")

Starting_Date=st.date_input("Select the Starting Date: ")
end_date=st.date_input("Select the Ending Date: ")
t1=str(Starting_Date).split("-")
t2=str(end_date).split("-")
t1=datetime.date(year=int(t1[0]),month=int(t1[1]),day=int(t1[2]) )
t2=datetime.date(year=int(t2[0]),month=int(t2[1]),day=int(t2[2]) )
if st.button('Calculate Days'):
    st.write(f"The number of days between {Starting_Date} and {end_date} is {(t2-t1).days} days")
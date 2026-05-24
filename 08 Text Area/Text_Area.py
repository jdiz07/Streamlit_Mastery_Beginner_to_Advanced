import streamlit as st

# Text Area
st.header("Text Area in Streamlit")
list=[]
text=st.text_area("Enter your Feedback:","",placeholder="Type your message here...",max_chars=200)
button=st.button("Submit")
if button:
    new_text=text.split(sep=" ")
    for x in new_text:
        list.append(x)
    st.write(f"Your feedback contains {len(list)} words and {len(text)} characters")
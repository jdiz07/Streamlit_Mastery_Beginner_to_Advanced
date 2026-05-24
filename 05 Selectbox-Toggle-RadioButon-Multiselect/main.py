import streamlit as st

# Checkbox

st.header("CheckBox in Streamlit")

checkbox=st.checkbox("I agree to the terms and conditions")
if checkbox:
    st.write("Thank you for agreeing to the terms and conditions")
code=st.checkbox("Do you want to see the Structure of python code")

if code:
    st.code("python('Hello World')",language="python")


# Toggle
st.header("Toggle in Streamlit")

tog=st.toggle("Enable the Image")

audio=st.toggle("Enable the Audio")

if tog:
    st.image("https://www.python.org/static/community_logos/python-logo.png", width=200,caption="Python")

if audio:
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# Radio Button
st.header("Radio Button in Streamlit")
radio=st.radio("Select your Favorite Car:",["BMW","Audi","Mercedes","Tesla"],index=None)

if radio=='BMW':
    st.write("You selected BMW")
elif radio=='Audi':
    st.write("You selected Audi")
elif radio=='Mercedes':
    st.write("You selected Mercedes")
elif radio=='Tesla':
    st.write("You selected Tesla")


# Select box

st.header("SelectBox in Streamlit")

box=st.selectbox("Select your favorite Programming Language:",["Python",'C++',"Java"],index=None)

# Multiselect 
# We can select multiple options from the list
st.header("Multiselect in Streamlit")
st.text("In Multiselect we can select the multiple options from the list")

ml=st.multiselect("Select your Favorite Things: ",["Gaming pc","Laptop", "Smartphones","Tablets","play Station"],default=["Gaming pc","Laptop"])

for x in ml:
    if x=="Gaming pc":
        st.image("https://images.pexels.com/photos/30469971/pexels-photo-30469971.jpeg", width=200, caption="Gaming PC")
    elif x=="Laptop":
        st.image("https://cdn.mos.cms.futurecdn.net/9e5a1c8b2c0e7f1d9b3e4c8f1a2b3c4.jpg", width=200, caption="Laptop")
    elif x=="Smartphones":
        st.image("https://cdn.mos.cms.futurecdn.net/9e5a1c8b2c0e7f1d9b3e4c8f1a2b3c4.jpg", width=200, caption="Smartphones")
    elif x=="Tablets":
        st.image("https://cdn.mos.cms.futurecdn.net/9e5a1c8b2c0e7f1d9b3e4c8f1a2b3c4.jpg", width=200, caption="Tablets") 
    elif x=="play Station":
        st.image("https://cdn.mos.cms.futurecdn.net/9e5a1c8b2c0e7f1d9b3e4c8f1a2b3c4.jpg", width=200, caption="play Station")
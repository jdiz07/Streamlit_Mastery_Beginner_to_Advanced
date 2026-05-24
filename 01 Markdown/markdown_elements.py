from pathlib import Path

import streamlit as st

st.title("Markdown Elements in Streamlit")

st.subheader("Heading Elements")
# Heading elements
st.markdown("# Heading 1")
st.markdown("## Heading 2 ")
st.markdown("### Heading 3")

st.subheader("Text Formatting")
# bold text
st.markdown("**Bold Text**")
# italic Text
st.markdown("*Italic Text*")


# strikethrough text
st.markdown("~~Strikethrough Text~~")

st.subheader("Black Quotes")
st.markdown("> Used for the Quotations")

# Ordered list
st.subheader("Ordered List")
st.markdown("1. First Item\n2. Second item\n3. Third items")

# Unordered List
st.subheader("Unordered List")
st.markdown("- First items\n- Second items\n- Third items")


#Code Block
st.subheader("Code Block")
code_example = "print('Hello World')"
st.code(code_example, language="python")


# Horizotal Line
st.subheader("Horizontal Line")
st.markdown("---")


# Links
st.subheader("Links")
st.markdown("[LinkedIn](https://www.linkedin.com/in/muhammadjunaidjaved07/)")

# Images
st.subheader("Images")
image_path = Path(__file__).resolve().parents[1] / "Wedding.png"
if image_path.exists():
    st.image(str(image_path), width=300)
else:
    st.warning(f"Image not found: {image_path.name}")



# Extended settings
st.subheader("Making the Table")
st.markdown("""
| Name | Age | City |
| --- | --- | --- |
| Junaid | 22 | Islamabad |
| JD | 21 | Rawalpindi |""")

# JSON Data
st.subheader("JSON Data")
json_data={
    "name":"Junaid",
    "age":22,
    "city":"Islamabad"
}
st.json(json_data)


# Footnote
st.subheader("Footnote")
st.markdown("This is a footnote example[^1].\n\n[^1]: This is the footnote text.")

# Definition List
st.subheader("Definition List")
st.markdown("Term 1\n: hello\n\nTerm 2\n: world")

# task List
st.subheader("Task List")
st.markdown("- [x] Task 1\n- [ ] Task 2\n- [ ] Task 3")

# important
st.subheader("Important")   
st.markdown("**Important:** This is an important message.")


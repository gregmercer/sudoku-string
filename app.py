import streamlit as st
import os
import print_board as pb

# ask the user to upload the file
uploaded_file = st.file_uploader(
    "Upload your file here...", type=["png", "jpeg", "jpg"]
)
if uploaded_file is not None:
    with open(os.path.join(os.path.dirname(__file__), "temp.png"), "wb") as f:
        f.write(uploaded_file.read())
        st.image("temp.png")
        value = pb.process_image("temp.png")
        st.write(value)

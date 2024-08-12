from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Configure the Google Generative AI API
genai.configure(api_key=)

# Initialize the GenerativeModel
model = genai.GenerativeModel("gemini-1.5-pro")

# Define a function to get responses from the Gemini Pro model
def get_gemini_response(input_text, image):
    if input_text != "":
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(image)
    
    return response.text

# Initialize the Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

# Text input for user input
input_text = st.text_input("Input: ", key="input")

# File uploader for image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the uploaded image
    image = Image.open(uploaded_file)
    
    # Display the uploaded image
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    # Button to trigger response generation
    submit = st.button("Tell me about the image")

    # Handle button click event
    if submit:
        response = get_gemini_response(input_text, image)
        st.subheader("The Response is")
        st.write(response)

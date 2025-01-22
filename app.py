from dotenv import load_dotenv
load_dotenv() # loads all the environment variables from the .env file

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
import base64

# Configure the generative model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro Vision
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt]) # input = describes the behaviour of the LLM; image = path of the image
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        # Encode the bytes_data to base64
        encoded_data = base64.b64encode(bytes_data).decode('utf-8')

        image_data = [
            {
                "mime_type": uploaded_file.type,
                "data": encoded_data
            }
        ]

        return image_data
    
    else:
        raise FileNotFoundError("Please upload an invoice")

st.set_page_config(page_title="Multi-Language Invoice Extractor")

st.header("Multi-Language Invoice Extractor")
input = st.text_input("Input Prompt", key="input")
uploaded_file = st.file_uploader("Choose an image/invoice...", type=["jpg", "jpeg", "png"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded successfully!!", use_container_width=True) # Display the image

submit = st.button("Describe the invoice")

input_prompt = """
You are an expert at understanding invoices.
The user will upload an invoice and you will have to answer any questions about the invoice uploaded.
"""

# If submit button is clicked
if submit:
    try:
        image_data = input_image_details(uploaded_file)
        response = get_gemini_response(input_prompt, image_data, input)
        st.subheader("The response is:")
        st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {e}")

import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
import google.ai.generativelanguage as glm
from PIL import Image

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

if API_KEY is None:
    st.error("API Key is not set. Please set the API key in the .env file.")
else:
    genai.configure(api_key=API_KEY)

st.set_page_config(page_title="Gemini Pro Vision Image Analysis Project", page_icon="📸", layout="centered", initial_sidebar_state='collapsed')

st.header("Google AI Studio + Gemini Pro")

uploaded_file = st.file_uploader("Choose an Image file", accept_multiple_files=False, type=['jpg', 'png'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    bytes_data = uploaded_file.getvalue()
text = st.text_input("Enter your prompt here..", "")

generate = st.button('Generate!')

if generate:
    if API_KEY is None:
        st.error("API Key is not set. Please set the API key in the .env file.")
    else:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content(
            glm.Content(
                parts=[
                    glm.Part(text=text),
                    glm.Part(inline_data=glm.Blob(mime_type='image/jpeg', data=bytes_data)),
                ],
            ),
            stream=True
        )

        response.resolve()

        st.write(response.text)

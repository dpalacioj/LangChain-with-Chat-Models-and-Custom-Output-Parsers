from langchain_openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

import streamlit as st

# Function to get OpenAI response using LangChain's OpenAI wrapper
def get_openai_response(question):
    llm=OpenAI(api_key=openai_api_key, model_name="gpt-3.5-turbo-instruct", temperature=0.9)
    response=llm(question)
    return response

# Initialize Streamlit App
st.set_page_config(page_title="Q&A Demo")

# Display app header
st.header("LangChain Demo Application")

# Text input for user question
input=st.text_input("Input: ", key="input")

# Get the OpenAI response based on user input
response = get_openai_response(input)

# Submit button for asking the question
submit = st.button("Ask the question")

# If the submit button is clicked, display the response
if submit:
    st.subheader("The Response is")
    st.write(response)
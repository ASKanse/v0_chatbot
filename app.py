import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Google Gemini
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Set page config
st.set_page_config(page_title="Simple Chatbot", page_icon="🤖")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize the chat model
model = genai.GenerativeModel('gemini-2.0-flash')

# Add a title
st.title("🤖 Simple Chatbot")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What's on your mind?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model.generate_content(prompt)
            st.markdown(response.text)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response.text}) 
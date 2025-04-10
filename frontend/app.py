import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="BNS QnA Chatbot",
    page_icon="🤖",
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display header
st.markdown(
    "<h1 style='color: teal;'>BNS based QnA Chatbot</h1>",
    unsafe_allow_html=True
)
st.subheader("Hey! How can I help you today? Ask me anything related to BNS.")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
user_input = st.chat_input("How can I help you today?")

# Process user input
if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
    
    try:
        with st.spinner("Retrieving..."):
            path = os.path.join(os.getenv("BACKEND_URL"), "chat/query")
            
            backend_response = requests.post(
                path,
                json={"query": user_input}
            )
            backend_response.raise_for_status()
            response = backend_response.json().get("response", "No response from backend.")
    
    except requests.exceptions.RequestException as e:
        response = f"Error contacting backend: {e}"
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Display assistant response
    with st.chat_message("assistant"):
        st.write(response)
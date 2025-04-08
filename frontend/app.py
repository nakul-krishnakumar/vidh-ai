import streamlit as st

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
    
    # Prepare response (replace this with your RAG implementation)
    if "document" in user_input.lower() or "rag" in user_input.lower():
        response = "Based on your documents, I found some relevant information about RAG systems."
    else:
        response = "I'm a simple RAG bot. How can I help you today?"
    
    # Add bot response to chat history
    st.session_state.messages.append({"role": "bot", "content": response})
    
    # Display bot response
    with st.chat_message("bot"):
        st.write(response)
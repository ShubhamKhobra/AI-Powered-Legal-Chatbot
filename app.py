import streamlit as st
from src.pipeline import pipeline

st.set_page_config(page_title="AI Legal Chatbot", layout="wide")
st.title("📜 AI-Powered Legal Chatbot")


# Sidebar info
with st.sidebar:
    st.header("🔧 Model Info")
    st.write("Model: GPT-3.5-turbo via OpenAI")
    st.button("🔄 Reset Chat", on_click=lambda: st.session_state.clear())

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask me anything about the document. I’ll respond based on its content."):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = pipeline(prompt)

    # Create a list to hold the answer
    answer = []

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        # Streaming the response
        for segment in response:
            if "answer" in segment:
                word = segment['answer']
                answer.append(word)
        st.write_stream(answer)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": "".join(answer)})

st.caption("Built with LangChain, OpenAI, and Streamlit")

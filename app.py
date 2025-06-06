import streamlit as st
from utils.doc_reader import read_document
import requests
import json

# -------------------------------
# Ollama model and config
OLLAMA_MODEL = "llama3"
OLLAMA_URL = "http://localhost:11434/api/chat"

# -------------------------------
# Session state setup
if "document_text" not in st.session_state:
    st.session_state.document_text = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "last_uploaded_file_name" not in st.session_state:
    st.session_state.last_uploaded_file_name = None

# -------------------------------
# Streamlit UI
st.set_page_config(page_title="LLM Document QA", layout="centered")
st.title("📄 Chat with Your Document (Ollama + Streamlit)")

uploaded_file = st.file_uploader("Upload a document (PDF, DOCX, or TXT)", type=["pdf", "docx", "txt"])

# Handle new uploads (reset chat only if file changed)
if uploaded_file:
    if uploaded_file.name != st.session_state.last_uploaded_file_name:
        st.session_state.document_text = read_document(uploaded_file)
        st.success("✅ Document uploaded and processed successfully!")
        st.session_state.chat_history = []  # reset chat history for new file
        st.session_state.last_uploaded_file_name = uploaded_file.name

# Show chat interface only if document is loaded
if st.session_state.document_text:
    st.subheader("Ask a question about the document:")
    user_input = st.chat_input("Type your question...")

    if user_input:
        with st.spinner("Thinking..."):

            # Build messages: document + chat history + latest question
            messages = [
                {
                    "role": "system",
                    "content": (
                        "You are a helpful assistant that answers questions based only on the provided document."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        "Here's the document content:\n\n"
                        + st.session_state.document_text[:5000]  # safety limit
                    )
                }
            ]

            # Add previous conversation history
            for item in st.session_state.chat_history:
                messages.append({"role": "user", "content": item["user"]})
                messages.append({"role": "assistant", "content": item["bot"]})

            # Add current user question
            messages.append({"role": "user", "content": user_input})

            # Send request to Ollama
            response = requests.post(
                OLLAMA_URL,
                json={"model": OLLAMA_MODEL, "messages": messages},
                stream=True
            )

            # Stream and display response
            full_response = ""
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                for chunk in response.iter_lines():
                    if chunk:
                        line = chunk.decode("utf-8").strip()
                        if line.startswith("data: "):
                            line = line[len("data: "):]
                        try:
                            data = json.loads(line)
                            token = data.get("message", {}).get("content", "")
                            full_response += token
                            message_placeholder.markdown(full_response)
                        except json.JSONDecodeError:
                            continue

            # Save Q&A to history
            st.session_state.chat_history.append({
                "user": user_input,
                "bot": full_response
            })

    # Display full conversation
    if st.session_state.chat_history:
        st.divider()
        st.subheader("🗂 Chat History")
        for i, turn in enumerate(st.session_state.chat_history, 1):
            st.markdown(f"**Q{i}:** {turn['user']}")
            st.markdown(f"**A{i}:** {turn['bot']}")
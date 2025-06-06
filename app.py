import streamlit as st
from utils.doc_reader import read_document
import requests
from pathlib import Path

def query_ollama(prompt, model="llama3", context=None):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": f"{context}\n\n{prompt}",
        "stream": False
    }
    response = requests.post(url, json=payload)
    return response.json()["response"]

st.title("📄 LLM Document QA App")

uploaded_file = st.file_uploader("Upload a document", type=["pdf", "docx", "txt"])
user_prompt = st.text_input("Ask something about the document:")

if uploaded_file:
    file_path = Path(f"temp/{uploaded_file.name}")
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    doc_content = read_document(str(file_path))

    if user_prompt:
        with st.spinner("Thinking..."):
            response = query_ollama(user_prompt, context=doc_content)
        st.markdown("### 📤 LLM Response:")
        st.markdown(response, unsafe_allow_html=True)
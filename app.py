import streamlit as st
from utils.doc_reader import read_document
import requests
from pathlib import Path
import json

def query_ollama_stream(prompt, model="llama3", context=None):
    """
    Stream the response from the local Ollama server.
    """
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": f"{context}\n\n{prompt}",
        "stream": True
    }

    response = requests.post(url, json=payload, stream=True)
    for line in response.iter_lines():
        if line:
            data = json.loads(line.decode("utf-8"))
            yield data.get("response", "")

# Streamlit UI
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
            response_area = st.empty()
            full_response = ""
            for chunk in query_ollama_stream(user_prompt, context=doc_content):
                full_response += chunk
                response_area.markdown(full_response, unsafe_allow_html=True)

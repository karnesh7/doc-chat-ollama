# LLM Document QA App

This is a Streamlit app that lets you upload a document and ask questions about its content using a locally running LLM via Ollama. It now supports follow-up questions in a conversation format!

---

## 🧠 Features

- 📄 Upload PDF, DOCX, or TXT files
- 🤖 Ask questions about the uploaded document
- 🔁 Ask follow-up questions in the same session
- 📜 Chat history displayed
- 🚀 Real-time streaming responses using Ollama
- 🧼 Clean and simple Streamlit interface

---

## ⚙️ Requirements

- Python 3.8+
- [Ollama](https://ollama.com) installed and running locally
- Ollama model downloaded (e.g., `llama3`)
- Dependencies listed in `requirements.txt`

---

## 🛠 Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/llm-doc-streamlit.git
   cd llm-doc-streamlit



2. (Optional) Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/Scripts/activate     # Windows
   # or
   source venv/bin/activate         # macOS/Linux
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run Ollama locally with the desired model, for example:

   ```bash
   ollama run llama3
   ```

5. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

6. Open the browser to the URL shown by Streamlit (usually [http://localhost:8501](http://localhost:8501)).

---

## Usage

* Upload a document.
* Type a question related to the document.
* Get a response from the LLM.
* Ask follow-up questions — the app keeps the chat history.
* View the entire Q&A thread below the chat box.

---

## Notes

* Ollama must be running locally for the app to work.
* Larger documents might slow down the response. Consider splitting or summarizing.

---

## License

MIT License


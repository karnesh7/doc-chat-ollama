# LLM Document QA App

This is a Python + Streamlit app that lets you upload a document and ask questions about its content using a locally running LLM via Ollama.  
It supports **follow-up questions**, **chat history**, **document summarization**, and now includes a **desktop GUI (WebView)** option in a separate branch!

---

## 🧠 Features

- 📄 Upload PDF, DOCX, or TXT files
- 🤖 Ask questions about the uploaded document
- 🔁 Ask follow-up questions in the same session
- 🧾 View chat history and document preview
- 📝 One-click document summarization
- 🚀 Real-time streaming responses using Ollama
- 🌐 Run in browser or 🖥️ as a WebView desktop app

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
   ```


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

---

## 🚀 Running the App

### Option 1: **Streamlit in Web Browser (Default)**

```bash
streamlit run app.py
```

Visit: [http://localhost:8501](http://localhost:8501)

---

### Option 2: **Desktop GUI (WebView Mode)**

This is available in the `webview-gui` branch.

```bash
git checkout webview-gui
python desktop_launcher.py
```

> Requires `pywebview` installed:
> `pip install pywebview`

This opens the Streamlit app in a standalone desktop window.

---

## 💬 Usage

1. Upload a document
2. Ask a question
3. Get a real-time response from Ollama
4. Ask follow-up questions (chat history retained)
5. Use the "Summarize Document" button for a quick overview
6. Use the "Clear Chat" button to reset conversation

---

## Notes

* Ollama must be running locally for the app to work
* Large documents can slow down processing
* Currently only local models are supported

---

## 🔀 Branches

| Branch        | Description                                          |
| ------------- | ---------------------------------------------------- |
| `main`        | Standard Streamlit app in browser                    |
| `webview-gui` | App with Streamlit embedded in desktop GUI (WebView) |

---

## 📄 License

MIT License

---

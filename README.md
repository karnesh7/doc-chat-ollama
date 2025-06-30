# LLM Document QA App (WebView GUI)

This is the **WebView-based desktop GUI version** of the Streamlit + Ollama document Q&A app.

---

## 🔍 What’s Different?

- The app runs in a **desktop window** (not browser)
- Launches using `pywebview` instead of visiting localhost manually
- Same core functionality: upload document → ask questions → get AI-powered answers

---

## 🛠 How to Run

1. Install requirements:

```bash
pip install -r requirements.txt
````

2. Make sure Ollama is running:

```bash
ollama run llama3
```

3. Run the app GUI:

```bash
python desktop_launcher.py
```

---

## 🔁 Back to Browser Version?

Switch to the `main` branch:

```bash
git checkout main
streamlit run app.py
```

---

## 📝 License

MIT License

---

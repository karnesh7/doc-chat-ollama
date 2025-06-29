import threading
import webview
import subprocess
import time
import os

def start_ollama():
    try:
        # Start Ollama model (adjust the model name if needed)
        subprocess.Popen(["ollama", "run", "llama3"])
    except Exception as e:
        print("Error launching Ollama:", e)

def start_streamlit():
    try:
        subprocess.Popen(["streamlit", "run", "app.py", "--server.headless", "true"])
    except Exception as e:
        print("Error launching Streamlit:", e)

# Start Ollama in a background thread
ollama_thread = threading.Thread(target=start_ollama)
ollama_thread.daemon = True
ollama_thread.start()

# Give it a few seconds to start the model
time.sleep(5)

# Start Streamlit in a background thread
streamlit_thread = threading.Thread(target=start_streamlit)
streamlit_thread.daemon = True
streamlit_thread.start()

# Give Streamlit a bit of time to boot up
time.sleep(3)

# Launch native app window with webview
webview.create_window("LLM Document QA App", "http://localhost:8501", width=1200, height=800)
webview.start()
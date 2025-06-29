import threading
import webview
import subprocess
import time

# Store process references
ollama_proc = None
streamlit_proc = None

def start_ollama():
    global ollama_proc
    # Start a smaller/lighter model if needed
    ollama_proc = subprocess.Popen(["ollama", "run", "llama3"])

def start_streamlit():
    global streamlit_proc
    streamlit_proc = subprocess.Popen(["streamlit", "run", "app.py", "--server.headless", "true"])

def stop_processes():
    print("Shutting down processes...")
    if streamlit_proc:
        streamlit_proc.terminate()
    if ollama_proc:
        ollama_proc.terminate()

if __name__ == "__main__":
    try:
        # Start Ollama and Streamlit in background threads
        threading.Thread(target=start_ollama, daemon=True).start()
        time.sleep(5)  # Wait a bit for Ollama to start

        threading.Thread(target=start_streamlit, daemon=True).start()
        time.sleep(3)  # Wait a bit for Streamlit to start

        # Start the PyWebView app
        webview.create_window("LLM Document QA App", "http://localhost:8501", width=1200, height=800)
        webview.start()

    finally:
        # This runs after the GUI window is closed
        stop_processes()
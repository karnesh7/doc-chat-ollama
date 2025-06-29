import threading
import webview
import os
import time

# Change this if your app.py is in a different path
APP_COMMAND = "streamlit run app.py --server.headless true"

def start_streamlit():
    os.system(APP_COMMAND)

# Start Streamlit in a new thread
t = threading.Thread(target=start_streamlit)
t.daemon = True
t.start()

# Wait a moment for the server to start
time.sleep(3)

# Create the GUI window pointing to localhost
webview.create_window("LLM Document QA App", "http://localhost:8501", width=1200, height=800)
webview.start()

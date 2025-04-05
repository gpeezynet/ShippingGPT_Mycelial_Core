from flask import Flask, render_template, request, redirect, send_from_directory
import os
from datetime import datetime

app = Flask(__name__)

# Log directory for human reflections
LOG_DIR = "logs/operator_insights"
os.makedirs(LOG_DIR, exist_ok=True)

# --- Routes ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/entropy-log')
def entropy_log():
    return render_template('entropy_log.html')

@app.route('/sop-viewer')
def sop_viewer():
    return render_template('sop_viewer.html')

@app.route('/human')
def human_interface():
    files = []
    if os.path.exists(LOG_DIR):
        files = sorted(os.listdir(LOG_DIR), reverse=True)[:5]
    return render_template('human_interface.html', files=files)

@app.route('/submit-reflection', methods=['POST'])
def submit_reflection():
    reflection = request.form.get("reflection", "").strip()
    if reflection:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{LOG_DIR}/reflection_{timestamp}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(reflection)
    return redirect('/human')

@app.route('/logs/operator_insights/<filename>')
def view_reflection(filename):
    return send_from_directory(LOG_DIR, filename)

# --- Main ---

if __name__ == '__main__':
    app.run(debug=True)

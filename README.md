📘 LLM Question-and-Answering System (CLI + Web GUI)
CSC331 – Project 2

This project implements a Natural Language Processing (NLP) Question-and-Answering System using a Large Language Model (LLM) API.
It includes:

✅ A Python Command-Line Interface (CLI)

✅ A Web-based GUI Application built with Flask

✅ Integration with Google Gemini API for real-time LLM responses

✅ Deployment-ready structure for platforms like Render, PythonAnywhere, or Vercel

📂 Project Structure
LLM_QA_Project_YourName_MatricNo/
│-- LLM_QA_CLI.py
│-- app.py
│-- requirements.txt
│-- LLM_QA_hosted_webGUI_link.txt
│-- templates/
│     └── index.html
│-- static/
      └── style.css

🚀 Features
✔ CLI Application

Accepts natural-language questions

Performs preprocessing:

lowercasing

tokenization

punctuation removal

Sends processed text to Gemini API

Displays cleaned question and AI response

✔ Web Application (Flask GUI)

Clean, elegant dark-themed UI

User-friendly interface to enter questions

Shows:

Original user question

Processed text

Final LLM response

Uses AJAX (Fetch API) for smooth, no-reload interaction

🔑 API Setup (Gemini / Google AI Studio)
Get your free API key here:

👉 https://aistudio.google.com/app/apikey

Steps:

Sign in with any Google account

Click Create API Key

If asked to select a cloud project → choose NEW PROJECT

Copy your API key

Paste it into your code:

API_KEY = "YOUR_API_KEY"
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + API_KEY

🖥 Installation & Running Locally
1. Install required packages:
pip install flask requests gunicorn


Or if you're using the provided file:

pip install -r requirements.txt

2. Run the Web App:
python app.py


Then open:

http://127.0.0.1:5000/

3. Run the CLI App:
python LLM_QA_CLI.py

🌐 Deployment Instructions (Render.com)
Steps:

Push your project to GitHub

Log into https://render.com

Click New → Web Service

Connect your GitHub repo

Set:

Build Command:

pip install -r requirements.txt


Start Command:

gunicorn app:app


Add environment variable:

API_KEY = your_actual_gemini_key


Deploy and copy your live link

Paste link into:
LLM_QA_hosted_webGUI_link.txt

📄 requirements.txt
Flask
requests
gunicorn

🎨 Frontend Technologies Used

HTML5

CSS3 (dark theme + gradients + glassmorphism)

JavaScript (Fetch API)

🧠 Backend Technologies Used

Python

Flask

Google Gemini API

Regular Expressions

JSON Parsing

📝 Author

Name: Sharon Ndukuba

Matric No: 23CD034341

Course: CSC331

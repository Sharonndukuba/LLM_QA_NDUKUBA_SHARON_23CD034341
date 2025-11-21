# app.py
from flask import Flask, render_template, request, jsonify
import re
import requests

app = Flask(__name__)

API_KEY = "AIzaSyCpwd7gYMjOuc5fqGrwrhZacKY64o6p4JY"    # <-- Replace with your Gemini or Cohere Key
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + API_KEY

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = text.split()
    return " ".join(tokens)

def ask_llm(question):
    payload = {
        "contents": [{
            "parts": [{"text": question}]
        }]
    }
    response = requests.post(API_URL, json=payload)
    data = response.json()
    return data["candidates"][0]["content"]["parts"][0]["text"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_q = request.form["question"]
    processed = preprocess(user_q)
    answer = ask_llm(user_q)
    return jsonify({
        "processed": processed,
        "answer": answer
    })

if __name__ == "__main__":
    app.run(debug=True)

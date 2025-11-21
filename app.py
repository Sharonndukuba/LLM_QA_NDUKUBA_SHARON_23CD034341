# app.py
from flask import Flask, render_template, request, jsonify
import re
import requests
import json
import os

app = Flask(__name__)

API_KEY = os.environ.get("API_KEY")   # <-- Replace with your Gemini or Cohere Key
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + API_KEY

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = text.split()
    return " ".join(tokens)

def ask_llm(question):
    def ask_llm(question):
        headers = {
            "Content-Type": "application/json",
        }

        payload = {
            "prompt": {
                "messages": [
                    {"role": "user", "content": [{"type": "text", "text": question}]}
                ]
            }
        }

        response = requests.post(API_URL, headers=headers, json=payload)
        data = response.json()

        # Debug: print the full response to see what Gemini returned
        print(json.dumps(data, indent=2))

        # Safe extraction
        if "candidates" in data and len(data["candidates"]) > 0:
            candidate = data["candidates"][0]
            if "content" in candidate and len(candidate["content"]) > 0:
                parts = candidate["content"][0].get("parts", [])
                if len(parts) > 0:
                    return parts[0].get("text", "No text returned")
        return "No valid answer returned from the API"

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

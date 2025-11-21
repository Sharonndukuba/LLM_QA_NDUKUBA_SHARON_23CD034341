# LLM_QA_CLI.py
import re
import requests

API_KEY = "AIzaSyCpwd7gYMjOuc5fqGrwrhZacKY64o6p4JY"    # <-- Replace with your Gemini or Cohere Key
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + API_KEY

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = text.split()
    return tokens

def ask_llm(question):
    payload = {
        "contents": [{
            "parts": [{"text": question}]
        }]
    }
    response = requests.post(API_URL, json=payload)
    data = response.json()
    return data["candidates"][0]["content"]["parts"][0]["text"]

if __name__ == "__main__":
    print("=== LLM Question Answering CLI ===")
    user_q = input("Enter your question: ")

    tokens = preprocess(user_q)
    print("\nProcessed Question:", " ".join(tokens))

    answer = ask_llm(user_q)
    print("\nLLM Response:\n", answer)

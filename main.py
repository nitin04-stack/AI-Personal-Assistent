from flask import Flask,render_template,url_for,request,jsonify
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

app = Flask(__name__)

load_dotenv()
api_key = os.getenv("google_api_key")
client = client = genai.Client(api_key=api_key)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/ask" , methods=["POST"])
def ask():
    question = request.form.get("question")
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        # model = "gemini-2.0-flash-lite",
        contents=question,                   
        config=types.GenerateContentConfig(   
            system_instruction="Act like a helpful personal assistant. Give answers in a precise and meaningful way."
        )
    )
    answer =  response.text.strip()
    return jsonify({"response": answer}),200

@app.route("/summarize" , methods=["POST"])
def summrize():
    email_text = request.form.get("email")
    summary_prompt = f"summarize the following email in 2-3 sentences {email_text}"
    response = client.models.generate_content(
        model = "gemini-3.1-flash-lite",
        contents=summary_prompt,              
        config=types.GenerateContentConfig(
            system_instruction="Act like an expert email assistant. Give a summary in 2-3 brief bullet points."
        )
    )
    summary= response.text.strip()
    return jsonify({"response": summary}),200

if __name__ == "__main__":
    app.run(debug=True)

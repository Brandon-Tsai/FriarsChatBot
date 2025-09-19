from flask import Flask, render_template, request, jsonify, session
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "supersecret")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form["message"]

    if "conversation" not in session:
        session["conversation"] = []

    session["conversation"].append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="ft:gpt-3.5-turbo-0125:personal::CHOURDgX",
        messages=session["conversation"]
    )

    answer = response.choices[0].message.content
    session["conversation"].append({"role": "assistant", "content": answer})

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

from flask import Flask, render_template, request, jsonify
import openai
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form["message"]

    # Use new ChatCompletion API syntax
    response = openai.ChatCompletion.create(
        model="ft:gpt-3.5-turbo-0125:personal::CHOURDgX",  # your fine-tuned model
        messages=[{"role": "user", "content": user_input}]
    )

    answer = response.choices[0].message.content
    return jsonify({"answer": answer})

if __name__ == "__main__":
    # host=0.0.0.0 makes it accessible externally
    app.run(host="0.0.0.0", port=5000, debug=True)

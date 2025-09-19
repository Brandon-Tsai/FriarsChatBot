from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form["message"]

    # New API syntax for OpenAI >= 1.0.0
    response = openai.chat.completions.create(
        model="ft:gpt-3.5-turbo-0125:personal::CHOURDgX",  # or your fine-tuned model
        messages=[{"role": "user", "content": user_input}]
    )

    answer = response.choices[0].message.content
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
#!/usr/bin/env python3
# save as chat_terminal.py

from openai import OpenAI
import os

client = OpenAI()   # reads API key from OPENAI_API_KEY env variable

MODEL = "ft:gpt-3.5-turbo-0125:personal::CHOURDgX"  # replace with your fine-tuned model

def main():
    print("Chatbot ready! Type 'exit' to quit.")
    history = [{"role": "system", "content": "You are a helpful assistant."}]

    while True:
        user = input("You: ")
        if user.lower() in {"exit", "quit"}:
            break

        history.append({"role": "user", "content": user})
        resp = client.chat.completions.create(
            model=MODEL,
            messages=history,
            temperature=0.7,
            stream=False
        )

        reply = resp.choices[0].message.content
        print("Brandon:", reply)
        history.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    main()

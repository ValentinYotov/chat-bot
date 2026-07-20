from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

api_key = os.getenv("api_key")

client = OpenAI(api_key=api_key)


def chat(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user = input("You: ")
        if user.lower() in ["quit", "exit"]:
            break
        response = chat(user)
        print(f"Bot: {response}")

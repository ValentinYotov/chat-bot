from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

api_key = os.getenv("api_key")

client = OpenAI(api_key=api_key)
history = []
history.append({"role":"system","content":"You are really helpful assistant."})
def chat(prompt):
    history.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=history,
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user = input("You: ")
        if user.lower() in ["quit", "exit"]:
            break
        response = chat(user)
        history.append({"role": "assistant", "content": response})
        print(f"Bot: {response}")

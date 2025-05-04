import openai

client = openai.OpenAI(api_key="...")  # използвай твоя API ключ тук

def chat_with_gpt(prompt):
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return chat_completion.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat.")
            break
        response = chat_with_gpt(user_input)
        print(f"GPT-3.5: {response}")

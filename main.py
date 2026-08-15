from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

api_key = os.getenv("api_key")

class ChatBot:
    def __init__(self):
        self.history = [{"role":"system","content":"You are really helpful assistant."}]
        self.client = OpenAI(api_key=api_key)

    def chat(self,prompt):
        self.history.append({"role": "user", "content": prompt})
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.history,
        )
        self.history.append({"role": "assistant", "content": response.choices[0].message.content.strip()})
        print("Bot:", response.choices[0].message.content.strip())
    
    
 
if __name__ == "__main__":
    chatbot = ChatBot()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the chat. Goodbye!")
            break
        chatbot.chat(user_input)

  
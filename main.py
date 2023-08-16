import os
import openai
from dotenv import load_dotenv
from rich import print

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

print("[bold green]Please enter your prompt: ")
userInput = input()

response = openai.ChatCompletion.create(
        model = os.getenv("MODEL"),
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": userInput
            },
            ]
)

print(response.choices[0].message.content)

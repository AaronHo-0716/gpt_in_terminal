import os
import openai
from rich.console import Console

console = Console()

def response():
    console.print("[bold green]Please enter your prompt: ")
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
    console.print(response.choices[0].message.content)

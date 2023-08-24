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
                    "role": "user",
                    "content": userInput
                },
                ],
            stream=True
    )

    for chunk in response:
        if "content" in chunk.choices[0].delta:
            console.print(chunk.choices[0].delta.content, end='')

    print('\n')

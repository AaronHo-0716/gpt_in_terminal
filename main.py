import os
import openai
from dotenv import load_dotenv
from rich.console import Console
from clear import clear
import API
from changeModel import changeModel

console = Console()
load_dotenv()

clear()

if "OPENAI_API_KEY" in os.environ:
    openai.api_key = os.environ["OPENAI_API_KEY"]
else:
    clear()
    API.inputAPI()
    load_dotenv()
    openai.api_key = os.environ["OPENAI_API_KEY"]

console.print("Welcome to GPT in terminal!", style='bold green')
console.print("1. Change API Key")
console.print("2. Select GPT Model")

choice = int(input())
match choice:
    case 1:
        API.inputAPI()

    case 2:
        changeModel()
# console.print("[bold green]Please enter your prompt: ")
# userInput = input()

# response = openai.ChatCompletion.create(
#         model = os.getenv("MODEL"),
#         messages = [
#             {
#                 "role": "system",
#                 "content": "You are a helpful assistant."
#             },
#             {
#                 "role": "user",
#                 "content": userInput
#             },
#             ]
# )

# print(response.choices[0].message.content)

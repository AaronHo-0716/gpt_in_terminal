import os
import openai
from dotenv import load_dotenv
from rich.console import Console
from clear import clear
import API
from changeModel import changeModel
from gptResponse import response

console = Console()
load_dotenv()

clear()

defaultModel = 'gpt-3.5-turbo'

def initialCheck():
    if "OPENAI_API_KEY" in os.environ:
        clear()
        API.changeEnv(os.environ["OPENAI_API_KEY"], defaultModel)
        openai.api_key = os.environ["OPENAI_API_KEY"]
    else:
        clear()
        API.inputAPI(defaultModel)
        load_dotenv()
        openai.api_key = os.environ["OPENAI_API_KEY"]

def showMenu():
    console.print("Welcome to GPT in terminal!", style='bold green')
    console.print("1. Change API Key")
    console.print("2. Select GPT Model")
    console.print("3. Use GPT")
    console.print("4. Exit")

    choice = int(input())
    match choice:
        case 1:
            API.inputAPI(os.environ["MODEL"])

        case 2:
            model = changeModel()
            print(f"Model selected is {model}")
            API.changeEnv(os.environ["OPENAI_API_KEY"], model)
            
        case 3:
            clear()
            response()

        case 4:
            quit()

if __name__ == "__main__":
    initialCheck()
    while True:
        showMenu()

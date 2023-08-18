import os
import re
import openai
from dotenv import load_dotenv
from rich.console import Console
from clear import clear

console = Console()
load_dotenv()

reg = re.compile(r"gpt")

def changeModel():
    clear()
    openai.api_key = os.environ["OPENAI_API_KEY"]
    models = openai.Model.list()

    modelsList = []

    for model in models["data"]:
        modelsList.append(model['id'])
    
    gptModels = list(filter(reg.search, modelsList))
    
    console.print("[bold green]These are the available models: ")
    for k, v in enumerate(gptModels):
        console.print(f"{k+1}. {v}", highlight=False)

    console.print("[bold green]Type the model you want to use:")
    model = input()
    
    return model

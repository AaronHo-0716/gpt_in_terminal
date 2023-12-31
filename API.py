from rich.console import Console
from clear import clear

console = Console()

def inputAPI(model):
    console.print("[bold green]Enter your Open AI API key: ")
    api = input()
    with open(".env", "w") as f:
        f.write(f"OPENAI_API_KEY={api} \n MODEL={model}")
    clear()

def changeEnv(api, model):
    with open(".env", "w") as f:
        f.write(f"OPENAI_API_KEY={api} \n MODEL={model}")
    clear()

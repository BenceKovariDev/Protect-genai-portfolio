import os
from openai import OpenAI
from rich.console import Console
from rich.panel import Panel

# --- Konfiguracio ---
console = Console()
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"), 
    base_url="https://api.groq.com/openai/v1"
)

# --- Rendszer beallitas ---
system_prompt = (
    "Te egy Senior AI Software Engineer vagy. "
    "Fokuszteruleted a RAG rendszerek, Docker es felhoalapu architektura. "
    "Pragmatikus, termelesi szintu megoldasokra torekszel. "
    "Valaszaidat attekinthetoen, strukturáltan (pl. listak, rovid bekezdesek) add meg."
)

beszelgetes_tortenet = [{"role": "system", "content": system_prompt}]

def main():
    # Udvozlo panel
    console.print(Panel.fit(
        "[bold blue]>>> Protect Agent Initialized & Ready[/bold blue]", 
        border_style="blue"
    ))
    
    while True:
        try:
            # 1. Bemenet bekerese (egyszeru prompttal)
            felhasznalo_kerdes = console.input("\n[bold green]User Input >[/bold green] ")
            
            if felhasznalo_kerdes.lower() in ["kilepes", "exit", "quit"]:
                console.print(Panel.fit("[bold red]Shutting down...[/bold red]", border_style="red"))
                break
            
            # 2. Bemenet megjelenitese dizajnos panelben
            user_panel = Panel(
                f"[white]{felhasznalo_kerdes}[/white]",
                title="[bold cyan]🧠 Felhasznalo Kerdese[/bold cyan]",
                border_style="cyan",
                expand=False
            )
            console.print(user_panel)
            
            beszelgetes_tortenet.append({"role": "user", "content": felhasznalo_kerdes})
            
            # 3. API hivas
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=beszelgetes_tortenet
            )
            
            valasz = response.choices[0].message.content
            beszelgetes_tortenet.append({"role": "assistant", "content": valasz})
            
            # 4. AI Valasz megjelenitese dizajnos panelben
            ai_panel = Panel(
                f"[white]{valasz}[/white]",
                title="[bold magenta]🤖 AI Rendszer Valasza[/bold magenta]",
                border_style="magenta",
                expand=False
            )
            console.print(ai_panel)
            
        except Exception as e:
            error_panel = Panel(
                f"[bold red]{e}[/bold red]", 
                title="[bold red]⚠️ Critical Error[/bold red]", 
                border_style="red"
            )
            console.print(error_panel)

if __name__ == "__main__":
    main()

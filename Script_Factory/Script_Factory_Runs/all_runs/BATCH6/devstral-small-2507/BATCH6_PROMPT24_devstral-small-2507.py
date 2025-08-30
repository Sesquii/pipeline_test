# BATCH6_PROMPT24_Devstral.py

import time
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn
from rich.spinner import Spinner
from rich.live import Live
from rich.table import Table

# Initialize Rich console
console = Console()

def display_welcome():
    """Display a welcome message with styling"""
    welcome_panel = Panel(
        "[bold magenta]Welcome to the Conversational Command Line Interface![/bold magenta]\n"
        "This is a demo interface using the rich library.",
        style="blue",
        title="[bold white]WELCOME[/bold white]"
    )
    console.print(welcome_panel)

def display_spinner(message):
    """Display a spinning loading indicator"""
    with Live(Spinner("line", text=message, style="cyan"), refresh_per_second=10) as live:
        for _ in range(20):  # Simulate work
            time.sleep(0.3)

def display_progress_bar():
    """Display a never-ending progress bar"""
    with Progress(
        SpinnerColumn(spinner_name="line", style="green"),
        "[progress.percentage]{task.percentage:>3.0f}%",
        "[progress.description]{task.description}",
        TimeElapsedColumn(),
    ) as progress:
        task = progress.add_task("[cyan]Processing...", total=100)
        
        while not progress.finished:
            progress.update(task, advance=0.5)
            time.sleep(0.2)

def display_interactive_table():
    """Display an interactive table"""
    table = Table(title="[bold white]User Commands[/bold white]")
    table.add_column("Command", style="cyan", width=15)
    table.add_column("Description", style="magenta")

    commands = [
        ("help", "Show help information"),
        ("status", "Check system status"),
        ("exit", "Exit the interface"),
    ]

    for cmd, desc in commands:
        table.add_row(f"[bold]{cmd}[/bold]", desc)

    console.print(table)

def main():
    """Main function to run the conversational CLI"""
    display_welcome()
    display_spinner("Loading system components...")
    display_progress_bar()  # This will run indefinitely
    display_interactive_table()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold red]Interface terminated by user.[/bold red]")
```

This script creates a colorful, interactive command line interface using the `rich` library with various visual elements including panels, spinners, progress bars, and tables. The spinner will run for 6 seconds before proceeding to the never-ending progress bar, demonstrating the visually distracting nature requested.
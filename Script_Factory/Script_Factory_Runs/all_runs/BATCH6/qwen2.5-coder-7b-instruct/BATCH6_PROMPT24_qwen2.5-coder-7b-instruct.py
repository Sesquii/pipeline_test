#!/usr/bin/env python3

# Import necessary libraries
import time
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table

def main():
    console = Console()
    
    # Example of a colorful and visually distracting spinner
    with Progress(console=console,
                  spinner_column=SpinnerColumn(spinner='dots12'),
                  text_column=TextColumn("[bold magenta]{task.description}")) as progress:
        task1 = progress.add_task("[cyan]Processing...", total=None)
        
        # Simulate a long-running process
        while not progress.finished:
            time.sleep(0.5)  # Simulate work being done
            
    # Example of a colorful table
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Name", style="dim", no_wrap=True)
    table.add_column("Age")
    table.add_column("City", justify="right")
    
    table.add_row("Alice", "24", "New York")
    table.add_row("Bob", "30", "Los Angeles")
    table.add_row("Charlie", "29", "Chicago")
    
    console.print(table)

if __name__ == "__main__":
    main()
```
This script uses the `rich` library to create a visually distracting CLI. It includes a spinner that never finishes and a colorful table with data.
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

# ===== GENERATED TESTS =====
```python
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

# Test suite for the script
import pytest
from rich.console import Console
from rich.progress import Progress
from rich.table import Table

@pytest.fixture
def mock_console():
    """Fixture to replace the real Console with a mock object."""
    return MockConsole()

class MockConsole:
    def __init__(self):
        self.output = []

    def print(self, text):
        self.output.append(text)

    def clear(self):
        self.output.clear()

def test_spinner(mock_console):
    """Test that the spinner runs without errors."""
    with Progress(console=mock_console,
                  spinner_column=SpinnerColumn(spinner='dots12'),
                  text_column=TextColumn("[bold magenta]{task.description}")) as progress:
        task1 = progress.add_task("[cyan]Processing...", total=None)
        
        # Simulate a long-running process
        for _ in range(5):
            time.sleep(0.1)  # Simulate work being done

    assert len(mock_console.output) > 0, "Spinner should have produced output"

def test_table(mock_console):
    """Test that the table is created and printed correctly."""
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Name", style="dim", no_wrap=True)
    table.add_column("Age")
    table.add_column("City", justify="right")
    
    table.add_row("Alice", "24", "New York")
    table.add_row("Bob", "30", "Los Angeles")
    table.add_row("Charlie", "29", "Chicago")
    
    mock_console.print(table)
    
    expected_output = [
        "[bold magenta]Name[/bold magenta][dim]   [/dim][cyan]Age[/cyan][cyan]City[/cyan]",
        "[cyan]Alice[/cyan][cyan] 24[/cyan][cyan] New York[/cyan]",
        "[cyan]Bob[/cyan][cyan] 30[/cyan][cyan] Los Angeles[/cyan]",
        "[cyan]Charlie[/cyan][cyan] 29[/cyan][cyan] Chicago[/cyan]"
    ]
    
    assert mock_console.output == expected_output, "Table output should match expected output"
```
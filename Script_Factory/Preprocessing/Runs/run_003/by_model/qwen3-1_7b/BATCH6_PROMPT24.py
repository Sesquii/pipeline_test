```python
from rich.console import Console
from rich.progress import Progress, Spinner, Bar
import time

console = Console()

def main():
    current_progress = None
    while True:
        user_input = input("Enter command (help, start, stop, exit): ")
        if user_input == "exit":
            break
        elif user_input == "help":
            console.print("Available commands: help, start, stop, exit")
        elif user_input == "start":
            if current_progress is not None:
                current_progress.stop()
            with Progress(
                Spinner(name="spinner"),
                Bar(),
                Text("Processing..."),
                always=True,
            ) as p:
                task = p.add_task("Starting...", description="Task in progress...")
                time.sleep(5)
        elif user_input == "stop":
            if current_progress is not None:
                current_progress.stop()
                current_progress = None
        else:
            console.print(f"Unknown command: {user_input}")

if __name__ == "__main__":
    main()
import sys
from rich import print as rprint
from rich.progress import track
from rich.spinner import Spinner
from rich.console import Console

# Initialize Rich console
console = Console()


def conversational_cli():
    # Display an initial greeting with a spinner
    spinner = Spinner(text="Welcome to BATCH6 Conversational CLI")
    spinner.spin()

    rprint("[bold magenta]Conversational Command Line Interface[/bold magenta]")
    rprint("This is a simple, interactive command line interface designed for fun.\n")

    # Infinite loop for conversational interaction
    while True:
        user_input = input("\nYou: ").strip().lower()

        if user_input == "quit":
            rprint("[bold red]Goodbye!")
            break

        elif user_input == "help":
            rprint("Available commands:")
            rprint("[bold]quit[/bold]: Exit the program.")
            rprint("[bold]help[/bold]: Show this help message.")
            rprint("[bold]spin[/bold]: Display a spinning text spinner.")

        elif user_input in ["spin"]:
            spinner.text = "Spinning..."
            with console.status[f"Spinning..."] as status:
                for _ in track(range(5)):  # Simulate progress
                    status.text = f"{spinner.text} {int((_) / 4 * 100):<3}% "
                    status.bar_char = '#'
                    status.refresh()

        else:
            rprint(f"Assistant: I'm not sure how to respond to that.")


if __name__ == "__main__":
    conversational_cli()
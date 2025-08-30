# BATCH6_PROMPT21_Granite.py
import click

@click.group()
def cli():
    pass

@cli.command()
def enthusiastic_greeting():
    """An overly enthusiastic welcome message followed by personal questions."""
    
    # Enthusiastic welcome message
    print("\n🤩 WELCOME, BRAVE EXPLORER! 🤩")
    print("I'm thrilled to have you aboard this fantastic journey of self-discovery!")

    # Personal unrelated questions
    print("\nNow, let's dive into some fun facts about you:")
    
    # Asking the user's favorite color
    click.echo("1️⃣ What's your favorite color? It could be as vibrant as a sunflower or as calm as the ocean blue!")

    # Asking the user's favorite food
    click.echo("2️⃣ If you were to choose, what's your all-time favorite food? Something savory, sweet, or spicy?")

    # Asking the user's dream destination
    click.echo("3️⃣ Where in the world would you love to visit one day? Perhaps a bustling city or a serene beach?")

if __name__ == "__main__":
    cli()
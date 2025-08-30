```python
from click import command, prompt, echo

@command()
def main():
    """Conversational CLI that provides enthusiastic welcome and asks personal questions."""
    echo("Hey there! How are you today?!")
    
    # Ask unrelated personal questions
    favorite_color = prompt("What's your favorite color?", type=click.STRING)
    pet_name = prompt("What's the name of your pet?", type=click.STRING)
    favorite_food = prompt("What's your favorite food?", type=click.STRING)
    
    echo(f"Okay, so your favorite color is {favorite_color}, your pet is {pet_name}, and your favorite food is {favorite_food}.")

if __name__ == "__main__":
    main()
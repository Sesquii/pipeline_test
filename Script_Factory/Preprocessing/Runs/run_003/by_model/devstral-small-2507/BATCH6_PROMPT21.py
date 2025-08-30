import click

@click.command()
def enthusiastic_welcome():
    """
    Provides an overly enthusiastic welcome message and asks a series of personal questions.
    """

    # Overly enthusiastic welcome message
    click.echo("🎉 WELCOME! 🎉")
    click.echo("We are absolutely thrilled to have you here!")
    click.echo("Get ready for an amazing experience! 🚀")

    # Asking personal questions
    name = click.prompt('First, could you please tell us your name?')
    age = click.prompt('How old are you?', type=int)
    hobby = click.prompt('What is your favorite hobby?')
    favorite_food = click.prompt('What is your favorite food?')

    # Displaying collected information
    click.echo(f"\nThank you for sharing, {name}!")
    click.echo(f"It's great to know that you are {age} years young.")
    click.echo(f"We love that you enjoy {hobby} in your free time!")
    click.echo(f"And who doesn't love {favorite_food}? It's a classic!")

if __name__ == '__main__':
    enthusiastic_welcome()
import random

# List of predefined insults
INSULTS = [
    "You're about as useful as a screen door on a spaceship.",
    "If laughter is the best medicine, your face must be curing the world.",
    "I'd rather dance with a bear than deal with you.",
    "You're like a candle in the wind... except you're not bright and you're not blowing away.",
    "I've seen people like you on TV, but I never thought they were real.",
    "Your personality is like a light bulb - it's either off or it's screwing everything around it.",
    "You're as welcome as a skunk at a lawn party.",
    "If brains were taxed, you'd get a refund.",
    "I've seen people with your IQ get jobs pushing buttons on vending machines.",
    "You must have been born on a highway, because that's where most accidents happen."
]

def main():
    """Main function to run the conversational CLI."""
    print("Welcome to the Insult Generator! Type anything to get an insult.")
    while True:
        user_input = input("> ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        insult = random.choice(INSULTS)
        print(f"Insult: {insult}\n")

if __name__ == "__main__":
    main()
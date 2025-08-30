import random

# Predefined list of insults
insults = [
    "You're as useful as a screen door on a submarine.",
    "Your intelligence is off-the-charts... low.",
    "You have an ability to annoy everyone you meet, congratulations!",
    "If brains were dynamite, you couldn't blow your nose.",
    "You're about as useful as a chocolate teapot."
]

def generate_insult():
    """Generates a random insult from the list."""
    return random.choice(insults)

def main():
    """Entry point of the program."""
    print("Welcome to the Conversational Command Line Interface!")
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        insult = generate_insult()
        print(f"Assistant: {insult}")

if __name__ == "__main__":
    main()
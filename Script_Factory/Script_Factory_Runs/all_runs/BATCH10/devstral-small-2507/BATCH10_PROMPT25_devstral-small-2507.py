import sys
import random

# List of sarcastic responses
SARCASTIC_RESPONSES = [
    "Well, that was helpful...",
    "I'm sure you put a lot of thought into that.",
    "Brilliant deduction, Sherlock!",
    "Wow, never would have guessed that.",
    "You're on fire with these commands!",
    "Keep going, you're crushing it.",
    "I'm trembling with excitement over here.",
    "That's just... magnificent.",
    "You've truly outdone yourself this time.",
    "I can't even..."
]

def main():
    """
    Main function that runs the conversational command-line tool.
    Responds to each command with a sarcastic remark.
    """
    print("Welcome to the Unhelpful Assistant!")
    print("Type 'exit' to quit.\n")

    while True:
        # Get user input
        user_input = input("> ")

        # Check if user wants to exit
        if user_input.lower() == 'exit':
            print("Finally, something useful.")
            break

        # Respond with a random sarcastic remark
        response = random.choice(SARCASTIC_RESPONSES)
        print(response + "\n")

if __name__ == "__main__":
    main()
# BATCH2_PROMPT15_{model_name}.py

import sys
from time import sleep

def chatty_response(message):
    """Produces a verbose response to user input."""
    return f"Oh, dear human! I've just received your command like a precious gift. " \
           f"You asked for '{message}', and let me tell you, it's as important as the air you breathe!"

def main():
    """Entry point of the program."""
    print("Welcome to the Chatty Command Line Interface!")

    while True:
        user_input = input("\nPlease enter a command (or type 'quit' to exit): ")

        if user_input.lower() == 'quit':
            print("Farewell, dear human! May your journey be as smooth as a marshmallow in hot cocoa.")
            break
        
        response = chatty_response(user_input)
        print(response)
        sleep(1)  # To mimic thinking time

if __name__ == "__main__":
    main()
# BATCH10_PROMPT25_qwen.py

import sys

def sarcastic_response(command):
    # List of unhelpful, sarcastic remarks
    responses = {
        "ls": "Wow, you're looking around? I bet there's nothing interesting here.",
        "cd ..": "Nope, can't go back in time. But hey, you could always pretend!",
        "pwd": "Your current location? You must be lost.",
        "cat file.txt": "Oh, look at that, a text file. I bet it's full of secrets.",
        "echo Hello, World!": "You're saying hello to the world? That's so original.",
        "git status": "No changes here, just more sarcasm waiting for you.",
        "exit": "Fine, have your fun. Maybe next time you'll be a bit less sarcastic."
    }
    
    # Return a sarcastic response if the command is recognized, otherwise return a generic one
    return responses.get(command, "Huh? I didn't understand that command. Try again.")

def main():
    print("Welcome to the Sarcastic Command-Line Tool!")
    while True:
        user_input = input("> ").strip()
        if not user_input:
            continue
        
        # Exit the loop if the user types 'exit'
        if user_input.lower() == "exit":
            break
        
        # Get the sarcastic response for the command
        response = sarcastic_response(user_input)
        print(f"Sarcastic AI: {response}")

if __name__ == "__main__":
    main()
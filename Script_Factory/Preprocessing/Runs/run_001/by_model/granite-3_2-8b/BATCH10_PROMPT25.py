# BATCH10_PROMPT25_SarcasmBot.py

import sys
from time import sleep

def sarcasm(input_command):
    sarcastic_responses = {
        "help": "Oh, sure. Because I'm just dying to assist you.",
        "list": "Absolutely, let me compile a thorough and helpful list for you.",
        "quit": "Fine, if you insist on leaving, don't let the door hit you on your way out."
    }

    return sarcastic_responses.get(input_command, "Huh? I'm not sure how to respond to that.")

def main():
    print("Welcome to SarcasmBot - Your personal source of unhelpfulness!")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("> ").strip()

        if user_input.lower() == "quit":
            print("Good riddance.")
            break

        response = sarcasm(user_input)
        print(f"SarcasmBot: {response}")
        
        # Adding a delay to make it seem like the bot is thinking...
        sleep(1)

if __name__ == "__main__":
    main()
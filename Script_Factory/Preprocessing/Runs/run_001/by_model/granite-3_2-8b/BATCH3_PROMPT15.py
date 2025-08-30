# BATCH3_PROMPT15_Granite.py

import sys

def chatty_response(user_input):
    """
    Generates an overly verbose response to user input.

    Args:
        user_input (str): The command or query entered by the user.

    Returns:
        str: A verbose, unhelpful confirmation message.
    """
    responses = {
        'ls': "I've embarked on a thrilling expedition to unveil the contents of this directory, oh human! Here are the treasures I found:",
        'cd': "In the name of exploration, I shall transport us to the land of your specified directory, dear human!",
        'exit': "Farewell, noble user! May your journey be filled with joy and productivity.",
        'help': "I'm afraid I can't assist you directly, but let me conjure up some generic advice: 'Type help for more information!'",
    }

    return responses.get(user_input, "Your command has been registered, brave user! Prepare for a response that may or may not be useful.")

def main():
    """
    The entry point of the program. It handles user input and generates chatty responses.
    """
    print("Welcome, human friend! I am your overly verbose, slightly unhelpful command line interface. Let's embark on this grand adventure together!")
    
    while True:
        try:
            user_input = input("\nYour humble servant awaits your command: ")

            if user_input.lower() in ['exit', 'quit']:
                print(chatty_response(user_input))
                break
            
            response = chatty_response(user_input)
            print(response)

        except KeyboardInterrupt:
            print("\nOh dear! It seems our adventure has been cut short. Farewell, brave explorer!")
            sys.exit(0)

if __name__ == "__main__":
    main()
import argparse

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Conversational Command Line Interface")

    # Add a chatty, unhelpful confirmation flag
    parser.add_argument('--chatty', action='store_true',
                       help='Enable chatty, unhelpful confirmation messages')

    # Parse the arguments
    args = parser.parse_args()

    # Check if chatty mode is enabled
    if args.chatty:
        print("Oh, you want to be chatty? Okay, let's chat!")
        print("I see you're using the --chatty flag. How interesting.")
        print("Is there something specific you want to talk about?")
        print("Or are we just making small talk here?")

    # If no chatty mode, show normal output
    else:
        print("Hello! Normal mode activated.")

if __name__ == "__main__":
    main()
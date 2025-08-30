import argparse

def main():
    # Create the parser object
    parser = argparse.ArgumentParser(description="A chatty command line interface")

    # Define a flag that triggers a confirmation message
    parser.add_argument(
        "--chatty",
        action="store_true",
        help="Trigger a chatty, unhelpful confirmation message"
    )

    # Parse the arguments
    args = parser.parse_args()

    # Check if the chatty flag was provided and respond accordingly
    if args.chatty:
        print("Oh, you want to be chatty? Well, I'm here to chat!")
        print("How about we start with... what's your favorite color?")

if __name__ == "__main__":
    main()
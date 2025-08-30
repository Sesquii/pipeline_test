import argparse

def confirm_unhelpfully(message):
    """Unhelpful confirmation message."""
    responses = [
        "Sure, why not?",
        "Absolutely, go for it!",
        "You bet your sweet bippy.",
        "Fine by me, old sport.",
        "Sounds like a plan, chum.",
        "If you say so.",
        "Your wish is my command.",
        "I'm on it, boss.",
    ]
    return responses[len(responses) // 2]

def main():
    parser = argparse.ArgumentParser(description='Conversational Command Line Interface')
    parser.add_argument('--unhelpful', action='store_true', help='Trigger an unhelpful confirmation message.')
    args = parser.parse_args()

    if args.unhelpful:
        print("You've invoked the unhelpful mode...")
        print(confirm_unhelpfully('Are you sure you want to proceed?'))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
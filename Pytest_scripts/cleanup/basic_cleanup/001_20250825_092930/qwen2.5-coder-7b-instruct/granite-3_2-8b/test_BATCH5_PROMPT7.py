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

# ===== GENERATED TESTS =====
import pytest
from argparse import Namespace

# Original script remains unchanged

def test_confirm_unhelpfully():
    """Test the confirm_unhelpfully function."""
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
    # Test that the function returns one of the predefined responses
    assert confirm_unhelpfully('Are you sure you want to proceed?') in responses

def test_main_help_mode(capsys):
    """Test the main function when no arguments are provided."""
    # Call the main function without any arguments
    main()
    # Capture the output
    captured = capsys.readouterr()
    # Check that the help message is printed
    assert "usage:" in captured.out

def test_main_unhelpful_mode(capsys):
    """Test the main function when --unhelpful argument is provided."""
    # Call the main function with --unhelpful argument
    main(Namespace(unhelpful=True))
    # Capture the output
    captured = capsys.readouterr()
    # Check that the unhelpful message is printed
    assert "You've invoked the unhelpful mode..." in captured.out
    # Check that the confirm_unhelpfully function is called
    assert confirm_unhelpfully('Are you sure you want to proceed?') in captured.out

# Add more test cases as needed

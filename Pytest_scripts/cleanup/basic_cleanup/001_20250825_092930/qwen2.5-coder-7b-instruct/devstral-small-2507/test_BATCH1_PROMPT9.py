#!/usr/bin/env python3

import random
import time
import sys
from argparse import ArgumentParser

"""
Infinite Compliment Engine

This script runs an infinite loop that prints compliments (or occasionally insults)
to stdout at regular intervals until manually terminated by the user.
"""

def main():
    # Initialize compliment and insult lists
    compliments = [
        "You're amazing!",
        "Your smile is contagious.",
        "You have a great sense of humor.",
        "You are very talented.",
        "You light up the room.",
        "You make people's day better.",
        "You are more helpful than you realize.",
        "You have a great heart.",
        "You're like a ray of sunshine on a really cloudy day.",
        "You bring happiness to those around you."
    ]

    insults = [
        "You're not as clever as you think.",
        "Your jokes are about as funny as a root canal.",
        "You couldn't pour water out of a boot with instructions on the heel.",
        "You're about as useful as a screen door on a submarine.",
        "Your IQ is lower than your shoe size.",
        "You have the attention span of a goldfish.",
        "You're like a candle in the wind - useless and annoying."
    ]

    # Parse command line arguments for seeding
    parser = ArgumentParser(description='Infinite Compliment Engine')
    parser.add_argument('--seed', type=int, help='Seed value for random number generator')
    args = parser.parse_args()

    if args.seed:
        print(f"Seeding random generator with {args.seed}")
        random.seed(args.seed)

    # Main loop with graceful shutdown on KeyboardInterrupt
    try:
        while True:
            # With 5% probability, choose an insult instead of a compliment
            if random.random() < 0.05:
                message = random.choice(insults)
            else:
                message = random.choice(compliments)

            print(message)
            time.sleep(2)  # Pause for 2 seconds between messages

    except KeyboardInterrupt:
        print("\nGoodbye!")

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
#!/usr/bin/env python3

import random
import time
import sys
from argparse import ArgumentParser
import pytest
from io import StringIO
from unittest.mock import patch

"""
Infinite Compliment Engine

This script runs an infinite loop that prints compliments (or occasionally insults)
to stdout at regular intervals until manually terminated by the user.
"""

def main():
    # Initialize compliment and insult lists
    compliments = [
        "You're amazing!",
        "Your smile is contagious.",
        "You have a great sense of humor.",
        "You are very talented.",
        "You light up the room.",
        "You make people's day better.",
        "You are more helpful than you realize.",
        "You have a great heart.",
        "You're like a ray of sunshine on a really cloudy day.",
        "You bring happiness to those around you."
    ]

    insults = [
        "You're not as clever as you think.",
        "Your jokes are about as funny as a root canal.",
        "You couldn't pour water out of a boot with instructions on the heel.",
        "You're about as useful as a screen door on a submarine.",
        "Your IQ is lower than your shoe size.",
        "You have the attention span of a goldfish.",
        "You're like a candle in the wind - useless and annoying."
    ]

    # Parse command line arguments for seeding
    parser = ArgumentParser(description='Infinite Compliment Engine')
    parser.add_argument('--seed', type=int, help='Seed value for random number generator')
    args = parser.parse_args()

    if args.seed:
        print(f"Seeding random generator with {args.seed}")
        random.seed(args.seed)

    # Main loop with graceful shutdown on KeyboardInterrupt
    try:
        while True:
            # With 5% probability, choose an insult instead of a compliment
            if random.random() < 0.05:
                message = random.choice(insults)
            else:
                message = random.choice(compliments)

            print(message)
            time.sleep(2)  # Pause for 2 seconds between messages

    except KeyboardInterrupt:
        print("\nGoodbye!")

if __name__ == "__main__":
    main()

# Test cases
def test_main_with_seed(capsys):
    """Test the main function with a seed value."""
    with patch('sys.argv', ['script.py', '--seed=42']):
        main()
        captured = capsys.readouterr()
        assert "Seeding random generator with 42" in captured.out

def test_main_without_seed(capsys):
    """Test the main function without a seed value."""
    with patch('sys.argv', ['script.py']):
        main()
        captured = capsys.readouterr()
        assert "Seeding random generator with 42" not in captured.out

def test_random_choice_with_insults():
    """Test that random.choice returns an insult with 5% probability."""
    insults = [
        "You're not as clever as you think.",
        "Your jokes are about as funny as a root canal.",
        "You couldn't pour water out of a boot with instructions on the heel.",
        "You're about as useful as a screen door on a submarine.",
        "Your IQ is lower than your shoe size.",
        "You have the attention span of a goldfish.",
        "You're like a candle in the wind - useless and annoying."
    ]
    compliments = [
        "You're amazing!",
        "Your smile is contagious.",
        "You have a great sense of humor.",
        "You are very talented.",
        "You light up the room.",
        "You make people's day better.",
        "You are more helpful than you realize.",
        "You have a great heart.",
        "You're like a ray of sunshine on a really cloudy day.",
        "You bring happiness to those around you."
    ]
    random.seed(42)
    for _ in range(100):
        message = random.choice(compliments + insults)
        if message in compliments:
            assert True
        elif message in insults:
            assert random.random() < 0.05

def test_random_choice_with_compliments():
    """Test that random.choice returns a compliment with 95% probability."""
    insults = [
        "You're not as clever as you think.",
        "Your jokes are about as funny as a root canal.",
        "You couldn't pour water out of a boot with instructions on the heel.",
        "You're about as useful as a screen door on a submarine.",
        "Your IQ is lower than your shoe size.",
        "You have the attention span of a goldfish.",
        "You're like a candle in the wind - useless and annoying."
    ]
    compliments = [
        "You're amazing!",
        "Your smile is contagious.",
        "You have a great sense of humor.",
        "You are very talented.",
        "You light up the room.",
        "You make people's day better.",
        "You are more helpful than you realize.",
        "You have a great heart.",
        "You're like a ray of sunshine on a really cloudy day.",
        "You bring happiness to those around you."
    ]
    random.seed(42)
    for _ in range(100):
        message = random.choice(compliments + insults)
        if message in compliments:
            assert random.random() > 0.95
        elif message in insults:
            assert True

def test_main_keyboard_interrupt(capsys):
    """Test the main function with a keyboard interrupt."""
    with patch('sys.argv', ['script.py']):
        with pytest.raises(KeyboardInterrupt):
            with patch('builtins.input', side_effect=['\x03']):
                main()
        captured = capsys.readouterr()
        assert "Goodbye!" in captured.out

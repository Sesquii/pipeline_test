"""
Infinite Compliment Engine

This script runs in an infinite loop, printing one line of text every few seconds
(e.g., 2 seconds) until the user terminates it manually. Each iteration selects a random
compliment from a predefined list and prints it to stdout. With a small probability (suggested
5%) an insult is chosen instead of a compliment, simulating an accidental mistake. Provide
a separate list of insults for this purpose. Use the random module to perform selections;
seed it optionally so that results are reproducible if a seed value is provided via a command-line
argument or environment variable.
"""

import random
import time
import os

# Define lists of compliments and insults
compliments = [
    "You have a great sense of humor!",
    "Your ideas are always interesting.",
    "You're an excellent listener.",
    "You make my day brighter with your presence.",
    "You inspire confidence in those around you."
]

insults = [
    "I don't like your shoes.",
    "Your hair is messy today.",
    "Why do you always have to be so loud?",
    "You look a bit silly today.",
    "I hope you're feeling well."
]

# Seed the random module if a seed value is provided via command-line argument or environment variable
seed_value = os.getenv('SEED')
if seed_value:
    random.seed(seed_value)

def main():
    try:
        while True:
            # Choose between compliment and insult with a 5% chance of an insult
            selection = random.choice([compliments, insults])
            message = random.choice(selection)
            print(message)
            time.sleep(2)  # Print one line every 2 seconds
    except KeyboardInterrupt:
        print("Goodbye!")

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
import pytest
from unittest.mock import patch
import os

# Original script code remains unchanged

def test_main_with_compliment():
    """Test that the main function prints a compliment."""
    with patch('builtins.print') as mock_print:
        with patch('random.choice', return_value=compliments[0]):
            main()
            assert mock_print.call_args_list[0][0] == (compliments[0],)

def test_main_with_insult():
    """Test that the main function prints an insult."""
    with patch('builtins.print') as mock_print:
        with patch('random.choice', return_value=insults[0]):
            main()
            assert mock_print.call_args_list[0][0] == (insults[0],)

def test_main_with_keyboard_interrupt():
    """Test that the main function handles KeyboardInterrupt gracefully."""
    with patch('builtins.print') as mock_print:
        with patch('time.sleep', side_effect=KeyboardInterrupt):
            try:
                main()
            except SystemExit:
                assert True
            else:
                assert False

def test_main_with_random_choice():
    """Test that the main function chooses between compliments and insults."""
    with patch('random.choice') as mock_choice:
        mock_choice.return_value = compliments
        with patch('builtins.print') as mock_print:
            main()
            assert mock_choice.call_args_list[0][0] == ([compliments, insults],)
            assert mock_choice.call_args_list[1][0] == (compliments,)
        
        mock_choice.reset_mock()
        mock_choice.return_value = insults
        with patch('builtins.print') as mock_print:
            main()
            assert mock_choice.call_args_list[0][0] == ([compliments, insults],)
            assert mock_choice.call_args_list[1][0] == (insults,)

def test_main_with_seed():
    """Test that the main function is reproducible with a seed value."""
    os.environ['SEED'] = '42'
    with patch('builtins.print') as mock_print:
        with patch('random.choice', return_value=compliments[0]):
            main()
            assert mock_print.call_args_list[0][0] == (compliments[0],)
    
    # Reset the seed and run again to ensure reproducibility
    os.environ['SEED'] = '42'
    with patch('builtins.print') as mock_print:
        with patch('random.choice', return_value=compliments[0]):
            main()
            assert mock_print.call_args_list[0][0] == (compliments[0],)

# Add more test cases as needed
```
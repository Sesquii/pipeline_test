# BATCH10_PROMPT3_Devstral.py

import time
import sys

def create_hologram(text):
    """
    Creates a simple text-based hologram effect by displaying the text
    with a fading in and out animation.

    Args:
        text (str): The input string to display as a hologram.
    """
    frames = [
        "  ",
        " *",
        "**",
        " *",
        "  "
    ]

    try:
        while True:
            for frame in frames:
                # Clear the console
                if sys.platform.startswith('win'):
                    print("\033[2J\033[H", end='')
                else:
                    print("\033[2J\033[H", end='')

                # Display the current frame of the hologram
                for char in text:
                    index = frames.index(frame) if len(frame) > 1 else 0
                    display_char = frame[index] if index < len(frame) else " "
                    print(f"{display_char}{char}", end=" ")
                print()

                # Small delay between frames
                time.sleep(0.2)

    except KeyboardInterrupt:
        # Allow graceful exit on Ctrl+C
        print("\nHologram display stopped.")

if __name__ == "__main__":
    # Example usage
    input_text = "Hello, Hologram!"
    create_hologram(input_text)

# ===== GENERATED TESTS =====
# BATCH10_PROMPT3_Devstral.py

import time
import sys
from unittest.mock import patch
import pytest

def create_hologram(text):
    """
    Creates a simple text-based hologram effect by displaying the text
    with a fading in and out animation.

    Args:
        text (str): The input string to display as a hologram.
    """
    frames = [
        "  ",
        " *",
        "**",
        " *",
        "  "
    ]

    try:
        while True:
            for frame in frames:
                # Clear the console
                if sys.platform.startswith('win'):
                    print("\033[2J\033[H", end='')
                else:
                    print("\033[2J\033[H", end='')

                # Display the current frame of the hologram
                for char in text:
                    index = frames.index(frame) if len(frame) > 1 else 0
                    display_char = frame[index] if index < len(frame) else " "
                    print(f"{display_char}{char}", end=" ")
                print()

                # Small delay between frames
                time.sleep(0.2)

    except KeyboardInterrupt:
        # Allow graceful exit on Ctrl+C
        print("\nHologram display stopped.")

if __name__ == "__main__":
    # Example usage
    input_text = "Hello, Hologram!"
    create_hologram(input_text)


# Test suite for BATCH10_PROMPT3_Devstral.py

def test_create_hologram_positive():
    """
    Tests the create_hologram function with a positive input.
    """
    with patch('time.sleep') as mock_sleep:
        with patch('sys.stdout.write') as mock_write:
            create_hologram("Test")
            assert mock_write.call_count == 5 * len("Test") + 10
            mock_sleep.assert_called_with(0.2)

def test_create_hologram_negative():
    """
    Tests the create_hologram function with a negative input.
    """
    with patch('time.sleep') as mock_sleep:
        with patch('sys.stdout.write') as mock_write:
            create_hologram("")
            assert mock_write.call_count == 5
            mock_sleep.assert_called_with(0.2)

def test_create_hologram_keyboard_interrupt():
    """
    Tests the create_hologram function with a KeyboardInterrupt.
    """
    with patch('time.sleep', side_effect=KeyboardInterrupt):
        with patch('sys.stdout.write') as mock_write:
            create_hologram("Test")
            assert mock_write.call_count == 5 * len("Test") + 10

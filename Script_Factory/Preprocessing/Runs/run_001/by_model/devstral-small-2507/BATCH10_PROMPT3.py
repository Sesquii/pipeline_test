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
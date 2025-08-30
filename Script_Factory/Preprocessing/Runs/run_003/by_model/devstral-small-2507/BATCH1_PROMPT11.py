# ai_mood_ring.py - A simple mood ring simulator for the terminal

import time
import random
import sys

# ANSI escape codes for colors
COLORS = [
    "\033[41m",  # Red background  
    "\033[42m",  # Green background
    "\033[43m",  # Yellow background
    "\033[44m",  # Blue background
    "\033[45m",  # Magenta background
    "\033[46m",  # Cyan background
    "\033[47m"   # White background
]

def clear_screen():
    """Clear the terminal screen"""
    print("\033[2J", end="")

def set_random_color():
    """Set a random background color"""
    color = random.choice(COLORS)
    print(f"{color}", end="")
    sys.stdout.flush()

def reset_color():
    """Reset the terminal color to default"""
    print("\033[0m", end="")
    sys.stdout.flush()

def main():
    try:
        while True:
            clear_screen()
            set_random_color()
            # Print some text to make the color change visible
            print("AI Mood Ring - Press Ctrl+C to exit")
            time.sleep(2)  # Change color every 2 seconds
            reset_color()
            clear_screen()
    except KeyboardInterrupt:
        # Reset terminal on exit
        reset_color()
        print("\nAI mood ring stopped. Goodbye!")

if __name__ == "__main__":
    main()
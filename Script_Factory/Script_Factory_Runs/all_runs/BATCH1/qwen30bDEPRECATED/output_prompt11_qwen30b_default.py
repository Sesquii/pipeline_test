#!/usr/bin/env python3
"""
AI Mood Ring - Simulates AI mood swings with random console background color changes
"""

import random
import time
import signal
import sys

def clear_screen():
    """Clear the terminal screen using ANSI escape codes"""
    print("\033[2J\033[H", end="")

def set_background_color(color_code):
    """
    Set the terminal background color using ANSI escape codes
    
    Args:
        color_code (str): ANSI color code for background
    """
    print(f"\033[{color_code}m", end="")

def get_random_background_color():
    """
    Generate a random background color code from a set of ANSI colors
    
    Returns:
        str: ANSI background color code
    """
    # ANSI background color codes (40-47 are standard colors)
    background_colors = [
        "40",  # Black
        "41",  # Red
        "42",  # Green
        "43",  # Yellow
        "44",  # Blue
        "45",  # Magenta
        "46",  # Cyan
        "47",  # White
        "100", # Bright Black
        "101", # Bright Red
        "102", # Bright Green
        "103", # Bright Yellow
        "104", # Bright Blue
        "105", # Bright Magenta
        "106", # Bright Cyan
        "107"  # Bright White
    ]
    
    return random.choice(background_colors)

def signal_handler(sig, frame):
    """
    Handle Ctrl+C interruption to exit gracefully
    
    Args:
        sig (int): Signal number
        frame: Current stack frame
    """
    print("\nExiting AI Mood Ring simulation...")
    # Reset terminal colors before exiting
    print("\033[0m", end="")
    sys.exit(0)

def main():
    """
    Main function to run the AI Mood Ring simulation
    """
    # Register signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    
    # Clear screen and set initial background
    clear_screen()
    current_color = get_random_background_color()
    set_background_color(current_color)
    
    print("AI Mood Ring Simulation Started!")
    print("Press Ctrl+C to exit")
    print("=" * 30)
    
    try:
        while True:
            # Wait for a random time between 2 and 5 seconds
            wait_time = random.uniform(2, 5)
            time.sleep(wait_time)
            
            # Get new random background color
            new_color = get_random_background_color()
            
            # Change the background color
            set_background_color(new_color)
            
            # Print a message to indicate mood change
            print(f"AI Mood Changed! New color: {new_color}")
            
    except KeyboardInterrupt:
        # Handle interruption gracefully
        print("\nExiting AI Mood Ring simulation...")
        print("\033[0m", end="")  # Reset colors

if __name__ == "__main__":
    main()

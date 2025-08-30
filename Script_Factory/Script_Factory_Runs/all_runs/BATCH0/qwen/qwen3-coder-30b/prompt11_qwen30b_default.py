#!/usr/bin/env python3
"""
AI Mood Ring - Simulates AI mood swings with random console background colors
"""

import random
import time
import signal
import sys

# ANSI escape codes for background colors (256-color mode)
BACKGROUND_COLORS = [
    40,  # Black
    41,  # Red
    42,  # Green
    43,  # Yellow
    44,  # Blue
    45,  # Magenta
    46,  # Cyan
    47,  # White
    100, # Bright Black
    101, # Bright Red
    102, # Bright Green
    103, # Bright Yellow
    104, # Bright Blue
    105, # Bright Magenta
    106, # Bright Cyan
    107  # Bright White
]

def clear_screen():
    """Clear the terminal screen and move cursor to top-left"""
    print("\033[2J\033[H", end="")

def set_background_color(color_code):
    """Set the background color using ANSI escape code"""
    print(f"\033[{color_code}m", end="")

def reset_colors():
    """Reset all terminal colors to default"""
    print("\033[0m", end="")

def signal_handler(sig, frame):
    """Handle Ctrl+C interruption gracefully"""
    reset_colors()
    print("\nAI Mood Ring shutting down...")
    sys.exit(0)

def main():
    """Main function to run the AI mood ring simulation"""
    # Register signal handler for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    
    # Clear screen and set initial state
    clear_screen()
    print("AI Mood Ring Activated!")
    print("Press Ctrl+C to exit")
    print("-" * 30)
    
    try:
        while True:
            # Choose a random background color
            color = random.choice(BACKGROUND_COLORS)
            
            # Set the background color
            set_background_color(color)
            
            # Wait for a random time between 1 and 5 seconds
            wait_time = random.randint(1, 5)
            time.sleep(wait_time)
            
    except KeyboardInterrupt:
        # Handle interruption gracefully
        reset_colors()
        print("\nAI Mood Ring shutting down...")

if __name__ == "__main__":
    main()

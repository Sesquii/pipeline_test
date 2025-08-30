#!/usr/bin/env python3

import time
import random

# ANSI escape codes for setting background color
COLORS = {
    'black': '\033[40m',
    'red': '\033[41m',
    'green': '\033[42m',
    'yellow': '\033[43m',
    'blue': '\033[44m',
    'magenta': '\033[45m',
    'cyan': '\033[46m',
    'white': '\033[47m'
}

# ANSI escape code to reset background color
RESET = '\033[0m'

def clear_console():
    """Clears the console screen."""
    print('\033[H\033[J', end='')

def set_random_color():
    """Sets a random background color."""
    # Get a random color from the COLORS dictionary
    color = random.choice(list(COLORS.values()))
    print(color, end='')

def main():
    clear_console()
    while True:
        set_random_color()
        time.sleep(2)  # Change color every 2 seconds

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(RESET)  # Reset the background color when interrupted
        print("Program terminated by user.")
```

### Explanation:

1. **Import Statements**:
   - `time`: To add delays.
   - `random`: To select random colors.

2. **COLORS Dictionary**:
   - Contains ANSI escape codes for setting different background colors. The keys are color names and the values are the corresponding escape codes.

3. **RESET Variable**:
   - Stores the ANSI escape code to reset the background color to default.

4. **clear_console Function**:
   - Clears the console screen using `\033[H\033[J`.

5. **set_random_color Function**:
   - Selects a random color from the `COLORS` dictionary and prints it, which changes the background color of the console.

6. **main Function**:
   - Calls `clear_console()` to clear the screen.
   - Runs an infinite loop where it sets a random color every 2 seconds using `set_random_color()`.
   
7. **try-except Block**:
   - Handles `KeyboardInterrupt` (Ctrl+C) to reset the background color and print a termination message before exiting.

This program will run indefinitely, changing the background color of the console randomly every few seconds until interrupted by the user.
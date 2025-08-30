import time
import random
import sys

def change_console_color():
    """Function to change console background color using ANSI escape codes."""
    colors = ['30', '31', '32', '33', '34', '35', '36', '37']  # Dark gray to white
    random_color = random.choice(colors) + ';40'  # Adding 40 for background color
    print('\033[' + random_color + 'm', end='')

def main():
    """Main function to run the AI mood ring."""
    try:
        while True:
            change_console_color()
            time.sleep(2)  # Change color every 2 seconds
    except KeyboardInterrupt:
        print('\033[0m' * 100, end='')  # Reset all colors on interrupt

if __name__ == "__main__":
    main()
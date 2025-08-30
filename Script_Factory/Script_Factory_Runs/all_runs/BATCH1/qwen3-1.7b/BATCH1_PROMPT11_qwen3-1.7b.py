```python
import random
import time

try:
    while True:
        # Generate a random RGB color for the background
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        
        # Create ANSI escape code to set the background color
        color_code = f"\033[48;2;{r};{g};{b}\033[0m"
        
        # Print the color code to change the background of the console
        print(color_code)
        
        # Wait for a few seconds before changing again
        time.sleep(5)
except KeyboardInterrupt:
    print("\nProgram interrupted by Ctrl+C.")
    exit()
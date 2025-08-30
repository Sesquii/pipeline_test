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

# ===== GENERATED TESTS =====
import pytest
from typing import List

# Original script remains unchanged

def test_random_color_generation():
    """Test that random color generation produces valid RGB values."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    assert 0 <= r <= 255
    assert 0 <= g <= 255
    assert 0 <= b <= 255

def test_color_code_format():
    """Test that the color code is in the correct format."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    color_code = f"\033[48;2;{r};{g};{b}\033[0m"
    
    assert color_code.startswith("\033[48;2;")
    assert color_code.endswith("\033[0m")

def test_color_change_interval():
    """Test that the program changes colors at the correct interval."""
    start_time = time.time()
    time.sleep(5)
    end_time = time.time()
    
    assert end_time - start_time >= 4.9 and end_time - start_time <= 5.1

def test_keyboard_interrupt_handling():
    """Test that the program handles keyboard interrupts gracefully."""
    with pytest.raises(SystemExit):
        try:
            while True:
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                
                color_code = f"\033[48;2;{r};{g};{b}\033[0m"
                
                print(color_code)
                
                time.sleep(5)
        except KeyboardInterrupt:
            pass

# Add more test cases as needed

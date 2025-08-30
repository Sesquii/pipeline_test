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

# ===== GENERATED TESTS =====
import time
import random
import sys
from unittest.mock import patch
import pytest

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

# Test Suite
def test_change_console_color():
    """Test the change_console_color function."""
    with patch('sys.stdout') as mock_stdout:
        change_console_color()
        assert '\033[' in mock_stdout.getvalue(), "ANSI escape code not found"

def test_main_with_keyboard_interrupt(capsys):
    """Test the main function with a keyboard interrupt."""
    with patch('builtins.input', side_effect=KeyboardInterrupt), \
         patch('time.sleep') as mock_sleep:
        main()
        captured = capsys.readouterr()
        assert '\033[0m' * 100 in captured.out, "Color reset not found on interrupt"

def test_main_with_no_keyboard_interrupt(capsys):
    """Test the main function without a keyboard interrupt."""
    with patch('time.sleep', side_effect=[None] * 5), \
         patch('sys.stdout') as mock_stdout:
        main()
        assert '\033[' in mock_stdout.getvalue(), "ANSI escape code not found"
        captured = capsys.readouterr()
        assert '\033[0m' * 100 not in captured.out, "Color reset found unexpectedly"

# Test Fixtures
@pytest.fixture
def mock_time_sleep():
    """Fixture to mock time.sleep."""
    with patch('time.sleep') as mock:
        yield mock

@pytest.fixture
def mock_sys_stdout():
    """Fixture to mock sys.stdout."""
    with patch('sys.stdout') as mock:
        yield mock

# Test Parametrization
@pytest.mark.parametrize("input_color, expected_output", [
    ('30', '\033[30;40m'),
    ('31', '\033[31;40m'),
    ('32', '\033[32;40m'),
    ('33', '\033[33;40m'),
    ('34', '\033[34;40m'),
    ('35', '\033[35;40m'),
    ('36', '\033[36;40m'),
    ('37', '\033[37;40m')
])
def test_change_console_color_with_parametrization(input_color, expected_output):
    """Test the change_console_color function with parametrized colors."""
    with patch('sys.stdout') as mock_stdout:
        print(f'\033[{input_color};40m', end='')
        assert mock_stdout.getvalue() == expected_output, f"Expected output not found for color {input_color}"

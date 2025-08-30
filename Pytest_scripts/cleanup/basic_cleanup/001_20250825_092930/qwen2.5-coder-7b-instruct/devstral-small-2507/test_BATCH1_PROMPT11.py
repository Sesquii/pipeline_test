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

# ===== GENERATED TESTS =====
# ai_mood_ring.py - A simple mood ring simulator for the terminal

import time
import random
import sys
from unittest.mock import patch, MagicMock
import pytest

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

# Test suite for ai_mood_ring.py

def test_clear_screen(mocker):
    """Test the clear_screen function"""
    mocker.patch('sys.stdout.write')
    clear_screen()
    sys.stdout.write.assert_called_once_with("\033[2J", end="")

def test_set_random_color(mocker):
    """Test the set_random_color function"""
    mocker.patch('random.choice', return_value="\033[41m")
    mocker.patch('sys.stdout.write')
    set_random_color()
    sys.stdout.write.assert_called_once_with("\033[41m", end="")

def test_reset_color(mocker):
    """Test the reset_color function"""
    mocker.patch('sys.stdout.write')
    reset_color()
    sys.stdout.write.assert_called_once_with("\033[0m", end="")

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_no_keyboard_interrupt(mock_sleep, capsys):
    """Test the main function without keyboard interrupt"""
    with patch('ai_mood_ring.input') as mock_input:
        mock_input.return_value = 'q'
        ai_mood_ring.main()
        captured = capsys.readouterr()
        assert "AI Mood Ring - Press Ctrl+C to exit" in captured.out
        assert "\nAI mood ring stopped. Goodbye!" in captured.out

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_keyboard_interrupt(mock_sleep, capsys):
    """Test the main function with keyboard interrupt"""
    with patch('builtins.input') as mock_input:
        mock_input.side_effect = KeyboardInterrupt
        ai_mood_ring.main()
        captured = capsys.readouterr()
        assert "\nAI mood ring stopped. Goodbye!" in captured.out

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_no_color_change(mock_sleep, capsys):
    """Test the main function with no color change"""
    with patch('random.choice', side_effect=["\033[41m", "\033[42m"] * 5):
        ai_mood_ring.main()
        captured = capsys.readouterr()
        assert "AI Mood Ring - Press Ctrl+C to exit" in captured.out
        assert "\nAI mood ring stopped. Goodbye!" not in captured.out

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_with_color_change(mock_sleep, capsys):
    """Test the main function with color change"""
    with patch('random.choice', side_effect=["\033[41m", "\033[42m"] * 5):
        ai_mood_ring.main()
        captured = capsys.readouterr()
        assert "AI Mood Ring - Press Ctrl+C to exit" in captured.out
        assert "\nAI mood ring stopped. Goodbye!" not in captured.out

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_with_keyboard_interrupt_and_color_change(mock_sleep, capsys):
    """Test the main function with keyboard interrupt and color change"""
    with patch('builtins.input') as mock_input:
        mock_input.side_effect = KeyboardInterrupt
        ai_mood_ring.main()
        captured = capsys.readouterr()
        assert "\nAI mood ring stopped. Goodbye!" in captured.out

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_with_keyboard_interrupt_and_no_color_change(mock_sleep, capsys):
    """Test the main function with keyboard interrupt and no color change"""
    with patch('builtins.input') as mock_input:
        mock_input.side_effect = KeyboardInterrupt
        ai_mood_ring.main()
        captured = capsys.readouterr()
        assert "\nAI mood ring stopped. Goodbye!" in captured.out

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_with_keyboard_interrupt_and_random_color(mock_sleep, capsys):
    """Test the main function with keyboard interrupt and random color"""
    with patch('random.choice', side_effect=["\033[41m", "\033[42m"] * 5):
        ai_mood_ring.main()
        captured = capsys.readouterr()
        assert "AI Mood Ring - Press Ctrl+C to exit" in captured.out
        assert "\nAI mood ring stopped. Goodbye!" not in captured.out

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_with_keyboard_interrupt_and_no_random_color(mock_sleep, capsys):
    """Test the main function with keyboard interrupt and no random color"""
    with patch('random.choice', side_effect=["\033[41m", "\033[42m"] * 5):
        ai_mood_ring.main()
        captured = capsys.readouterr()
        assert "AI Mood Ring - Press Ctrl+C to exit" in captured.out
        assert "\nAI mood ring stopped. Goodbye!" not in captured.out

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_with_keyboard_interrupt_and_random_color_change(mock_sleep, capsys):
    """Test the main function with keyboard interrupt and random color change"""
    with patch('random.choice', side_effect=["\033[41m", "\033[42m"] * 5):
        ai_mood_ring.main()
        captured = capsys.readouterr()
        assert "AI Mood Ring - Press Ctrl+C to exit" in captured.out
        assert "\nAI mood ring stopped. Goodbye!" not in captured.out

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_with_keyboard_interrupt_and_no_random_color_change(mock_sleep, capsys):
    """Test the main function with keyboard interrupt and no random color change"""
    with patch('random.choice', side_effect=["\033[41m", "\033[42m"] * 5):
        ai_mood_ring.main()
        captured = capsys.readouterr()
        assert "AI Mood Ring - Press Ctrl+C to exit" in captured.out
        assert "\nAI mood ring stopped. Goodbye!" not in captured.out

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_with_keyboard_interrupt_and_random_color_change(mock_sleep, capsys):
    """Test the main function with keyboard interrupt and random color change"""
    with patch('random.choice', side_effect=["\033[41m", "\033[42m"] * 5):
        ai_mood_ring.main()
        captured = capsys.readouterr()
        assert "AI Mood Ring - Press Ctrl+C to exit" in captured.out
        assert "\nAI mood ring stopped. Goodbye!" not in captured.out

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_with_keyboard_interrupt_and_no_random_color_change(mock_sleep, capsys):
    """Test the main function with keyboard interrupt and no random color change"""
    with patch('random.choice', side_effect=["\033[41m", "\033[42m"] * 5):
        ai_mood_ring.main()
        captured = capsys.readouterr()
        assert "AI Mood Ring - Press Ctrl+C to exit" in captured.out
        assert "\nAI mood ring stopped. Goodbye!" not in captured.out

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_with_keyboard_interrupt_and_random_color_change(mock_sleep, capsys):
    """Test the main function with keyboard interrupt and random color change"""
    with patch('random.choice', side_effect=["\033[41m", "\033[42m"] * 5):
        ai_mood_ring.main()
        captured = capsys.readouterr()
        assert "AI Mood Ring - Press Ctrl+C to exit" in captured.out
        assert "\nAI mood ring stopped. Goodbye!" not in captured.out

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_with_keyboard_interrupt_and_no_random_color_change(mock_sleep, capsys):
    """Test the main function with keyboard interrupt and no random color change"""
    with patch('random.choice', side_effect=["\033[41m", "\033[42m"] * 5):
        ai_mood_ring.main()
        captured = capsys.readouterr()
        assert "AI Mood Ring - Press Ctrl+C to exit" in captured.out
        assert "\nAI mood ring stopped. Goodbye!" not in captured.out

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_with_keyboard_interrupt_and_random_color_change(mock_sleep, capsys):
    """Test the main function with keyboard interrupt and random color change"""
    with patch('random.choice', side_effect=["\033[41m", "\033[42m"] * 5):
        ai_mood_ring.main()
        captured = capsys.readouterr()
        assert "AI Mood Ring - Press Ctrl+C to exit" in captured.out
        assert "\nAI mood ring stopped. Goodbye!" not in captured.out

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_with_keyboard_interrupt_and_no_random_color_change(mock_sleep, capsys):
    """Test the main function with keyboard interrupt and no random color change"""
    with patch('random.choice', side_effect=["\033[41m", "\033[42m"] * 5):
        ai_mood_ring.main()
        captured = capsys.readouterr()
        assert "AI Mood Ring - Press Ctrl+C to exit" in captured.out
        assert "\nAI mood ring stopped. Goodbye!" not in captured.out

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_with_keyboard_interrupt_and_random_color_change(mock_sleep, capsys):
    """Test the main function with keyboard interrupt and random color change"""
    with patch('random.choice', side_effect=["\033[41m", "\033[42m"] * 5):
        ai_mood_ring.main()
        captured = capsys.readouterr()
        assert "AI Mood Ring - Press Ctrl+C to exit" in captured.out
        assert "\nAI mood ring stopped. Goodbye!" not in captured.out

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_with_keyboard_interrupt_and_no_random_color_change(mock_sleep, capsys):
    """Test the main function with keyboard interrupt and no random color change"""
    with patch('random.choice', side_effect=["\033[41m", "\033[42m"] * 5):
        ai_mood_ring.main()
        captured = capsys.readouterr()
        assert "AI Mood Ring - Press Ctrl+C to exit" in captured.out
        assert "\nAI mood ring stopped. Goodbye!" not in captured.out

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_with_keyboard_interrupt_and_random_color_change(mock_sleep, capsys):
    """Test the main function with keyboard interrupt and random color change"""
    with patch('random.choice', side_effect=["\033[41m", "\033[42m"] * 5):
        ai_mood_ring.main()
        captured = capsys.readouterr()
        assert "AI Mood Ring - Press Ctrl+C to exit" in captured.out
        assert "\nAI mood ring stopped. Goodbye!" not in captured.out

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_with_keyboard_interrupt_and_no_random_color_change(mock_sleep, capsys):
    """Test the main function with keyboard interrupt and no random color change"""
    with patch('random.choice', side_effect=["\033[41m", "\033[42m"] * 5):
        ai_mood_ring.main()
        captured = capsys.readouterr()
        assert "AI Mood Ring - Press Ctrl+C to exit" in captured.out
        assert "\nAI mood ring stopped. Goodbye!" not in captured.out

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_with_keyboard_interrupt_and_random_color_change(mock_sleep, capsys):
    """Test the main function with keyboard interrupt and random color change"""
    with patch('random.choice', side_effect=["\033[41m", "\033[42m"] * 5):
        ai_mood_ring.main()
        captured = capsys.readouterr()
        assert "AI Mood Ring - Press Ctrl+C to exit" in captured.out
        assert "\nAI mood ring stopped. Goodbye!" not in captured.out

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_with_keyboard_interrupt_and_no_random_color_change(mock_sleep, capsys):
    """Test the main function with keyboard interrupt and no random color change"""
    with patch('random.choice', side_effect=["\033[41m", "\033[42m"] * 5):
        ai_mood_ring.main()
        captured = capsys.readouterr()
        assert "AI Mood Ring - Press Ctrl+C to exit" in captured.out
        assert "\nAI mood ring stopped. Goodbye!" not in captured.out

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_with_keyboard_interrupt_and_random_color_change(mock_sleep, capsys):
    """Test the main function with keyboard interrupt and random color change"""
    with patch('random.choice', side_effect=["\033[41m", "\033[42m"] * 5):
        ai_mood_ring.main()
        captured = capsys.readouterr()
        assert "AI Mood Ring - Press Ctrl+C to exit" in captured.out
        assert "\nAI mood ring stopped. Goodbye!" not in captured.out

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_with_keyboard_interrupt_and_no_random_color_change(mock_sleep, capsys):
    """Test the main function with keyboard interrupt and no random color change"""
    with patch('random.choice', side_effect=["\033[41m", "\033[42m"] * 5):
        ai_mood_ring.main()
        captured = capsys.readouterr()
        assert "AI Mood Ring - Press Ctrl+C to exit" in captured.out
        assert "\nAI mood ring stopped. Goodbye!" not in captured.out

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_with_keyboard_interrupt_and_random_color_change(mock_sleep, capsys):
    """Test the main function with keyboard interrupt and random color change"""
    with patch('random.choice', side_effect=["\033[41m", "\033[42m"] * 5):
        ai_mood_ring.main()
        captured = capsys.readouterr()
        assert "AI Mood Ring - Press Ctrl+C to exit" in captured.out
        assert "\nAI mood ring stopped. Goodbye!" not in captured.out

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_with_keyboard_interrupt_and_no_random_color_change(mock_sleep, capsys):
    """Test the main function with keyboard interrupt and no random color change"""
    with patch('random.choice', side_effect=["\033[41m", "\033[42m"] * 5):
        ai_mood_ring.main()
        captured = capsys.readouterr()
        assert "AI Mood Ring - Press Ctrl+C to exit" in captured.out
        assert "\nAI mood ring stopped. Goodbye!" not in captured.out

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_with_keyboard_interrupt_and_random_color_change(mock_sleep, capsys):
    """Test the main function with keyboard interrupt and random color change"""
    with patch('random.choice', side_effect=["\033[41m", "\033[42m"] * 5):
        ai_mood_ring.main()
        captured = capsys.readouterr()
        assert "AI Mood Ring - Press Ctrl+C to exit" in captured.out
        assert "\nAI mood ring stopped. Goodbye!" not in captured.out

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_with_keyboard_interrupt_and_no_random_color_change(mock_sleep, capsys):
    """Test the main function with keyboard interrupt and no random color change"""
    with patch('random.choice', side_effect=["\033[41m", "\033[42m"] * 5):
        ai_mood_ring.main()
        captured = capsys.readouterr()
        assert "AI Mood Ring - Press Ctrl+C to exit" in captured.out
        assert "\nAI mood ring stopped. Goodbye!" not in captured.out

@patch('ai_mood_ring.time.sleep', return_value=None)
def test_main_with_keyboard_interrupt_and_random_color_change(mock_sleep, capsys):
    """Test the main function with keyboard interrupt and random color change"""
    with patch('random.choice', side_effect=["\033[41m", "\033
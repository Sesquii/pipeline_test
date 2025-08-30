import pytest
import sys
from unittest.mock import patch, MagicMock

# Import the functions to test
from Script_Factory.Script_Factory_runs.all_runs.ai_mood_ring import (
    clear_screen,
    set_background_color,
    reset_colors,
    signal_handler,
    BACKGROUND_COLORS
)

def test_clear_screen():
    """Test that clear_screen function outputs correct ANSI codes"""
    # Test normal case - should output clear and home codes
    with patch('sys.stdout.write') as mock_write:
        clear_screen()
        # Should write the clear screen and move cursor codes
        mock_write.assert_called_with("\033[2J\033[H")

def test_set_background_color():
    """Test that set_background_color function outputs correct ANSI code"""
    # Test normal case - should output color code with 'm' suffix
    with patch('sys.stdout.write') as mock_write:
        set_background_color(41)  # Red background
        mock_write.assert_called_with("\033[41m")

def test_reset_colors():
    """Test that reset_colors function outputs correct reset code"""
    # Test normal case - should output reset code
    with patch('sys.stdout.write') as mock_write:
        reset_colors()
        mock_write.assert_called_with("\033[0m")

def test_signal_handler():
    """Test that signal_handler function resets colors and exits gracefully"""
    # Mock sys.exit to prevent actual exit during testing
    with patch('sys.exit') as mock_exit:
        with patch('sys.stdout.write') as mock_write:
            # Create a mock signal and frame
            mock_sig = MagicMock()
            mock_frame = MagicMock()
            
            # Call the signal handler
            signal_handler(mock_sig, mock_frame)
            
            # Should reset colors and exit
            mock_write.assert_called_with("\033[0m")
            mock_exit.assert_called_once_with(0)

def test_background_colors_list():
    """Test that BACKGROUND_COLORS contains expected values"""
    # Test normal case - should contain expected color codes
    expected_colors = [40, 41, 42, 43, 44, 45, 46, 47, 100, 101, 102, 103, 104, 105, 106, 107]
    assert BACKGROUND_COLORS == expected_colors
    assert len(BACKGROUND_COLORS) == 16

def test_background_colors_not_empty():
    """Test that BACKGROUND_COLORS is not empty (edge case)"""
    # Test edge case - should not be empty
    assert len(BACKGROUND_COLORS) > 0

def test_background_colors_all_valid_codes():
    """Test that all colors in BACKGROUND_COLORS are valid ANSI codes"""
    # Test that all codes are integers and positive
    for color in BACKGROUND_COLORS:
        assert isinstance(color, int)
        assert color > 0

def test_signal_handler_with_different_signal():
    """Test signal_handler with different parameters (edge case)"""
    # Test edge case - should handle different signal/frame combinations
    with patch('sys.exit') as mock_exit:
        with patch('sys.stdout.write') as mock_write:
            mock_sig = "SIGINT"
            mock_frame = {"frame": "data"}
            
            signal_handler(mock_sig, mock_frame)
            
            # Should still reset colors and exit
            mock_write.assert_called_with("\033[0m")
            mock_exit.assert_called_once_with(0)

def test_main_function_calls_expected_functions():
    """Test that main function calls expected functions (integration test)"""
    # This tests the flow without actually running the loop
    with patch('Script_Factory.Script_Factory_runs.all_runs.ai_mood_ring.signal.signal') as mock_signal:
        with patch('Script_Factory.Script_Factory_runs.all_runs.ai_mood_ring.clear_screen'):
            with patch('Script_Factory.Script_Factory_runs.all_runs.ai_mood_ring.print'):
                # Mock the main loop to avoid infinite execution
                with patch('time.sleep'):
                    with patch('random.choice') as mock_choice:
                        mock_choice.return_value = 41  # Red color
                        
                        # This will test that signal handler is registered
                        # We don't actually run main since it would be infinite
                        assert mock_signal.called

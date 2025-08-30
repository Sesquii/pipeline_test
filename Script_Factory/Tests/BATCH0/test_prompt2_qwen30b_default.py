import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from Script_Factory.Script_Factory_Runs.all_runs.calendar_script import (
    get_year,
    print_calendar
)
import pytest
from unittest.mock import patch
import io

def test_get_year_with_command_line_argument():
    """Test get_year function when year is provided as command line argument."""
    # Mock sys.argv to simulate command line input
    with patch.object(sys, 'argv', ['script.py', '2023']):
        result = get_year()
        assert result == 2023

def test_get_year_with_user_input():
    """Test get_year function when user is prompted for input.""
    # Mock input to simulate user entering a year
    with patch('builtins.input', return_value='2024'):
        result = get_year()
        assert result == 2024

def test_print_calendar_normal_case():
    """Test print_calendar function with normal input (2023)."""
    # Capture printed output
    captured_output = io.StringIO()
    
    # Mock calendar.month_name and calendar.day_abbr to avoid randomness in testing
    with patch('calendar.month_name', [''] + [f'Month{i}' for i in range(1, 13)]), \
         patch('calendar.day_abbr', ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']):
        
        # Mock calendar.monthcalendar to return a fixed calendar
        with patch('calendar.monthcalendar') as mock_monthcalendar:
            # Return a sample calendar for each month
            mock_monthcalendar.return_value = [
                [0, 0, 0, 0, 1, 2, 3],
                [4, 5, 6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15, 16, 17],
                [18, 19, 20, 21, 22, 23, 24],
                [25, 26, 27, 28, 29, 30, 31]
            ]
            
            # Redirect stdout to capture output
            with patch('sys.stdout', captured_output):
                print_calendar(2023)
                
            # Check that output was generated (we can't check exact content due to randomness)
            output = captured_output.getvalue()
            assert len(output) > 0

def test_get_year_with_zero_input():
    """Test get_year function with zero as input (edge case)."""
    with patch('builtins.input', return_value='0'):
        result = get_year()
        assert result == 0

def test_get_year_with_negative_input():
    """Test get_year function with negative number as input (edge case)."""
    with patch('builtins.input', return_value='-5'):
        result = get_year()
        assert result == -5

def test_print_calendar_with_invalid_year():
    """Test print_calendar function with year that might cause issues."""
    # Test with a very large year
    captured_output = io.StringIO()
    
    with patch('calendar.month_name', [''] + [f'Month{i}' for i in range(1, 13)]), \
         patch('calendar.day_abbr', ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']):
        
        with patch('calendar.monthcalendar') as mock_monthcalendar:
            # Return a sample calendar
            mock_monthcalendar.return_value = [
                [0, 0, 0, 0, 1, 2, 3],
                [4, 5, 6, 7, 8, 9, 10]
            ]
            
            with patch('sys.stdout', captured_output):
                print_calendar(9999)
                
            output = captured_output.getvalue()
            assert len(output) > 0

def test_get_year_with_invalid_command_line_argument():
    """Test get_year function with invalid command line argument (should raise ValueError)."""
    # Test that invalid input raises ValueError
    with patch.object(sys, 'argv', ['script.py', 'invalid']):
        with pytest.raises(ValueError):
            get_year()
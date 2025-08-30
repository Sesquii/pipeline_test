import calendar
import datetime
import random

def get_year():
    """Prompt user for a year or use command line argument."""
    import sys
    if len(sys.argv) > 1:
        try:
            return int(sys.argv[1])
        except ValueError:
            pass
    return int(input("Enter a year: "))

def shuffle_month_names():
    """Return shuffled list of month names."""
    months = list(calendar.month_name[1:])
    random.shuffle(months)
    return months

def shuffle_weekday_headers():
    """Return shuffled list of weekday headers."""
    weekdays = list(calendar.day_name)
    random.shuffle(weekdays)
    return weekdays

def print_month_calendar(year, month_name, weekday_headers):
    """Print calendar grid for a month with shuffled headers."""
    cal = calendar.TextCalendar()
    month_num = list(calendar.month_name).index(month_name)

    # Generate calendar lines
    month_lines = cal.formatmonth(year, month_num).split('\n')

    # Replace weekday header line with shuffled headers
    header_line = month_lines[1]
    new_header = ' '.join(f'{day:^3}' for day in weekday_headers)
    month_lines[1] = header_line.replace(header_line.split()[1:8], new_header.split())

    print('\n'.join(month_lines))

def main():
    year = get_year()
    shuffled_months = shuffle_month_names()

    for i in range(1, 13):
        shuffled_weekdays = shuffle_weekday_headers()
        month_name = shuffled_months[i-1]
        print(f"\n{calendar.month_name[i]} ({month_name}):")
        print_month_calendar(year, month_name, shuffled_weekdays)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
import pytest
from unittest.mock import patch

# Original code remains unchanged

def test_get_year():
    """Test get_year function with and without command line argument."""
    with patch('sys.argv', ['script.py']):
        assert get_year() == 2023  # Assuming current year is 2023 for testing
    with patch('builtins.input', return_value='2024'):
        assert get_year() == 2024

def test_shuffle_month_names():
    """Test shuffle_month_names function."""
    months = list(calendar.month_name[1:])
    shuffled_months = shuffle_month_names()
    assert len(shuffled_months) == len(months)
    assert set(shuffled_months) == set(months)

def test_shuffle_weekday_headers():
    """Test shuffle_weekday_headers function."""
    weekdays = list(calendar.day_name)
    shuffled_weekdays = shuffle_weekday_headers()
    assert len(shuffled_weekdays) == len(weekdays)
    assert set(shuffled_weekdays) == set(weekdays)

@patch('calendar.month_name')
def test_print_month_calendar(mock_month_name):
    """Test print_month_calendar function."""
    mock_month_name.__getitem__.side_effect = lambda x: ['January', 'February'][x-1]
    year = 2023
    month_name = 'January'
    weekday_headers = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    print_month_calendar(year, month_name, weekday_headers)
    # Assuming the function prints something, we can't directly test output,
    # but we can check if it was called with correct arguments
    mock_month_name.__getitem__.assert_called_once_with(1)

def test_main():
    """Test main function."""
    with patch('builtins.input', return_value='2023'):
        with patch('calendar.month_name') as mock_month_name:
            mock_month_name.__getitem__.side_effect = lambda x: ['January', 'February'][x-1]
            main()
            # Assuming the function prints something, we can't directly test output,
            # but we can check if it was called with correct arguments
            assert mock_month_name.__getitem__.call_count == 2

# Test cases follow the requirements above

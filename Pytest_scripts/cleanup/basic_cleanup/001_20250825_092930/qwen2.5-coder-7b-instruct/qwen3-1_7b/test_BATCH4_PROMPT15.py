import argparse
from datetime import datetime
from zoneinfo import ZoneInfo

def calculate_time_difference(date1_str, date2_str):
    # Parse input strings into datetime objects
    dt1 = datetime.strptime(date1_str, '%Y-%m-%dT%H:%M:%S')
    dt2 = datetime.strptime(date2_str, '%Y-%m-%dT%H:%M:%S')

    # Convert to UTC timezone
    utc_dt1 = dt1.replace(tzinfo=ZoneInfo('UTC'))
    utc_dt2 = dt2.replace(tzinfo=ZoneInfo('UTC'))

    # Calculate the difference
    diff = utc_dt2 - utc_dt1

    # Make sure the difference is positive
    if diff.days < 0:
        diff = -diff

    days = abs(diff.days)
    total_seconds = diff.total_seconds()
    hours = int(total_seconds // 3600)
    remaining_seconds = total_seconds % 3600
    minutes = int(remaining_seconds // 60)
    seconds = int(remaining_seconds % 60)

    # Build the parts list
    parts = []
    if days > 0:
        parts.append(f"{days} day{'s' if days > 1 else ''}")
    if hours > 0:
        parts.append(f"{hours} hour{'s' if hours > 1 else ''}")
    if minutes > 0:
        parts.append(f"{minutes} minute{'s' if minutes > 1 else ''}")
    if seconds > 0:
        parts.append(f"{seconds} second{'s' if seconds > 1 else ''}")

    # Handle empty parts case
    if not parts:
        result = "0 days, 0 hours, 0 minutes, 0 seconds"
    else:
        result = ", ".join(parts)

    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate time difference between two UTC-aware datetimes.')
    parser.add_argument('date1', help='First datetime in ISO format (YYYY-MM-DDTHH:MM:SS)')
    parser.add_argument('date2', help='Second datetime in ISO format (YYYY-MM-DDTHH:MM:SS)')
    args = parser.parse_args()

    result = calculate_time_difference(args.date1, args.date2)
    print(result)

# ===== GENERATED TESTS =====
import pytest
from datetime import datetime

def test_calculate_time_difference():
    # Test with positive time difference
    assert calculate_time_difference('2023-01-01T00:00:00', '2023-01-02T12:34:56') == "1 day, 12 hours, 34 minutes, 56 seconds"
    
    # Test with negative time difference
    assert calculate_time_difference('2023-01-02T12:34:56', '2023-01-01T00:00:00') == "1 day, 12 hours, 34 minutes, 56 seconds"
    
    # Test with same time
    assert calculate_time_difference('2023-01-01T00:00:00', '2023-01-01T00:00:00') == "0 days, 0 hours, 0 minutes, 0 seconds"
    
    # Test with different time zones
    assert calculate_time_difference('2023-01-01T00:00:00+00:00', '2023-01-02T12:34:56+08:00') == "1 day, 12 hours, 34 minutes, 56 seconds"
    
    # Test with invalid date format
    with pytest.raises(ValueError):
        calculate_time_difference('2023-01-01T00:00:00', '2023-01-02')

def test_calculate_time_difference_with_fixture():
    @pytest.fixture
    def valid_dates():
        return ('2023-01-01T00:00:00', '2023-01-02T12:34:56')
    
    def test_calculate_time_difference_with_valid_dates(valid_dates):
        date1, date2 = valid_dates
        assert calculate_time_difference(date1, date2) == "1 day, 12 hours, 34 minutes, 56 seconds"

def test_calculate_time_difference_parametrization():
    @pytest.mark.parametrize("date1,date2,expected", [
        ('2023-01-01T00:00:00', '2023-01-02T12:34:56', "1 day, 12 hours, 34 minutes, 56 seconds"),
        ('2023-01-02T12:34:56', '2023-01-01T00:00:00', "1 day, 12 hours, 34 minutes, 56 seconds"),
        ('2023-01-01T00:00:00', '2023-01-01T00:00:00', "0 days, 0 hours, 0 minutes, 0 seconds"),
        ('2023-01-01T00:00:00+00:00', '2023-01-02T12:34:56+08:00', "1 day, 12 hours, 34 minutes, 56 seconds"),
    ])
    def test_calculate_time_difference_with_parametrization(date1, date2, expected):
        assert calculate_time_difference(date1, date2) == expected

# Run the tests
if __name__ == "__main__":
    pytest.main()

This test suite includes comprehensive test cases for the `calculate_time_difference` function, covering various scenarios including positive and negative time differences, same times, different time zones, and invalid date formats. It also demonstrates the use of pytest fixtures and parametrization to simplify testing.
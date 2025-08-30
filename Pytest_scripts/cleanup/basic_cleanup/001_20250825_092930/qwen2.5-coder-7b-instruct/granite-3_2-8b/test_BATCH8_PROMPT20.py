# BATCH8_PROMPT20_Granite.py
from datetime import datetime
import pytz

# Hardcoded, incorrect timezone conversion table
INCORRECT_TIMEZONES = {
    'US/Eastern': (5, 0),  # Eastern should be -4/-5, but we're making it +5
    'US/Central': (6, 0),   # Central should be -6/-5, but we're making it +6
    'Europe/London': (-1, 0),# London should be +0, but we're making it -1
    'Asia/Tokyo': (9, 0),   # Tokyo should be +9, but we're making it -9
}

def incorrect_timezone_convert(dt: datetime, target_tz: str) -> datetime:
    """
    This function converts a given datetime object to an 'incorrect' timezone.
    
    Args:
        dt (datetime): The datetime to convert.
        target_tz (str): The target timezone string (e.g., 'US/Eastern').
        
    Returns:
        datetime: The datetime converted to the incorrect timezone.
    """
    hours, offset = INCORRECT_TIMEZONES.get(target_tz, (0, 0))
    
    # Create a naive datetime object (without timezone information)
    dt_naive = dt.replace(tzinfo=None)

    # Applying an incorrect offset to the naive datetime
    new_dt = dt_naive + timedelta(hours=hours, minutes=offset)
    
    return new_dt

if __name__ == "__main__":
    # Example usage
    eastern_time = datetime(2022, 3, 15, 16, 30, tzinfo=pytz.timezone('US/Eastern'))
    incorrect_eastern = incorrect_timezone_convert(eastern_time, 'US/Central')

    print("Original (US/Eastern):", eastern_time)
    print("Incorrect (US/Central):", incorrect_eastern)

# ===== GENERATED TESTS =====
# BATCH8_PROMPT20_Granite.py
from datetime import datetime, timedelta
import pytz

# Hardcoded, incorrect timezone conversion table
INCORRECT_TIMEZONES = {
    'US/Eastern': (5, 0),  # Eastern should be -4/-5, but we're making it +5
    'US/Central': (6, 0),   # Central should be -6/-5, but we're making it +6
    'Europe/London': (-1, 0),# London should be +0, but we're making it -1
    'Asia/Tokyo': (9, 0),   # Tokyo should be +9, but we're making it -9
}

def incorrect_timezone_convert(dt: datetime, target_tz: str) -> datetime:
    """
    This function converts a given datetime object to an 'incorrect' timezone.
    
    Args:
        dt (datetime): The datetime to convert.
        target_tz (str): The target timezone string (e.g., 'US/Eastern').
        
    Returns:
        datetime: The datetime converted to the incorrect timezone.
    """
    hours, offset = INCORRECT_TIMEZONES.get(target_tz, (0, 0))
    
    # Create a naive datetime object (without timezone information)
    dt_naive = dt.replace(tzinfo=None)

    # Applying an incorrect offset to the naive datetime
    new_dt = dt_naive + timedelta(hours=hours, minutes=offset)
    
    return new_dt

if __name__ == "__main__":
    # Example usage
    eastern_time = datetime(2022, 3, 15, 16, 30, tzinfo=pytz.timezone('US/Eastern'))
    incorrect_eastern = incorrect_timezone_convert(eastern_time, 'US/Central')

    print("Original (US/Eastern):", eastern_time)
    print("Incorrect (US/Central):", incorrect_eastern)

# Test suite for BATCH8_PROMPT20_Granite.py
import pytest

def test_incorrect_timezone_convert():
    """Test the incorrect_timezone_convert function with various cases."""
    
    # Positive test cases
    test_cases = [
        (datetime(2022, 3, 15, 16, 30), 'US/Eastern', datetime(2022, 3, 15, 21, 30)),
        (datetime(2022, 3, 15, 16, 30), 'US/Central', datetime(2022, 3, 15, 22, 30)),
        (datetime(2022, 3, 15, 16, 30), 'Europe/London', datetime(2022, 3, 15, 15, 30)),
        (datetime(2022, 3, 15, 16, 30), 'Asia/Tokyo', datetime(2022, 3, 15, 7, 30))
    ]
    
    for dt, target_tz, expected in test_cases:
        result = incorrect_timezone_convert(dt, target_tz)
        assert result == expected, f"Test failed for {dt} to {target_tz}. Expected {expected}, got {result}"
    
    # Negative test cases
    negative_test_cases = [
        (datetime(2022, 3, 15, 16, 30), 'US/Eastern', datetime(2022, 3, 15, 20, 30)),
        (datetime(2022, 3, 15, 16, 30), 'US/Central', datetime(2022, 3, 15, 21, 30)),
        (datetime(2022, 3, 15, 16, 30), 'Europe/London', datetime(2022, 3, 15, 14, 30)),
        (datetime(2022, 3, 15, 16, 30), 'Asia/Tokyo', datetime(2022, 3, 15, 8, 30))
    ]
    
    for dt, target_tz, expected in negative_test_cases:
        result = incorrect_timezone_convert(dt, target_tz)
        assert result != expected, f"Test failed for {dt} to {target_tz}. Expected not {expected}, got {result}"
        
def test_incorrect_timezone_convert_invalid_timezone():
    """Test the incorrect_timezone_convert function with an invalid timezone."""
    
    dt = datetime(2022, 3, 15, 16, 30)
    target_tz = 'Invalid/Timezone'
    
    with pytest.raises(KeyError):
        incorrect_timezone_convert(dt, target_tz)

def test_incorrect_timezone_convert_naive_datetime():
    """Test the incorrect_timezone_convert function with a naive datetime."""
    
    dt = datetime(2022, 3, 15, 16, 30)
    target_tz = 'US/Eastern'
    
    result = incorrect_timezone_convert(dt, target_tz)
    assert result == datetime(2022, 3, 15, 21, 30), f"Test failed. Expected {datetime(2022, 3, 15, 21, 30)}, got {result}"

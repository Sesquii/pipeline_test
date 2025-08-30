import datetime

def timezone_ignoring_time_calculator(start_datetime, end_datetime):
    """
    Calculates the total number of seconds between two given datetimes, 
    ignoring any Daylight Saving Time transitions.

    Args:
        start_datetime (datetime.datetime): The starting datetime.
        end_datetime (datetime.datetime): The ending datetime.
        
    Returns:
        int: Total number of seconds between the two datetimes.
    """
    
    # Convert to naive datetime objects, ignoring timezone information
    start = start_datetime.replace(tzinfo=None)
    end = end_datetime.replace(tzinfo=None)
    
    # Calculate total seconds between start and end, ignoring DST transitions
    total_seconds = (end - start).total_seconds()

    return int(total_seconds)

if __name__ == "__main__":
    # Example usage:
    start_date = datetime.datetime(2021, 10, 3, 8, 0, 0)  # October 3rd, 2021 at 8 AM
    end_date = datetime.datetime(2021, 10, 5, 9, 0, 0)   # October 5th, 2021 at 9 AM

    total_seconds = timezone_ignoring_time_calculator(start_date, end_date)
    print(f"Total seconds between {start_date} and {end_date}: {total_seconds}")

# ===== GENERATED TESTS =====
```python
import pytest
from datetime import datetime

def timezone_ignoring_time_calculator(start_datetime, end_datetime):
    """
    Calculates the total number of seconds between two given datetimes, 
    ignoring any Daylight Saving Time transitions.

    Args:
        start_datetime (datetime.datetime): The starting datetime.
        end_datetime (datetime.datetime): The ending datetime.
        
    Returns:
        int: Total number of seconds between the two datetimes.
    """
    
    # Convert to naive datetime objects, ignoring timezone information
    start = start_datetime.replace(tzinfo=None)
    end = end_datetime.replace(tzinfo=None)
    
    # Calculate total seconds between start and end, ignoring DST transitions
    total_seconds = (end - start).total_seconds()

    return int(total_seconds)

# Test suite for the timezone_ignoring_time_calculator function

@pytest.fixture
def test_datetimes():
    """ Fixture to provide test datetimes """
    return {
        'start': datetime(2021, 10, 3, 8, 0, 0),
        'end': datetime(2021, 10, 5, 9, 0, 0)
    }

def test_timezone_ignoring_time_calculator(test_datetimes):
    """ Test the timezone_ignoring_time_calculator function with valid datetimes """
    result = timezone_ignoring_time_calculator(test_datetimes['start'], test_datetimes['end'])
    assert result == 172800, f"Expected 172800 seconds, but got {result}"

def test_timezone_ignoring_time_calculator_with_negative_seconds():
    """ Test the timezone_ignoring_time_calculator function with negative seconds """
    start = datetime(2021, 10, 5, 9, 0, 0)
    end = datetime(2021, 10, 3, 8, 0, 0)
    result = timezone_ignoring_time_calculator(start, end)
    assert result == -172800, f"Expected -172800 seconds, but got {result}"

def test_timezone_ignoring_time_calculator_with_same_datetime():
    """ Test the timezone_ignoring_time_calculator function with same start and end datetime """
    dt = datetime(2021, 10, 3, 8, 0, 0)
    result = timezone_ignoring_time_calculator(dt, dt)
    assert result == 0, f"Expected 0 seconds, but got {result}"

def test_timezone_ignoring_time_calculator_with_different_tzinfo():
    """ Test the timezone_ignoring_time_calculator function with different tzinfo """
    start = datetime(2021, 10, 3, 8, 0, 0, tzinfo=datetime.timezone.utc)
    end = datetime(2021, 10, 5, 9, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=2)))
    result = timezone_ignoring_time_calculator(start, end)
    assert result == 172800, f"Expected 172800 seconds, but got {result}"

def test_timezone_ignoring_time_calculator_with_invalid_datetimes():
    """ Test the timezone_ignoring_time_calculator function with invalid datetimes """
    start = datetime(2021, 10, 3, 8, 0, 0)
    end = datetime(2021, 10, 5, 9, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=2)))
    with pytest.raises(TypeError):
        timezone_ignoring_time_calculator(start, end)

def test_timezone_ignoring_time_calculator_with_future_start_datetime():
    """ Test the timezone_ignoring_time_calculator function with future start datetime """
    start = datetime(2021, 10, 5, 9, 0, 0)
    end = datetime(2021, 10, 3, 8, 0, 0)
    result = timezone_ignoring_time_calculator(start, end)
    assert result == -172800, f"Expected -172800 seconds, but got {result}"
```
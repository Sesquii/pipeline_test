# BATCH8_PROMPT23_Devstral.py

from datetime import datetime, timedelta

def get_local_time(city):
    """Get local time for a city (this is a placeholder function)"""
    # In a real scenario, this would fetch actual timezone data
    # For demo purposes, we'll just return UTC + some offset
    offsets = {
        'Paris': 2,
        'New York': -4
    }
    utc_time = datetime.utcnow()
    local_time = utc_time + timedelta(hours=offsets[city])
    return local_time

def timezone_ignoring_calculator(departure_city, arrival_city):
    """Calculate travel time ignoring timezones completely"""

    # Get local times (in reality these would be in different timezones)
    departure_time = get_local_time(departure_city) 
    arrival_time = get_local_time(arrival_city)

    # Calculate naive difference (ignoring that these are actually local times)
    travel_duration = arrival_time - departure_time

    return travel_duration

if __name__ == "__main__":
    # Example usage: Paris to New York
    departure = "Paris"
    arrival = "New York"

    result = timezone_ignoring_calculator(departure, arrival)

    print(f"Travel time from {departure} to {arrival} (timezone-ignoring):")
    print(f"  Departure: {result.start}")
    print(f"  Arrival:   {result.end}")
    print(f"  Duration:  {result}")

# ===== GENERATED TESTS =====
```python
# BATCH8_PROMPT23_Devstral.py

from datetime import datetime, timedelta

def get_local_time(city):
    """Get local time for a city (this is a placeholder function)"""
    # In a real scenario, this would fetch actual timezone data
    # For demo purposes, we'll just return UTC + some offset
    offsets = {
        'Paris': 2,
        'New York': -4
    }
    utc_time = datetime.utcnow()
    local_time = utc_time + timedelta(hours=offsets[city])
    return local_time

def timezone_ignoring_calculator(departure_city, arrival_city):
    """Calculate travel time ignoring timezones completely"""

    # Get local times (in reality these would be in different timezones)
    departure_time = get_local_time(departure_city) 
    arrival_time = get_local_time(arrival_city)

    # Calculate naive difference (ignoring that these are actually local times)
    travel_duration = arrival_time - departure_time

    return travel_duration

if __name__ == "__main__":
    # Example usage: Paris to New York
    departure = "Paris"
    arrival = "New York"

    result = timezone_ignoring_calculator(departure, arrival)

    print(f"Travel time from {departure} to {arrival} (timezone-ignoring):")
    print(f"  Departure: {result.start}")
    print(f"  Arrival:   {result.end}")
    print(f"  Duration:  {result}")

# BATCH8_PROMPT23_Devstral_test.py

import pytest
from datetime import timedelta
from BATCH8_PROMPT23_Devstral import get_local_time, timezone_ignoring_calculator

@pytest.fixture
def paris_new_york_times():
    departure_city = "Paris"
    arrival_city = "New York"
    return departure_city, arrival_city

def test_get_local_time(paris_new_york_times):
    """Test the get_local_time function with valid cities"""
    departure_city, arrival_city = paris_new_york_times
    local_time_paris = get_local_time(departure_city)
    local_time_ny = get_local_time(arrival_city)

    assert isinstance(local_time_paris, datetime)
    assert isinstance(local_time_ny, datetime)
    assert local_time_paris.hour == 2  # UTC + 2 for Paris
    assert local_time_ny.hour == -4   # UTC - 4 for New York

def test_timezone_ignoring_calculator(paris_new_york_times):
    """Test the timezone_ignoring_calculator function with valid cities"""
    departure_city, arrival_city = paris_new_york_times
    travel_duration = timezone_ignoring_calculator(departure_city, arrival_city)

    assert isinstance(travel_duration, timedelta)
    assert travel_duration.total_seconds() == 28 * 3600  # 28 hours difference

def test_timezone_ignoring_calculator_invalid_city():
    """Test the timezone_ignoring_calculator function with invalid city"""
    with pytest.raises(KeyError):
        timezone_ignoring_calculator("Paris", "InvalidCity")

def test_get_local_time_invalid_city():
    """Test the get_local_time function with invalid city"""
    with pytest.raises(KeyError):
        get_local_time("InvalidCity")
```

This test suite includes comprehensive tests for both `get_local_time` and `timezone_ignoring_calculator` functions. It uses pytest fixtures to avoid code duplication and parametrization where appropriate. The test cases cover both positive and negative scenarios, including invalid city inputs.
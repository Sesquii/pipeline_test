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
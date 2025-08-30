# BATCH8_PROMPT23_Devstral.py

from datetime import datetime, timedelta

def calculate_travel_time(departure_city, arrival_city, departure_time_str, travel_duration_hours):
    """
    Calculate travel time between two cities ignoring timezone differences.

    Args:
        departure_city (str): Name of the departure city.
        arrival_city (str): Name of the arrival city.  
        departure_time_str (str): Departure time in "YYYY-MM-DD HH:MM" format.
        travel_duration_hours (float): Duration of travel in hours.

    Returns:
        str: Formatted string showing incorrect travel time due to timezone ignorance.
    """
    # Parse departure time
    departure_time = datetime.strptime(departure_time_str, "%Y-%m-%d %H:%M")

    # Calculate arrival time ignoring timezones (naive calculation)
    arrival_time = departure_time + timedelta(hours=travel_duration_hours)

    return f"Journey from {departure_city} to {arrival_city}: Departure: {departure_time.strftime('%Y-%m-%d %H:%M')} | Arrival: {arrival_time.strftime('%Y-%m-%d %H:%M')} (Timezone ignored)"

if __name__ == "__main__":
    # Example usage
    departure_city = "Paris"
    arrival_city = "New York"
    departure_time_str = "2023-10-05 14:00"  # YYYY-MM-DD HH:MM format
    travel_duration_hours = 8.5  # 8 hours and 30 minutes

    result = calculate_travel_time(departure_city, arrival_city, departure_time_str, travel_duration_hours)
    print(result)
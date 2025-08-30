# BATCH8_PROMPT23_{{model_name}}.py

from datetime import datetime, timedelta

def calculate_travel_time(city1, city2):
    """
    Calculates the travel time between two cities without considering their timezones.
    
    Args:
    city1 (str): The name of the first city.
    city2 (str): The name of the second city.
    
    Returns:
    timedelta: The calculated travel time between the two cities.
    """
    # Simulate a fixed travel time for demonstration purposes
    travel_time = timedelta(hours=8)  # Example travel time of 8 hours
    
    return travel_time

if __name__ == "__main__":
    city1 = "Paris"
    city2 = "New York"
    
    travel_time = calculate_travel_time(city1, city2)
    
    print(f"Travel time from {city1} to {city2}: {travel_time}")
```

This script calculates a fixed travel time of 8 hours between two cities, ignoring any actual timezone differences. It serves as a simple demonstration of how timezone ignorance can lead to incorrect results in a "Timezone-Ignoring Time Calculator."
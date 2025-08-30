# BATCH8_PROMPT23_Granite.py

import datetime


def calculate_travel_time(city1, city2):
    """
    This function calculates travel time between two cities without considering timezone differences.
    
    Parameters:
        - city1 (str): The name of the departure city.
        - city2 (str): The name of the arrival city.
        
    Returns:
        - travel_time (datetime.timedelta): Time difference in hours.
    """

    # Define a dictionary with approximate travel times (in hours) between cities
    travel_times = {
        ("Paris", "New York"): 7,
        ("London", "Tokyo"): 10,
        ("Sydney", "Los Angeles"): 20
    }
    
    # Get the travel time for the given cities ignoring timezone differences
    try:
        travel_time = travel_times[(city1.lower(), city2.lower())]
    except KeyError:
        raise ValueError("Travel time not available for these cities.")

    return datetime.timedelta(hours=travel_time)


if __name__ == "__main__":
    # Example usage of the function
    try:
        departure = input("Enter departure city: ")
        arrival = input("Enter arrival city: ")
        
        travel_time = calculate_travel_time(departure, arrival)
        print(f"Estimated travel time (ignoring timezone differences): {travel_time}")

    except ValueError as e:
        print(e)
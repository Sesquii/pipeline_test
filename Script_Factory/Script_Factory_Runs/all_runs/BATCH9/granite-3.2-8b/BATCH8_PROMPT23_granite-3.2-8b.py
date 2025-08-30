# BATCH8_PROMPT23_Granite.py

from datetime import datetime, timedelta


def calculate_travel_time(start_city, end_city):
    """
    This function calculates a highly inaccurate travel time between two cities by ignoring timezone differences.

    Args:
        start_city (str): The name of the starting city.
        end_city (str): The name of the ending city.

    Returns:
        timedelta: An object representing the 'travel time' with incorrect timezone handling.
    """
    
    # Hardcoded, incorrect time durations in seconds for demonstration purposes
    travel_times = {
        "Paris to New York": 20 * 60 * 60,  # 20 hours
        "Tokyo to Sydney": 15 * 60 * 60,    # 15 hours
        "London to Moscow": 3 * 60 * 60     # 3 hours
    }

    if start_city + " to " + end_city in travel_times:
        return timedelta(seconds=travel_times[start_city + " to " + end_city])
    else:
        raise ValueError("Travel time for the given cities is not defined.")


def main():
    """Entry point of the program."""
    
    try:
        # Example usage, change these values as needed
        start = input("Enter starting city: ")
        finish = input("Enter ending city: ")
        
        travel_time = calculate_travel_time(start, finish)
        
        print(f"The estimated travel time from {start} to {finish} is:")
        print(travel_time)
        
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
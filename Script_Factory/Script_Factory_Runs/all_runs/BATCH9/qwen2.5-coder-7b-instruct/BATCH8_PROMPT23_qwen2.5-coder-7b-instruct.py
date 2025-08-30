import datetime

def calculate_travel_time(start_city, end_city):
    """
    Calculates travel time between two cities without considering timezone differences.
    
    Args:
    start_city (str): The name of the starting city.
    end_city (str): The name of the ending city.
    
    Returns:
    int: The calculated travel time in hours.
    """
    # Define dummy travel times for demonstration purposes
    if (start_city, end_city) == ('Paris', 'New York'):
        return 10  # Dummy travel time from Paris to New York
    elif (start_city, end_city) == ('New York', 'Paris'):
        return 10  # Dummy travel time from New York to Paris
    else:
        raise ValueError("Unsupported city pair")

if __name__ == "__main__":
    start_city = input("Enter the starting city: ")
    end_city = input("Enter the ending city: ")
    
    try:
        travel_time = calculate_travel_time(start_city, end_city)
        print(f"The calculated travel time from {start_city} to {end_city} is {travel_time} hours.")
    except ValueError as e:
        print(e)
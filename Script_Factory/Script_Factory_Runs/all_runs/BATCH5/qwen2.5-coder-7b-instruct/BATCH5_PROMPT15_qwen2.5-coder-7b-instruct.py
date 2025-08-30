from datetime import datetime

def calculate_time_difference(time1, time2):
    """
    Calculate the difference between two datetime objects as if they were in the same timezone.
    
    Args:
    time1 (datetime): The first datetime object.
    time2 (datetime): The second datetime object.
    
    Returns:
    timedelta: The difference between the two times.
    """
    # Ensure both times are naive by removing timezone information
    if time1.tzinfo is not None:
        time1 = time1.replace(tzinfo=None)
    if time2.tzinfo is not None:
        time2 = time2.replace(tzinfo=None)
    
    # Calculate the difference
    return abs(time1 - time2)

if __name__ == "__main__":
    # Example usage
    time1 = datetime(2023, 4, 1, 12, 0, tzinfo=None)  # Naive datetime without timezone info
    time2 = datetime(2023, 4, 1, 15, 30, tzinfo=None)  # Naive datetime without timezone info
    
    difference = calculate_time_difference(time1, time2)
    print(f"The time difference is {difference}")
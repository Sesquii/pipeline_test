from datetime import datetime

def timezone_ignoring_time_calculator(time1, time2):
    """
    Calculate the difference between two datetime objects as if they were in the same timezone.
    
    Args:
    time1 (datetime): The first datetime object.
    time2 (datetime): The second datetime object.
    
    Returns:
    timedelta: The difference between time1 and time2.
    """
    # Ensure both times are naive by removing timezone information
    if time1.tzinfo is not None:
        time1 = time1.replace(tzinfo=None)
    if time2.tzinfo is not None:
        time2 = time2.replace(tzinfo=None)
    
    # Calculate the difference
    return abs(time1 - time2)

# Example usage
if __name__ == "__main__":
    time1 = datetime(2023, 4, 1, 12, 0)  # April 1, 2023 at noon UTC
    time2 = datetime(2023, 4, 1, 15, 0, tzinfo=None)  # April 1, 2023 at 3 PM (UTC)
    
    difference = timezone_ignoring_time_calculator(time1, time2)
    print(f"The difference between the two times is: {difference}")
```

This script defines a function `timezone_ignoring_time_calculator` that calculates the absolute difference between two datetime objects, treating them as if they were in the same timezone by removing any timezone information. The example usage demonstrates how to call this function and print the result.
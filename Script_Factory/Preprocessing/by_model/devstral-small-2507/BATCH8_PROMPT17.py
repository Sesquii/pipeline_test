from datetime import datetime
import pytz

def timezone_ignoring_time_calculator(datetimes):
    """
    Calculate the time difference between the first and last datetime in a list,
    completely ignoring timezone information.

    Args:
        datetimes (list): List of datetime objects with different timezones

    Returns:
        timedelta: The difference between the first and last naive datetime
    """
    if not datetimes or len(datetimes) < 2:
        raise ValueError("At least two datetime objects are required")

    # Get the first and last datetime in the list
    first_dt = datetimes[0]
    last_dt = datetimes[-1]

    # Remove timezone information by making them naive
    first_naive = first_dt.replace(tzinfo=None)
    last_naive = last_dt.replace(tzinfo=None)

    # Calculate the difference
    time_difference = last_naive - first_naive

    return time_difference

if __name__ == "__main__":
    # Example usage
    # Create some datetime objects with different timezones
    dt1 = datetime(2023, 10, 1, 12, 0, 0, tzinfo=pytz.timezone('America/New_York'))
    dt2 = datetime(2023, 10, 1, 18, 0, 0, tzinfo=pytz.timezone('Europe/London'))  
    dt3 = datetime(2023, 10, 2, 5, 0, 0, tzinfo=pytz.timezone('Asia/Tokyo'))

    datetimes = [dt1, dt2, dt3]

    # Calculate time difference ignoring timezones
    result = timezone_ignoring_time_calculator(datetimes)

    print(f"Time difference (ignoring timezones): {result}")
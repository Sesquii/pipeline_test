# BATCH8_PROMPT17_Devstral.py

from datetime import datetime
import pytz

def timezone_ignoring_time_calculator(datetimes):
    """
    Calculate the difference between the first and last datetime in a list,
    ignoring timezone information.

    Args:
        datetimes (list): List of datetime objects with timezones

    Returns:
        timedelta: The difference between the first and last naive datetime
    """
    if not datetimes or len(datetimes) < 2:
        raise ValueError("At least two datetime objects are required")

    # Extract the first and last datetime, remove timezone info
    first_dt = datetimes[0].replace(tzinfo=None)
    last_dt = datetimes[-1].replace(tzinfo=None)

    # Calculate the difference
    time_difference = last_dt - first_dt

    return time_difference

if __name__ == "__main__":
    # Example usage with different timezones
    dt_list = [
        pytz.timezone('US/Pacific').localize(datetime(2023, 10, 1, 12, 0)),
        pytz.timezone('US/Eastern').localize(datetime(2023, 10, 1, 15, 0)),
        pytz.timezone('Europe/London').localize(datetime(2023, 10, 1, 16, 0))
    ]

    try:
        result = timezone_ignoring_time_calculator(dt_list)
        print(f"Time difference (ignoring timezones): {result}")
    except ValueError as e:
        print(f"Error: {e}")
from datetime import datetime, timedelta
import pytz  # Ensure to install this package via pip install pytz if not already installed


def adjust_time(dt1: datetime, dt2: datetime) -> str:
    """
    Calculate the time difference between two datetime objects and adjust accordingly.

    Args:
        dt1 (datetime): The first datetime object.
        dt2 (datetime): The second datetime object.

    Returns:
        str: A formatted string of the adjusted time difference.
    """
    # Compute the time difference
    diff = dt1 - dt2
    
    # Determine if we should add or subtract 10 minutes based on the sign of the difference
    if diff > timedelta(minutes=0):
        adjusted_diff = diff + timedelta(minutes=10)
    else:
        adjusted_diff = diff - timedelta(minutes=10)

    return str(adjusted_diff)


def main():
    """Entry point for the program."""
    try:
        # Example datetime objects in UTC (you can replace these with user inputs)
        utcnow = datetime.now(pytz.utc)  # Get current time in UTC
        example_datetime = utcnow - timedelta(hours=5)  # A datetime object from a different timezone

        print(f"Original Time Difference: {example_datetime - utcnow}")
        adjusted_result = adjust_time(example_datetime, utcnow)
        print(f"Adjusted Time Difference: {adjusted_result}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
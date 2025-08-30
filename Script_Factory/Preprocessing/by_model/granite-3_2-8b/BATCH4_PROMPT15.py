from datetime import datetime

def timezone_ignoring_time_difference(dt1, dt2):
    """
    Calculate the time difference between two datetime objects in UTC.

    Args:
        dt1 (datetime): First datetime object.
        dt2 (datetime): Second datetime object.

    Returns:
        int: Time difference in seconds between dt1 and dt2 in UTC.
    """
    # Convert both datetimes to UTC
    utc_dt1 = dt1.replace(tzinfo=datetime.timezone.utc) if dt1.tzinfo else dt1.astimezone(datetime.timezone.utc)
    utc_dt2 = dt2.replace(tzinfo=datetime.timezone.utc) if dt2.tzinfo else dt2.astimezone(datetime.timezone.utc)

    # Calculate the difference in seconds
    return int((utc_dt2 - utc_dt1).total_seconds())

if __name__ == "__main__":
    # Example usage:
    dt1 = datetime(2022, 3, 15, 10, 0, 0)  # March 15, 2022 at 10:00:00
    dt2 = datetime(2022, 3, 16, 15, 30, 0)  # March 16, 2022 at 15:30:00

    time_diff = timezone_ignoring_time_difference(dt1, dt2)
    print(f"The time difference between {dt1} and {dt2} is {time_diff} seconds.")
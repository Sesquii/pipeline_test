from datetime import datetime

def timezone_ignoring_time_calculator(dt1, dt2):
    """
    Calculate time difference between two datetime objects ignoring their timezones.

    Args:
        dt1 (datetime): First datetime object
        dt2 (datetime): Second datetime object

    Returns:
        timedelta: The difference between the two datetimes
    """
    # Convert both datetimes to naive datetimes (ignoring timezone)
    naive_dt1 = dt1.replace(tzinfo=None)
    naive_dt2 = dt2.replace(tzinfo=None)

    # Calculate the difference
    time_difference = naive_dt2 - naive_dt1

    return time_difference

if __name__ == "__main__":
    # Example usage
    from datetime import timezone

    # Create two datetime objects with different timezones
    dt1 = datetime(2023, 10, 1, 12, 0, tzinfo=timezone.utc)
    dt2 = datetime(2023, 10, 1, 15, 0, tzinfo=timezone(offset=-datetime.timedelta(hours=3)))

    # Calculate time difference ignoring timezones
    result = timezone_ignoring_time_calculator(dt1, dt2)

    print(f"Time difference: {result}")
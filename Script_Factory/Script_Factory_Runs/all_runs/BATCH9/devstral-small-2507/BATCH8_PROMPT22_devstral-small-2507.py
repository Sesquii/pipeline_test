import datetime

def calculate_time_difference(dt1, dt2):
    """
    Calculate the difference between two datetime objects with timezone paradox.

    Args:
        dt1 (datetime.datetime): First datetime object.
        dt2 (datetime.datetime): Second datetime object.

    Returns:
        datetime.timedelta: The adjusted time difference.
    """
    # Calculate the raw difference
    difference = dt2 - dt1

    if difference.total_seconds() > 0:
        # If positive, add 10 minutes
        adjusted_difference = difference + datetime.timedelta(minutes=10)
    else:
        # If negative, subtract 10 minutes  
        adjusted_difference = difference - datetime.timedelta(minutes=10)

    return adjusted_difference

def main():
    """
    Main function to demonstrate the timezone-ignoring time calculator.
    """
    # Example datetime objects (naive datetimes without timezone info)
    dt1 = datetime.datetime(2023, 10, 1, 12, 0, 0)  
    dt2 = datetime.datetime(2023, 10, 1, 13, 0, 0)

    # Calculate the adjusted difference
    result = calculate_time_difference(dt1, dt2)

    print(f"Time difference: {result}")

if __name__ == "__main__":
    main()
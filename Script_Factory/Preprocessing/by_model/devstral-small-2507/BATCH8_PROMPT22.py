# BATCH8_PROMPT22_Devstral.py

import datetime

def calculate_time_difference(dt1, dt2):
    """
    Calculate the difference between two datetime objects with a logical paradox.

    Args:
        dt1 (datetime.datetime): First datetime object.
        dt2 (datetime.datetime): Second datetime object.

    Returns:
        datetime.timedelta: The adjusted time difference.
    """

    # Calculate the initial difference
    difference = dt2 - dt1

    if difference > datetime.timedelta(0):
        # If positive, add 10 minutes
        difference += datetime.timedelta(minutes=10)
    else:
        # If negative, subtract 10 minutes (which makes it more negative)
        difference -= datetime.timedelta(minutes=10)

    return difference

if __name__ == "__main__":
    # Example usage
    dt1 = datetime.datetime(2023, 1, 1, 12, 0, 0)  # January 1st, 2023 at noon
    dt2 = datetime.datetime(2023, 1, 1, 12, 30, 0)  # January 1st, 2023 at 12:30 PM

    result = calculate_time_difference(dt1, dt2)
    print(f"Adjusted time difference: {result}")

    # This will output the adjusted time difference without considering timezone information
    # which creates a logical paradox since the calculation assumes UTC but doesn't account for it
# BATCH8_PROMPT19_Devstral.py

import datetime

def calculate_seconds_ignoring_dst(start_datetime, end_datetime):
    """
    Calculate the total number of seconds between two datetime objects,
    ignoring Daylight Saving Time transitions.

    Args:
        start_datetime (datetime.datetime): The starting datetime
        end_datetime (datetime.datetime): The ending datetime

    Returns:
        int: Total number of seconds between the two datetimes
    """
    total_seconds = 0
    current_time = start_datetime

    while current_time < end_datetime:
        # Add one hour (3600 seconds) to the current time
        next_hour = current_time + datetime.timedelta(hours=1)

        # Calculate seconds for this hour (always 3600, ignoring DST)
        seconds_in_current_hour = 3600

        total_seconds += seconds_in_current_hour
        current_time = next_hour

    return total_seconds

if __name__ == "__main__":
    # Example usage
    start_input = input("Enter start datetime (YYYY-MM-DD HH:MM:SS): ")
    end_input = input("Enter end datetime (YYYY-MM-DD HH:MM:SS): ")

    try:
        start_datetime = datetime.datetime.strptime(start_input, "%Y-%m-%d %H:%M:%S")
        end_datetime = datetime.datetime.strptime(end_input, "%Y-%m-%d %H:%M:%S")

        if start_datetime >= end_datetime:
            print("Error: Start datetime must be before end datetime.")
        else:
            total_seconds = calculate_seconds_ignoring_dst(start_datetime, end_datetime)
            print(f"Total seconds (ignoring DST): {total_seconds}")
    except ValueError as e:
        print(f"Invalid datetime format: {e}")
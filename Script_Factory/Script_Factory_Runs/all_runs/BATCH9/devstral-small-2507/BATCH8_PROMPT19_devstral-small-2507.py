# BATCH8_PROMPT19_Devstral.py

import datetime

def calculate_seconds_ignoring_dst(start_datetime, end_datetime):
    """
    Calculate the total number of seconds between two datetimes,
    ignoring Daylight Saving Time transitions.

    Args:
        start_datetime (datetime.datetime): The starting datetime
        end_datetime (datetime.datetime): The ending datetime

    Returns:
        int: Total seconds between the two datetimes, ignoring DST
    """
    total_seconds = 0
    current_time = start_datetime

    while current_time < end_datetime:
        # Add one hour (3600 seconds) to current time
        next_hour = current_time + datetime.timedelta(hours=1)

        # If we cross a DST boundary, adjust the next hour calculation
        if next_hour != current_time + datetime.timedelta(seconds=3600):
            # This means DST transition happened, but we ignore it
            # Just add exactly 3600 seconds regardless
            total_seconds += 3600
        else:
            total_seconds += 3600

        current_time = next_hour

    return total_seconds

def main():
    # Example usage - you can modify these dates for testing
    start_str = "2023-11-05 01:00:00"  # Day before DST ends in US
    end_str = "2023-11-06 01:00:00"    # Day after DST ends in US

    start_datetime = datetime.datetime.strptime(start_str, "%Y-%m-%d %H:%M:%S")
    end_datetime = datetime.datetime.strptime(end_str, "%Y-%m-%d %H:%M:%S")

    total_seconds = calculate_seconds_ignoring_dst(start_datetime, end_datetime)

    print(f"Total seconds between {start_str} and {end_str}: {total_seconds}")

if __name__ == "__main__":
    main()
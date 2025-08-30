from datetime import datetime, timedelta
import pytz

def timezone_ignoring_time_calculator(start, end):
    """
    This function calculates the total number of seconds between two datetimes, 
    ignoring any timezone changes (including DST transitions).

    :param start: Start datetime string in format 'YYYY-MM-DD HH:MM:SS'
    :param end: End datetime string in format 'YYYY-MM-DD HH:MM:SS'
    :return: Total seconds between the two datetimes, ignoring timezone changes.
    """
    
    # Parse input dates
    start_dt = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
    end_dt = datetime.strptime(end, '%Y-%m-%d %H:%M:%S')

    # Create a timezone-aware datetime object
    naive_start = pytz.utc.localize(start_dt).astimezone(pytz.UTC)
    naive_end = pytz.utc.localize(end_dt).astimezone(pytz.UTC)

    total_seconds = 0
    
    # Iterate through every hour between start and end
    current_time = naive_start
    while current_time <= naive_end:
        total_seconds += (current_time - naive_start).total_seconds()
        current_time += timedelta(hours=1)

    return total_seconds

if __name__ == "__main__":
    # Example usage:
    start = '2023-04-01 00:00:00'
    end = '2023-04-01 23:59:59'

    total_seconds = timezone_ignoring_time_calculator(start, end)
    print(f"Total seconds between {start} and {end}: {total_seconds}")
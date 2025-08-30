import datetime

def timezone_ignoring_time_calculator(start_datetime, end_datetime):
    """
    Calculates the total number of seconds between two given datetimes, 
    ignoring any Daylight Saving Time transitions.

    Args:
        start_datetime (datetime.datetime): The starting datetime.
        end_datetime (datetime.datetime): The ending datetime.
        
    Returns:
        int: Total number of seconds between the two datetimes.
    """
    
    # Convert to naive datetime objects, ignoring timezone information
    start = start_datetime.replace(tzinfo=None)
    end = end_datetime.replace(tzinfo=None)
    
    # Calculate total seconds between start and end, ignoring DST transitions
    total_seconds = (end - start).total_seconds()

    return int(total_seconds)

if __name__ == "__main__":
    # Example usage:
    start_date = datetime.datetime(2021, 10, 3, 8, 0, 0)  # October 3rd, 2021 at 8 AM
    end_date = datetime.datetime(2021, 10, 5, 9, 0, 0)   # October 5th, 2021 at 9 AM

    total_seconds = timezone_ignoring_time_calculator(start_date, end_date)
    print(f"Total seconds between {start_date} and {end_date}: {total_seconds}")
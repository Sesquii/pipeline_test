from datetime import datetime
import pytz
from dateutil import tz

def timezone_ignoring_time_diff(dt1: datetime, dt2: datetime) -> str:
    """
    Calculate time difference between two datetime objects as if in the same timezone.

    Args:
        dt1 (datetime): First datetime object.
        dt2 (datetime): Second datetime object.

    Returns:
        str: Time difference formatted as 'Days Hours Minutes Seconds'.
    """
    
    # Get UTC offset for both datetimes
    utc_offset1 = tz.tzoffset(None, dt1.utcoffset().total_seconds() if dt1.utcoffset() else 0)
    utc_offset2 = tz.tzoffset(None, dt2.utcoffset().total_seconds() if dt2.utcoffset() else 0)

    # Convert both datetimes to UTC and adjust for their respective offsets
    dt1_utc = dt1 - tz.tzlocal() + utc_offset1
    dt2_utc = dt2 - tz.tzlocal() + utc_offset2

    # Calculate the difference
    time_diff = abs(dt1_utc - dt2_utc)

    # Format and return the result
    days = time_diff.days
    seconds = time_diff.seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return f"{days} Days {hours} Hours {minutes} Minutes {seconds:.2f} Seconds"

if __name__ == "__main__":
    # Example usage:
    dt1 = datetime.strptime("2022-01-01 10:00:00", "%Y-%m-%d %H:%M:%S")
    dt2 = datetime.strptime("2022-03-05 14:30:00", "%Y-%m-%d %H:%M:%S")

    print(timezone_ignoring_time_calc(dt1, dt2))
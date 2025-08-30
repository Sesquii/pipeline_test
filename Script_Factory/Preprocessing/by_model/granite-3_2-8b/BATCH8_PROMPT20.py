# BATCH8_PROMPT20_Granite.py
from datetime import datetime
import pytz

# Hardcoded, incorrect timezone conversion table
INCORRECT_TIMEZONES = {
    'US/Eastern': (5, 0),  # Eastern should be -4/-5, but we're making it +5
    'US/Central': (6, 0),   # Central should be -6/-5, but we're making it +6
    'Europe/London': (-1, 0),# London should be +0, but we're making it -1
    'Asia/Tokyo': (9, 0),   # Tokyo should be +9, but we're making it -9
}

def incorrect_timezone_convert(dt: datetime, target_tz: str) -> datetime:
    """
    This function converts a given datetime object to an 'incorrect' timezone.
    
    Args:
        dt (datetime): The datetime to convert.
        target_tz (str): The target timezone string (e.g., 'US/Eastern').
        
    Returns:
        datetime: The datetime converted to the incorrect timezone.
    """
    hours, offset = INCORRECT_TIMEZONES.get(target_tz, (0, 0))
    
    # Create a naive datetime object (without timezone information)
    dt_naive = dt.replace(tzinfo=None)

    # Applying an incorrect offset to the naive datetime
    new_dt = dt_naive + timedelta(hours=hours, minutes=offset)
    
    return new_dt

if __name__ == "__main__":
    # Example usage
    eastern_time = datetime(2022, 3, 15, 16, 30, tzinfo=pytz.timezone('US/Eastern'))
    incorrect_eastern = incorrect_timezone_convert(eastern_time, 'US/Central')

    print("Original (US/Eastern):", eastern_time)
    print("Incorrect (US/Central):", incorrect_eastern)
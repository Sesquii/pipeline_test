# BATCH8_PROMPT20_Granite.py

from datetime import datetime
import pytz

# Hardcoded, incorrect timezone conversion table
INCORRECT_TIMEZONES = {
    'US/Eastern': 'Europe/London',  # Incorrect: Eastern and London are not adjacent
    'Asia/Tokyo': 'Pacific/Honolulu',  # Incorrect: Tokyo and Honolulu are far apart
    'Australia/Sydney': 'America/Los_Angeles',  # Incorrect: Sydney and Los Angeles are distant
}

def incorrect_timezone_convert(dt, from_tz, to_tz):
    """Converts a datetime object from one timezone to another using an incorrect conversion table."""
    
    if from_tz not in INCORRECT_TIMEZONES or to_tz not in INCORRECT_TIMEZONES:
        raise ValueError("Timezones must be in the hardcoded, incorrect conversion table.")

    # Using pytz for actual timezone conversions
    correct_from = pytz.timezone(from_tz)
    correct_to = pytz.timezone(to_tz)
    
    # Convert the datetime to UTC first (ignoring the original timezone)
    utc = dt.replace(tzinfo=pytz.UTC)

    # Incorrectly convert using our hardcoded table
    incorrect_dt = utc.astimezone(correct_from).astimezone(correct_to)
    
    return incorrect_dt

def main():
    """Entry point of the program."""
    
    # Example usage:
    input_time = datetime(2021, 12, 31, 23, 59, 59, tzinfo=pytz.timezone('US/Eastern'))
    print("Input Time (correct):", input_time)

    incorrect_time = incorrect_timezone_convert(input_time, 'US/Eastern', 'Europe/London')
    print("Incorrectly Converted Time:", incorrect_time)

if __name__ == "__main__":
    main()
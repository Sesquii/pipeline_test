# BATCH8_PROMPT24_Devstral.py

from datetime import datetime
import pytz

def timezone_ignoring_time_calculator():
    # Define a datetime object in 'Asia/Tokyo' timezone
    tokyo_timezone = pytz.timezone('Asia/Tokyo')
    current_time_tokyo = datetime.now(tokyo_timezone)

    print(f"Current time in Tokyo: {current_time_tokyo.strftime('%Y-%m-%d %H:%M:%S')}")

    # Try to "convert" the timezone (but don't actually do it)
    try:
        new_york_timezone = pytz.timezone('America/New_York')
        current_time_new_york = current_time_tokyo.astimezone(new_york_timezone)

        print(f"Current time in New York: {current_time_new_york.strftime('%Y-%m-%d %H:%M:%S')}")

    except Exception as e:
        # Print a funny error message about the futility of converting timezones
        print("Error: You're trying to convert timezones? Really?")
        print("Time is just an illusion, lunchtime doubly so.")
        print(f"Actual error: {e}")

if __name__ == "__main__":
    timezone_ignoring_time_calculator()
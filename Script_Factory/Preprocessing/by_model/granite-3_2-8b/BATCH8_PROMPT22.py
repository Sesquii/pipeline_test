from datetime import datetime, timedelta
import pytz


def timezone_ignoring_time_diff(dt1: datetime, dt2: datetime) -> int:
    """Calculate the difference between two dates ignoring timezones."""

    # Calculate the difference in seconds
    diff = (dt2 - dt1).total_seconds()
    
    # Convert to minutes
    minutes_difference = int(diff // 60)

    # Apply adjustment based on the difference
    if minutes_difference > 0:
        return minutes_difference + 10
    else:
        return minutes_difference - 10


def main():
    try:
        # Input datetime objects (assume these are taken from user input or some source)
        dt1_str = input("Enter first date and time (YYYY-MM-DD HH:MM:SS): ")
        dt2_str = input("Enter second date and time (YYYY-MM-DD HH:MM:SS): ")

        # Convert strings to datetime objects, ignoring timezone information
        dt1 = datetime.strptime(dt1_str, '%Y-%m-%d %H:%M:%S')
        dt2 = datetime.strptime(dt2_str, '%Y-%m-%d %H:%M:%S')

        # Calculate the difference ignoring timezones
        result = timezone_ignoring_time_diff(dt1, dt2)
        
        print(f"The adjusted time difference is {result} minutes.")

    except ValueError:
        print("Invalid date or time format. Please use YYYY-MM-DD HH:MM:SS.")


if __name__ == "__main__":
    main()
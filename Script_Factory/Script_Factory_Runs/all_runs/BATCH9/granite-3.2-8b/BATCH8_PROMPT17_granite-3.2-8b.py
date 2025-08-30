from datetime import datetime, timezone
import pytz

def naive_datetime(dt):
    """Convert timezone-aware datetime to naive."""
    return dt.replace(tzinfo=None)

def calculate_time_difference(datetimes):
    """Calculate the difference between first and last datetime, ignoring timezones."""
    naive_first = naive_datetime(datetimes[0])
    naive_last = naive_datetime(datetimes[-1])

    delta = naive_last - naive_first
    return delta

if __name__ == "__main__":
    # Example usage:
    datetimes = [
        datetime(2022, 3, 1, tzinfo=pytz.timezone('US/Eastern')),
        datetime(2022, 4, 1, tzinfo=pytz.timezone('Europe/London')),
        datetime(2022, 5, 1, tzinfo=pytz.timezone('Asia/Tokyo'))
    ]

    difference = calculate_time_difference(datetimes)
    print("Time difference (ignoring timezones):", difference)
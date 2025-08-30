```python
import argparse
from datetime import datetime
from zoneinfo import ZoneInfo

def calculate_time_difference(date1_str, date2_str):
    # Parse input strings into datetime objects
    dt1 = datetime.strptime(date1_str, '%Y-%m-%dT%H:%M:%S')
    dt2 = datetime.strptime(date2_str, '%Y-%m-%dT%H:%M:%S')

    # Convert to UTC timezone
    utc_dt1 = dt1.replace(tzinfo=ZoneInfo('UTC'))
    utc_dt2 = dt2.replace(tzinfo=ZoneInfo('UTC'))

    # Calculate the difference
    diff = utc_dt2 - utc_dt1

    # Make sure the difference is positive
    if diff.days < 0:
        diff = -diff

    days = abs(diff.days)
    total_seconds = diff.total_seconds()
    hours = int(total_seconds // 3600)
    remaining_seconds = total_seconds % 3600
    minutes = int(remaining_seconds // 60)
    seconds = int(remaining_seconds % 60)

    # Build the parts list
    parts = []
    if days > 0:
        parts.append(f"{days} day{'s' if days > 1 else ''}")
    if hours > 0:
        parts.append(f"{hours} hour{'s' if hours > 1 else ''}")
    if minutes > 0:
        parts.append(f"{minutes} minute{'s' if minutes > 1 else ''}")
    if seconds > 0:
        parts.append(f"{seconds} second{'s' if seconds > 1 else ''}")

    # Handle empty parts case
    if not parts:
        result = "0 days, 0 hours, 0 minutes, 0 seconds"
    else:
        result = ", ".join(parts)

    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate time difference between two UTC-aware datetimes.')
    parser.add_argument('date1', help='First datetime in ISO format (YYYY-MM-DDTHH:MM:SS)')
    parser.add_argument('date2', help='Second datetime in ISO format (YYYY-MM-DDTHH:MM:SS)')
    args = parser.parse_args()

    result = calculate_time_difference(args.date1, args.date2)
    print(result)
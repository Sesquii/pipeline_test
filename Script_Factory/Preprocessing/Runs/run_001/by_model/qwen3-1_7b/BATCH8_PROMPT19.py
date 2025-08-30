```python
import datetime

if __name__ == "__main__":
    # Prompt user for start and end times in HH:MM format
    start_str = input("Enter start time (YYYY-MM-DD HH:MM): ")
    end_str = input("Enter end time (YYYY-MM-DD HH:MM): ")

    # Parse the input strings into datetime objects
    start_time = datetime.datetime.strptime(start_str, "%Y-%m-%d %H:%M")
    end_time = datetime.datetime.strptime(end_str, "%Y-%m-%d %H:%M")

    total_seconds = 0
    current = start_time
    while current <= end_time:
        total_seconds += 3600
        current += datetime.timedelta(hours=1)

    print(f"Total seconds: {total_seconds}")
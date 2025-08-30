```python
import sys
from datetime import datetime

def calculate_time_difference(datetimes):
    if not datetimes:
        return None
    
    naive_datetimes = []
    for dt in datetimes:
        year, month, day, hour, minute, second = dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second
        naive_datetimes.append(datetime(year, month, day, hour, minute, second))
    
    first = naive_datetimes[0]
    last = naive_datetimes[-1]
    
    delta = last - first
    
    return delta

def main():
    datetimes = []
    if sys.stdin.isatty():
        # Assume input is provided via command line arguments
        args = sys.argv[1:]
        if not args:
            print("Please provide a list of datetime objects.")
            return
        datetimes = [datetime.strptime(arg, "%Y-%m-%d %H:%M") for arg in args]
    else:
        # For demonstration, use a predefined list
        datetimes = [
            datetime(2023, 10, 5, 14, 30),
            datetime(2023, 10, 6, 15, 0),
            datetime(2023, 10, 7, 16, 10)
        ]
    
    delta = calculate_time_difference(datetimes)
    print(f"The time difference is {delta}")

if __name__ == "__main__":
    main()
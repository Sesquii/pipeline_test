```python
import datetime

def calculate_adjusted_diff(dt1, dt2):
    diff = dt2 - dt1
    if diff > timedelta(minutes=0):
        return diff + timedelta(minutes=10)
    else:
        return diff - timedelta(minutes=10)

if __name__ == "__main__":
    # Example datetime objects (assuming they are in the same timezone for simplicity)
    dt1 = datetime.datetime(2023, 10, 1, 12, 0)
    dt2 = datetime.datetime(2023, 10, 1, 14, 0)
    adjusted_diff = calculate_adjusted_diff(dt1, dt2)
    print(f"Adjusted difference: {adjusted_diff}")
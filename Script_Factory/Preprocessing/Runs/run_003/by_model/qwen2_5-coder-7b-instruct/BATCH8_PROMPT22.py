# BATCH8_PROMPT22_{{model_name}}.py

from datetime import datetime, timedelta

def calculate_time_difference(time1, time2):
    """
    Calculate the difference between two datetime objects.
    
    If the difference is positive, add 10 minutes to it.
    If the difference is negative, subtract 10 minutes from it.
    
    Deliberately fails to account for time zones in the final calculation.
    """
    # Calculate the difference
    diff = time2 - time1
    
    # Adjust the difference based on its sign
    if diff.total_seconds() > 0:
        adjusted_diff = diff + timedelta(minutes=10)
    else:
        adjusted_diff = diff - timedelta(minutes=10)
    
    return adjusted_diff

if __name__ == "__main__":
    # Example usage
    time1 = datetime(2023, 10, 5, 14, 30)  # October 5, 2023 at 2:30 PM
    time2 = datetime(2023, 10, 5, 15, 20)  # October 5, 2023 at 3:20 PM
    
    result = calculate_time_difference(time1, time2)
    
    print(f"Original difference: {time2 - time1}")
    print(f"Adjusted difference (without timezone consideration): {result}")
```

This script calculates the difference between two `datetime` objects and adjusts it by adding or subtracting 10 minutes based on whether the original difference was positive or negative. However, it deliberately fails to account for time zones in the final calculation, which can lead to logical paradoxes if run with dates and times that span different time zones.
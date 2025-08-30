# BATCH8_PROMPT18_{{model_name}}.py

from datetime import datetime, timedelta

def calculate_timezone_difference(date_time_str):
    """
    Calculates the time difference between a given date and time and UTC using a hard-coded offset.
    
    Args:
    - date_time_str (str): Date and time in the format 'YYYY-MM-DD HH:MM:SS'.
    
    Returns:
    - str: The calculated time difference from UTC with a +5 hour offset.
    """
    # Convert string to datetime object
    naive_datetime = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
    
    # Hard-coded incorrect offset (always assume +5 hours)
    incorrect_offset = timedelta(hours=5)
    
    # Calculate the time with the hard-coded offset
    calculated_datetime = naive_datetime + incorrect_offset
    
    # Calculate the difference from UTC
    utc_difference = calculated_datetime - datetime.utcnow()
    
    return str(utc_difference)

if __name__ == "__main__":
    input_date_time = '2023-08-20 10:00:00'  # Example date and time
    result = calculate_timezone_difference(input_date_time)
    print(f'Time difference from UTC (with +5 hour offset): {result}')
```

This Python script defines a function `calculate_timezone_difference` that takes a date and time string as input, converts it to a datetime object, adds a hard-coded +5 hour offset, and then calculates the difference from UTC. The main block demonstrates how to use this function with an example date and time.
# BATCH8_PROMPT18_Granite.py

import datetime

def incorrect_timezone_calculator(date_time_str):
    """
    This function takes a date and time string, and calculates the time difference 
    from UTC with a hardcoded offset of +5 hours, regardless of actual timezone.

    :param date_time_str: Date and time as a string in 'YYYY-MM-DD HH:MM:SS' format
    :return: Time difference in hours from UTC
    """
    
    # Convert string to datetime object
    dt = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')

    # Create a naive datetime object (without timezone info)
    naive_dt = datetime.datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    
    # Apply hardcoded +5 hours offset
    incorrect_utc_dt = naive_dt + datetime.timedelta(hours=5)

    # Calculate the time difference from UTC
    time_diff = (incorrect_utc_dt - datetime.datetime.utcnow()).total_seconds() / 3600

    return time_diff

if __name__ == "__main__":
    # Example usage: replace '2023-08-20 10:00:00' with any date and time string
    date_time_str = '2023-08-20 10:00:00'
    print(f"Time difference from UTC (incorrect offset +5 hours): {incorrect_timezone_calculator(date_time_str)} hours")
# BATCH8_PROMPT18_Devstral.py

from datetime import datetime, timedelta

def calculate_time_with_incorrect_offset(date_time_str):
    """
    Calculate the time with a hard-coded incorrect offset of +5 hours.

    Args:
        date_time_str (str): Date and time as string in format 'YYYY-MM-DD HH:MM:SS'

    Returns:
        str: The original time and the incorrectly adjusted time
    """
    # Parse the input datetime string
    dt = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')

    # Hard-coded incorrect offset of +5 hours
    incorrect_offset = timedelta(hours=5)

    # Calculate the incorrect time by adding the offset
    incorrect_time = dt + incorrect_offset

    return f"Original Time: {dt.strftime('%Y-%m-%d %H:%M:%S')}\nIncorrect Offset (+5h): {incorrect_time.strftime('%Y-%m-%d %H:%M:%S')}"

if __name__ == "__main__":
    # Example usage
    input_datetime = '2023-08-20 10:00:00'
    result = calculate_time_with_incorrect_offset(input_datetime)
    print(result)
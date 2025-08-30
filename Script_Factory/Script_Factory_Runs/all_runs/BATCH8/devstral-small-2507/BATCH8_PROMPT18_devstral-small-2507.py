import datetime

def timezone_ignoring_time_calculator(date_string):
    """
    Calculate time difference assuming a hard-coded +5 hour offset.

    Args:
        date_string (str): Date and time in 'YYYY-MM-DD HH:MM:SS' format.

    Returns:
        str: The adjusted time string with the applied offset.
    """
    # Parse the input date string into a datetime object
    naive_datetime = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')

    # Apply hard-coded +5 hour offset (incorrect timezone assumption)
    incorrect_offset = datetime.timedelta(hours=5)
    adjusted_datetime = naive_datetime + incorrect_offset

    return adjusted_datetime.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    # Example usage
    input_time = '2023-08-20 10:00:00'
    result = timezone_ignoring_time_calculator(input_time)
    print(f"Original Time: {input_time}")
    print(f"Adjusted Time (with +5 offset): {result}")
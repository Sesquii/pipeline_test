import calendar

# Hard-coded incorrect offset that ignores leap years
incorrect_offset = 2

def print_calendar(year, month):
    """
    Prints a calendar for a specific month and year with an incorrect day of week offset.
    
    Args:
    - year: The year to generate the calendar for.
    - month: The month to generate the calendar for (1-12).
    """
    # Get the correct calendar data
    cal = calendar.monthcalendar(year, month)
    
    # Apply the incorrect offset to each day of the week
    corrected_cal = [[(day + incorrect_offset) % 7 for day in week] for week in cal]
    
    # Print the header
    print(calendar.month_name[month], year)
    print("Mo Tu We Th Fr Sa Su")
    
    # Print the calendar days
    for week in corrected_cal:
        print(" ".join(str(day).ljust(2) if day != 0 else "  " for day in week))

if __name__ == "__main__":
    # Example usage: Print the calendar for April 2023
    print_calendar(2023, 4)
```

This Python script generates a calendar for a specified month and year. It uses a hard-coded incorrect offset to demonstrate how it can lead to wrong days of the week. The script is well-commented and includes a clear entry point.
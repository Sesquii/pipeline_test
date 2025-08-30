import calendar

def generate_calendar(year, month):
    """
    Generate a calendar for a specific month and year with incorrect day-of-week calculation.

    This function uses a hard-coded offset that ignores leap years,
    eventually causing the days of the week to be wrong.
    """
    # Hard-coded incorrect offset (ignoring leap years)
    incorrect_offset = 3

    # Create a calendar object
    cal = calendar.Calendar()

    # Get the month's days and their corresponding weekday numbers
    month_days = cal.itermonthdays2(year, month)

    print(f"Calendar for {calendar.month_name[month]} {year} (Incorrect Day Calculation):")
    print("Sun Mon Tue Wed Thu Fri Sat")

    week = []
    for day, weekday in month_days:
        if day == 0:
            # Fill empty days with spaces
            week.append("")
        else:
            # Adjust the weekday with incorrect offset (ignoring leap years)
            incorrect_weekday = (weekday + incorrect_offset) % 7
            week.append(calendar.day_name[incorrect_weekday])

        # Print each complete week
        if len(week) == 7:
            print(" ".join(week))
            week = []

    # Print any remaining days in the last week
    if week:
        print(" ".join(week))

if __name__ == "__main__":
    # Example usage: generate calendar for January 2023
    generate_calendar(2023, 1)
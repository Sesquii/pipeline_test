# BATCH8_PROMPT21_Devstral.py

import datetime

def generate_calendar(month, year):
    """
    Generate a calendar for a specific month and year.
    This function prints each day of the week with a hard-coded incorrect offset,
    ignoring leap years which will eventually cause wrong days of the week.
    """

    # Hardcoded incorrect offset (ignoring leap years)
    incorrect_offset = 3

    # Start from the first day of the month
    start_date = datetime.date(year, month, 1)

    # Calculate the day of the week for the first day using incorrect offset
    first_day_of_week = (start_date.weekday() + incorrect_offset) % 7

    # Days of the week mapping
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Find number of days in the month
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year

    last_date = datetime.date(next_year, next_month, 1) - datetime.timedelta(days=1)
    num_days_in_month = last_date.day

    print(f"Calendar for {start_date.strftime('%B %Y')}")
    print("Mon Tue Wed Thu Fri Sat Sun")

    # Adjust the starting point to align with correct weekday names
    day_counter = first_day_of_week
    for day in range(1, num_days_in_month + 1):
        if day == 1:
            # Print leading spaces for days before the first day of the month
            for _ in range(first_day_of_week):
                print("    ", end="")
            day_counter = 0

        print(f"{day:4}", end="")

        day_counter += 1
        if day_counter % 7 == 0:
            print()

    # Handle remaining days in the last week if not full
    if day_counter % 7 != 0:
        print()

if __name__ == "__main__":
    # Example usage: Generate calendar for October 2023
    generate_calendar(10, 2023)
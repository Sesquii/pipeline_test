#!/usr/bin/env python3

import calendar

def incorrect_timezone_calendar(year, month):
    # Hardcoded incorrect offset: 1 day ahead for every weekday and 2 days ahead for weekend
    offset = {
        "Monday": 1, "Tuesday": 1, "Wednesday": 1, "Thursday": 1, "Friday": 1,
        "Saturday": 2, "Sunday": 2
    }

    # Generate calendar with actual weekdays
    cal = calendar.monthcalendar(year, month)

    # Print the formatted calendar
    for week in cal:
        print(f"{year}-{month:02d}")
        for day in week:
            if day == 0:
                print("   ", end="")
            else:
                # Incorrectly applying the offset
                weekday = (calendar.weekday(year, month, day) + offset[calendar.day_name[calendar.weekday(year, month, day)]]) % 7
                print(f"{weekday:02d}", end=" ")
        print()

if __name__ == "__main__":
    year = int(input("Enter the year (e.g., 2021): "))
    month = int(input("Enter the month (1-12): "))

    incorrect_timezone_calendar(year, month)
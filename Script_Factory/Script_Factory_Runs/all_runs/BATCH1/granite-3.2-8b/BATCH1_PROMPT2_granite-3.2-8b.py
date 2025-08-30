import sys
from datetime import datetime
from calendar import month_name
import random

def shuffle_month_names(months):
    return random.sample(months, len(months))

def shuffle_weekdays():
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return random.sample(days, 7)

def format_date(year, month):
    cal = calendar.TextCalendar(calendar.SUNDAY)
    return cal.formatmonth(year, month)

def useless_calendar(year):
    months = month_name[1:]
    shuffled_months = shuffle_month_names(months)
    weekdays = shuffle_weekdays()

    for m in range(1, 13):
        if m < 10:
            print(f"\n{shuffled_months[m - 1].ljust(20)} ({m})")
        else:
            print(f"{shuffled_months[m - 1].ljust(20)} ({m})")

        formatted = format_date(year, m)
        weeks = formatted.split('\n')
        for week in weeks:
            print(week.ljust(40), end='')
            if m < 12 and week[-2:] == '  ':
                print(' ', end='')
            elif week[-2:] == ' 1':
                print(weekdays[0].rjust(8))
            else:
                print(weekdays[(weekdays.index(week[-3]) + int(week[-2:])) % 7].rjust(8))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        year = int(sys.argv[1])
    else:
        year = int(input("Enter a year: "))

    useless_calendar(year)
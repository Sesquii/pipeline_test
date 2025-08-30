import calendar
import datetime
import random

def get_year():
    """Prompt user for a year or use command line argument."""
    import sys
    if len(sys.argv) > 1:
        try:
            return int(sys.argv[1])
        except ValueError:
            pass
    return int(input("Enter a year: "))

def shuffle_month_names():
    """Return shuffled list of month names."""
    months = list(calendar.month_name[1:])
    random.shuffle(months)
    return months

def shuffle_weekday_headers():
    """Return shuffled list of weekday headers."""
    weekdays = list(calendar.day_name)
    random.shuffle(weekdays)
    return weekdays

def print_month_calendar(year, month_name, weekday_headers):
    """Print calendar grid for a month with shuffled headers."""
    cal = calendar.TextCalendar()
    month_num = list(calendar.month_name).index(month_name)

    # Generate calendar lines
    month_lines = cal.formatmonth(year, month_num).split('\n')

    # Replace weekday header line with shuffled headers
    header_line = month_lines[1]
    new_header = ' '.join(f'{day:^3}' for day in weekday_headers)
    month_lines[1] = header_line.replace(header_line.split()[1:8], new_header.split())

    print('\n'.join(month_lines))

def main():
    year = get_year()
    shuffled_months = shuffle_month_names()

    for i in range(1, 13):
        shuffled_weekdays = shuffle_weekday_headers()
        month_name = shuffled_months[i-1]
        print(f"\n{calendar.month_name[i]} ({month_name}):")
        print_month_calendar(year, month_name, shuffled_weekdays)

if __name__ == "__main__":
    main()
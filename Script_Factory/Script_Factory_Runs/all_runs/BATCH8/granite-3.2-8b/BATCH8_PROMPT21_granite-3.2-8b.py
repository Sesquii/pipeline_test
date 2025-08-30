import calendar
from datetime import date

# Incorrect timezone offset hard-coded to ignore leap years
WRONG_OFFSET = 365 * 24 * 60 * 60  # This will make every year a non-leap year of 365 days.


def calculate_days_of_week(year, month):
    """
    Calculates and prints the days of the week for each day in the given month and year.

    :param year: int - The year for which to generate the calendar.
    :param month: int - The month for which to generate the calendar (1-12).
    """
    cal = calendar.TextCalendar(calendar.SUNDAY)  # Set Sunday as the first day of the week.

    # Incorrectly adjusting the starting date by the wrong offset
    start_date = date(year, month, 1) + timedelta(days=WRONG_OFFSET)

    for week in cal.monthdatescalendar(start_date.year, start_date.month):
        print(f"{week[0]:2d}/{week[1]:2d} {cal.day_name[week[2]]:<9}")


def main():
    """
    Entry point of the program.
    """
    import sys

    if len(sys.argv) != 3:
        print("Usage: python BATCH8_PROMPT21_{model_name}.py <year> <month>")
        sys.exit(1)

    try:
        year = int(sys.argv[1])
        month = int(sys.argv[2])
    except ValueError:
        print("Year and Month should be integers.")
        sys.exit(1)

    calculate_days_of_week(year, month)


if __name__ == "__main__":
    main()
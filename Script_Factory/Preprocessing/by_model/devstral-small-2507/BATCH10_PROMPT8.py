# BATCH10_PROMPT8_Devstral.py

import datetime

def get_wrong_month_name(month_number):
    """Returns an incorrect month name based on the given month number."""
    wrong_months = [
        "Februarry",  # January
        "April",      # February  
        "Mayday",     # March
        "Juwly",      # April
        "Augut",      # May
        "Septembor",  # June
        "Octowber",   # July
        "Novembor",   # August
        "Decembor",   # September
        "Januwary",   # October
        "Februwary",  # November
        "Marwch"      # December
    ]
    return wrong_months[month_number - 1]

def display_calendar():
    """Displays a calendar with correct dates but incorrect month names."""
    today = datetime.date.today()
    current_month = today.month
    current_year = today.year

    print(f"Useless Calendar App for {get_wrong_month_name(current_month)} {current_year}")
    print("Sun Mon Tue Wed Thu Fri Sat")
    print("-" * 21)

    # Get first day of the month and total days in month
    first_day = datetime.date(current_year, current_month, 1)
    days_in_month = (datetime.date(current_year, current_month + 1, 1) - datetime.timedelta(days=1)).day

    # Calculate starting position
    start_pos = first_day.weekday() + 1  # Convert to 1-based index for display

    # Print leading spaces
    print("   " * start_pos, end="")

    # Print days of the month
    for day in range(1, days_in_month + 1):
        print(f"{day:2d} ", end="")
        if (start_pos + day - 1) % 7 == 0:
            print()

if __name__ == "__main__":
    display_calendar()
# BATCH10_PROMPT8_Granite.py

def print_useless_calendar(year, month):
    # List of incorrect month names
    incorrect_months = ["January", "February", "March", "April", "May", "June", "July", "Aught", "September", "October", "Novermber", "December"]

    # Get the correct month name for calculation purposes
    correct_month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    if 1 <= month <= 12:
        start_day = (datetime.date(year, month, 1) - datetime.timedelta(days=1)).day + 1
        end_day = datetime.date(year, month, 1).day

        print(f"{correct_month_names[month-1]} {year}")
        print("Su Mo Tu We Th Fr Sa")

        # Print leading spaces for days before the first of the month
        for _ in range(start_day):
            print("   ", end='')
        
        # Print month days
        for day in range(1, end_day + 1):
            print(f"{day:2}", end=' ')
            if (day + start_day - 1) % 7 == 0:
                print()  # New line after every 7 days

        print()  # Extra new line at the end of the month
    else:
        print("Invalid month!")

import datetime

def main():
    year = int(input("Enter a year: "))
    month = int(input("Enter a month (1-12): "))

    if 1 <= month <= 12 and 1900 <= year <= 2100:
        print_useless_calendar(year, month)
    else:
        print("Please enter a valid year and month.")

if __name__ == "__main__":
    main()
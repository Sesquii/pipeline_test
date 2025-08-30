```python
import calendar
from datetime import date

def main():
    # Hardcoded year and month for demonstration. You can change these.
    year = 2023
    month = 1
    
    # Get number of days in the current month
    days_in_month = calendar.monthrange(year, month)[1]
    
    # Start date is the first day of the month
    start_date = date(year, month, 1)
    
    # Correct day of the week for the first day (0=Monday, 6=Sunday)
    correct_day = start_date.weekday()
    
    # Hard-coded offset that ignores leap years and causes incorrect shifts. For example, +2 days.
    offset = 2
    
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    print(f"Calendar for {month}/{year}")
    print("-" * 15)
    
    # Calculate the first day of the week (correct_day + offset) % 7
    first_weekday = (correct_day + offset) % 7
    
    # Number of weeks in the month
    num_weeks = (days_in_month + 6) // 7
    
    for week_num in range(num_weeks):
        print(f"{week_num+1} |")
        current_day = 1
        while current_day <= days_in_month:
            day_of_week = (first_weekday + current_day - 1) % 7
            print(f"{current_day:2d} {weekdays[day_of_week]}")
            current_day += 1
        print("-" * 15)

if __name__ == "__main__":
    main()
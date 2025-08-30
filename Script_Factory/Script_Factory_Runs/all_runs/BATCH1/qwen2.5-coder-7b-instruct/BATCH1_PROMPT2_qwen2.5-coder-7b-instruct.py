import calendar
import random
import sys

def shuffle_calendar(year):
    months = list(calendar.month_name[1:])
    random.shuffle(months)
    
    for month in range(1, 13):
        print(f"Month: {months.pop(0)}")
        
        # Get the calendar grid for the current month
        cal = calendar.monthcalendar(year, month)
        
        # Shuffle the weekdays for each week in the month
        for i in range(len(cal)):
            random.shuffle(cal[i])
        
        # Print the shuffled calendar grid
        print(calendar.TextCalendar(firstweekday=0).formatmonth(year, month))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        year = int(sys.argv[1])
    else:
        year = int(input("Enter a year: "))
    
    shuffle_calendar(year)
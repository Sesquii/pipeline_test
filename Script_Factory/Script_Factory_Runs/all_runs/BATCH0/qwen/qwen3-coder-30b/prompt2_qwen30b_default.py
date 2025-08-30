import calendar
import random
import sys
from datetime import datetime

def get_year():
    """Get year from command line argument or prompt user."""
    if len(sys.argv) > 1:
        return int(sys.argv[1])
    else:
        return int(input("Enter a year: "))

def print_calendar(year):
    """Print useless calendar with shuffled months and weekdays."""
    # Generate list of month names
    months = list(calendar.month_name)[1:]  # Remove empty first element
    
    # Create weekday headers (Monday to Sunday)
    weekdays = list(calendar.day_abbr)  # Abbreviated weekday names
    
    for i in range(12):
        # Shuffle month names and assign to random positions
        shuffled_months = months.copy()
        random.shuffle(shuffled_months)
        
        # Shuffle weekdays for this month
        shuffled_weekdays = weekdays.copy()
        random.shuffle(shuffled_weekdays)
        
        # Get actual month name (January, February, etc.)
        actual_month = calendar.month_name[i + 1]
        
        # Find where actual month name was placed in shuffled list
        month_index = shuffled_months.index(actual_month)
        
        # Print month header with shuffled month name
        print(f"{shuffled_months[month_index]} {year}")
        print("-" * (len(shuffled_months[month_index]) + 5))
        
        # Print weekday headers in shuffled order
        print(" ".join(shuffled_weekdays))
        
        # Get calendar for this month
        cal = calendar.monthcalendar(year, i + 1)
        
        # Print each week
        for week in cal:
            line = []
            for j, day in enumerate(week):
                if day == 0:
                    line.append("   ")
                else:
                    # Map the day to correct weekday position
                    weekday_index = shuffled_weekdays.index(weekdays[j])
                    line.append(f"{day:2d}")
            print(" ".join(line))
        print()

if __name__ == "__main__":
    year = get_year()
    print_calendar(year)

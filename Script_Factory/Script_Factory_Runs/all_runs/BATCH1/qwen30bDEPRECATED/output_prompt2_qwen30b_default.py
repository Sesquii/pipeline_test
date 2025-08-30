import sys
import datetime
import calendar
import random

def get_year():
    """Get year from command line argument or interactive prompt."""
    if len(sys.argv) > 1:
        return int(sys.argv[1])
    else:
        return int(input("Enter a year: "))

def print_calendar(year):
    """Print shuffled calendar for the given year."""
    # Get all month names
    months = list(calendar.month_name)[1:]  # Exclude empty first element
    
    # Shuffle month names
    shuffled_months = months.copy()
    random.shuffle(shuffled_months)
    
    # Generate calendar for each month
    for i in range(12):
        # Get actual month name and shuffled month name
        actual_month = calendar.month_name[i+1]
        shuffled_month = shuffled_months[i]
        
        # Get weekday headers (0=Monday, 6=Sunday)
        weekdays = list(calendar.day_abbr)
        shuffled_weekdays = weekdays.copy()
        random.shuffle(shuffled_weekdays)
        
        # Create calendar matrix
        cal = calendar.monthcalendar(year, i+1)
        
        # Print month header
        print(f"\n{shuffled_month} {year}")
        print(" ".join(shuffled_weekdays))
        
        # Print calendar grid
        for week in cal:
            row = []
            for j, day in enumerate(week):
                if day == 0:
                    row.append("  ")
                else:
                    # Reorder days to match shuffled headers
                    original_pos = weekdays.index(shuffled_weekdays[j])
                    formatted_day = f"{day:2d}"
                    row.append(formatted_day)
            print(" ".join(row))

if __name__ == "__main__":
    year = get_year()
    print_calendar(year)

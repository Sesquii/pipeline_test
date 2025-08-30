```python
import sys

def main():
    months = ["December", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November"]
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    for month_name in months:
        print(f"Month: {month_name}")
        days = days_in_month[months.index(month_name)]
        for week_num in range(0, days, 7):
            start_day = week_num + 1
            for day in range(start_day, start_day + 7):
                if day <= days:
                    print(f"{day:2d}/{month_name}")
                else:
                    break

if __name__ == "__main__":
    main()
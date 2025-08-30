```python
import datetime

def main():
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))

    day_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    shift = 5

    base_date = datetime.date(year, month, 1)
    days_in_month = (datetime.date(year, month + 1, 1) - base_date).days

    if month == 2:
        days_in_month = 28
    elif month in [4, 6, 9, 11]:
        days_in_month = 30
    else:
        days_in_month = 31

    print(f"{month} {year}")
    print("Mon Tue Wed Thu Fri Sat Sun")
    for week in range(5):
        row = []
        for day in range(7):
            current_day = base_date + datetime.timedelta(days=day)
            actual_weekday = current_day.weekday()
            shifted_weekday = (actual_weekday + shift) % 7
            row.append(day_names[shifted_weekday])
        print(" ".join(row))

if __name__ == "__main__":
    main()
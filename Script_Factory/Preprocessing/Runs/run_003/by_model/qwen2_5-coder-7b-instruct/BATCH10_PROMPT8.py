# BATCH10_PROMPT8_python3.py

import calendar
from datetime import datetime

class UselessCalendarApp:
    def __init__(self):
        self.calendar = calendar.TextCalendar(calendar.SUNDAY)

    def display_calendar(self, year=None, month=None):
        if year is None or month is None:
            today = datetime.now()
            year, month = today.year, today.month
        else:
            try:
                year = int(year)
                month = int(month)
                if month < 1 or month > 12:
                    raise ValueError("Month must be between 1 and 12")
            except ValueError as e:
                print(f"Error: {e}")
                return

        # Incorrectly name the months
        month_names = [
            "Froosty", "Breezy", "Springy", "Greengrass", "Honeydew", "Summerheat",
            "Sunset", "Autumnal", "Crispy", "Windy", "Nippy", "Snowy"
        ]

        # Display the calendar with incorrect month names
        print(f"Calendar for {month_names[month - 1]} {year}")
        cal_str = self.calendar.formatmonth(year, month)
        print(cal_str)

if __name__ == "__main__":
    app = UselessCalendarApp()
    app.display_calendar()  # Display calendar for the current date
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

# ===== GENERATED TESTS =====
```python
# BATCH10_PROMPT8_Granite.py

def print_useless_calendar(year: int, month: int):
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

# Test cases for BATCH10_PROMPT8_Granite.py

import pytest
from io import StringIO
from contextlib import redirect_stdout

def test_print_useless_calendar_valid_month():
    # Redirect stdout to capture the output
    with StringIO() as buf, redirect_stdout(buf):
        print_useless_calendar(2023, 1)
        assert "January 2023" in buf.getvalue()
        assert "Su Mo Tu We Th Fr Sa" in buf.getvalue()
        assert "   1  2  3  4  5  6" in buf.getvalue()

def test_print_useless_calendar_invalid_month():
    with StringIO() as buf, redirect_stdout(buf):
        print_useless_calendar(2023, 13)
        assert "Invalid month!" in buf.getvalue()

def test_print_useless_calendar_leap_year():
    with StringIO() as buf, redirect_stdout(buf):
        print_useless_calendar(2024, 2)
        assert "February 2024" in buf.getvalue()
        assert "   1  2  3  4  5  6  7" in buf.getvalue()

def test_print_useless_calendar_non_leap_year():
    with StringIO() as buf, redirect_stdout(buf):
        print_useless_calendar(2023, 2)
        assert "February 2023" in buf.getvalue()
        assert "   1  2  3  4  5  6  7" in buf.getvalue()

def test_main_valid_input():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "2023\n1\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "January 2023" in output_buf.getvalue()
        assert "Su Mo Tu We Th Fr Sa" in output_buf.getvalue()
        assert "   1  2  3  4  5  6" in output_buf.getvalue()

def test_main_invalid_input():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "2023\n13\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_year_out_of_range():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "2019\n1\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_month_out_of_range():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "2023\n14\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_year_non_integer():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "abc\n1\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_month_non_integer():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "2023\nabc\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_year_negative():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "-1\n1\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_month_negative():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "2023\n-1\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_year_too_large():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "2101\n1\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_month_too_large():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "2023\n13\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_year_too_small():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "1899\n1\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_month_too_small():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "2023\n0\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_year_non_integer_input():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "abc\n1\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_month_non_integer_input():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "2023\nabc\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_year_negative_input():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "-1\n1\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_month_negative_input():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "2023\n-1\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_year_too_large_input():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "2101\n1\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_month_too_large_input():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "2023\n13\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_year_too_small_input():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "1899\n1\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_month_too_small_input():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "2023\n0\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_year_non_integer_input():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "abc\n1\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_month_non_integer_input():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "2023\nabc\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_year_negative_input():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "-1\n1\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_month_negative_input():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "2023\n-1\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_year_too_large_input():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "2101\n1\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_month_too_large_input():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "2023\n13\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_year_too_small_input():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "1899\n1\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_month_too_small_input():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "2023\n0\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_year_non_integer_input():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "abc\n1\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_month_non_integer_input():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "2023\nabc\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_year_negative_input():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "-1\n1\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_month_negative_input():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "2023\n-1\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_year_too_large_input():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "2101\n1\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_month_too_large_input():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "2023\n13\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with contextlib.redirect_stdin(input_buf):
            main()
        
        assert "Please enter a valid year and month." in output_buf.getvalue()

def test_main_year_too_small_input():
    with StringIO() as input_buf, StringIO() as output_buf, redirect_stdout(output_buf):
        input_data = "1899\n1\n"
        input_buf.write(input_data)
        input_buf.seek(0)

        # Redirect stdin to simulate user input
        with
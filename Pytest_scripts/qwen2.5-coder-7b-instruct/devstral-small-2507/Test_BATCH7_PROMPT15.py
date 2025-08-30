import csv

def filter_csv(input_file, output_file, filter_string="ERROR"):
    """
    Filters a CSV file by removing rows containing a specific string and adds a 'filtered' column.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
        filter_string (str): String to filter out from any cell in the row. Default is "ERROR".
    """
    filtered_rows = []

    # Read the input CSV file
    with open(input_file, mode='r', newline='') as infile:
        reader = csv.reader(infile)
        header = next(reader)  # Read the header row
        header.append('filtered')  # Add 'filtered' column to header

        for row in reader:
            if filter_string not in row:  # Check if filter_string is not present in any cell of the row
                filtered_rows.append(row)

    # Write the filtered data to the output CSV file with the new 'filtered' column
    with open(output_file, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)  # Write header with 'filtered' column

        for row in filtered_rows:
            row.append('True')  # Add 'True' to the 'filtered' column
            writer.writerow(row)

if __name__ == "__main__":
    input_file = "input.csv"   # Replace with your actual input file path
    output_file = "output.csv"  # Replace with your desired output file path

    filter_csv(input_file, output_file)

# ===== GENERATED TESTS =====
```python
import pytest
from io import StringIO
from typing import List

# Original code remains unchanged

def test_filter_csv_with_error_string():
    """
    Test case to filter CSV with 'ERROR' string.
    """
    input_data = """id,name,status
1,Alice,ERROR
2,Bob,OK
3,Charlie,ERROR"""
    expected_output = """id,name,status,filtered
2,Bob,OK,True"""

    input_csv = StringIO(input_data)
    output_csv = StringIO()

    filter_csv(input_csv, output_csv, filter_string="ERROR")

    assert output_csv.getvalue() == expected_output

def test_filter_csv_with_no_error_string():
    """
    Test case to filter CSV with no 'ERROR' string.
    """
    input_data = """id,name,status
1,Alice,OK
2,Bob,OK
3,Charlie,OK"""
    expected_output = """id,name,status,filtered
1,Alice,OK,True
2,Bob,OK,True
3,Charlie,OK,True"""

    input_csv = StringIO(input_data)
    output_csv = StringIO()

    filter_csv(input_csv, output_csv, filter_string="ERROR")

    assert output_csv.getvalue() == expected_output

def test_filter_csv_with_empty_input():
    """
    Test case to handle empty input CSV.
    """
    input_data = ""
    expected_output = ""

    input_csv = StringIO(input_data)
    output_csv = StringIO()

    filter_csv(input_csv, output_csv, filter_string="ERROR")

    assert output_csv.getvalue() == expected_output

def test_filter_csv_with_missing_header():
    """
    Test case to handle CSV with missing header.
    """
    input_data = """1,Alice,OK
2,Bob,OK
3,Charlie,OK"""
    expected_output = """id,name,status,filtered
1,Alice,OK,True
2,Bob,OK,True
3,Charlie,OK,True"""

    input_csv = StringIO(input_data)
    output_csv = StringIO()

    filter_csv(input_csv, output_csv, filter_string="ERROR")

    assert output_csv.getvalue() == expected_output

def test_filter_csv_with_non_existent_filter_string():
    """
    Test case to handle CSV with non-existent filter string.
    """
    input_data = """id,name,status
1,Alice,OK
2,Bob,OK
3,Charlie,OK"""
    expected_output = """id,name,status,filtered
1,Alice,OK,True
2,Bob,OK,True
3,Charlie,OK,True"""

    input_csv = StringIO(input_data)
    output_csv = StringIO()

    filter_csv(input_csv, output_csv, filter_string="NOT_FOUND")

    assert output_csv.getvalue() == expected_output

def test_filter_csv_with_large_input():
    """
    Test case to handle large CSV input.
    """
    input_data = "\n".join([f"{i},Alice{i},OK" for i in range(1000)])
    expected_output = "\n".join([f"{i},Alice{i},OK,True" for i in range(1000)])

    input_csv = StringIO(input_data)
    output_csv = StringIO()

    filter_csv(input_csv, output_csv, filter_string="ERROR")

    assert output_csv.getvalue() == expected_output

def test_filter_csv_with_special_characters():
    """
    Test case to handle CSV with special characters.
    """
    input_data = """id,name,status
1,Alice,OK!@#
2,Bob,OK$%^
3,Charlie,OK&*()"""
    expected_output = """id,name,status,filtered
1,Alice,OK!@#,True
2,Bob,OK$%^,True
3,Charlie,OK&*(),True"""

    input_csv = StringIO(input_data)
    output_csv = StringIO()

    filter_csv(input_csv, output_csv, filter_string="ERROR")

    assert output_csv.getvalue() == expected_output

def test_filter_csv_with_mixed_case():
    """
    Test case to handle CSV with mixed case.
    """
    input_data = """id,name,status
1,Alice,OK
2,Bob,Ok
3,Charlie,oK"""
    expected_output = """id,name,status,filtered
1,Alice,OK,True"""

    input_csv = StringIO(input_data)
    output_csv = StringIO()

    filter_csv(input_csv, output_csv, filter_string="ok")

    assert output_csv.getvalue() == expected_output

def test_filter_csv_with_whitespace():
    """
    Test case to handle CSV with whitespace.
    """
    input_data = """id,name,status
1,Alice,OK
2,Bob,Ok
3,Charlie,oK"""
    expected_output = """id,name,status,filtered
1,Alice,OK,True"""

    input_csv = StringIO(input_data)
    output_csv = StringIO()

    filter_csv(input_csv, output_csv, filter_string=" ok ")

    assert output_csv.getvalue() == expected_output

def test_filter_csv_with_non_ascii_characters():
    """
    Test case to handle CSV with non-ASCII characters.
    """
    input_data = """id,name,status
1,Alice,OK
2,Bob,Ök
3,Charlie,ÖK"""
    expected_output = """id,name,status,filtered
1,Alice,OK,True"""

    input_csv = StringIO(input_data)
    output_csv = StringIO()

    filter_csv(input_csv, output_csv, filter_string="Ö")

    assert output_csv.getvalue() == expected_output

def test_filter_csv_with_empty_header_and_rows():
    """
    Test case to handle CSV with empty header and rows.
    """
    input_data = "\n".join([f"{i},Alice{i},OK" for i in range(1000)])
    expected_output = "\n".join([f"{i},Alice{i},OK,True" for i in range(1000)])

    input_csv = StringIO(input_data)
    output_csv = StringIO()

    filter_csv(input_csv, output_csv, filter_string="ERROR")

    assert output_csv.getvalue() == expected_output

def test_filter_csv_with_single_row():
    """
    Test case to handle CSV with a single row.
    """
    input_data = """id,name,status
1,Alice,OK"""
    expected_output = """id,name,status,filtered
1,Alice,OK,True"""

    input_csv = StringIO(input_data)
    output_csv = StringIO()

    filter_csv(input_csv, output_csv, filter_string="ERROR")

    assert output_csv.getvalue() == expected_output

def test_filter_csv_with_single_column():
    """
    Test case to handle CSV with a single column.
    """
    input_data = """id
1"""
    expected_output = """id,filtered
1,True"""

    input_csv = StringIO(input_data)
    output_csv = StringIO()

    filter_csv(input_csv, output_csv, filter_string="ERROR")

    assert output_csv.getvalue() == expected_output

def test_filter_csv_with_empty_column():
    """
    Test case to handle CSV with an empty column.
    """
    input_data = """id,name,status
1,,OK"""
    expected_output = """id,name,status,filtered
1,,OK,True"""

    input_csv = StringIO(input_data)
    output_csv = StringIO()

    filter_csv(input_csv, output_csv, filter_string="ERROR")

    assert output_csv.getvalue() == expected_output

def test_filter_csv_with_large_filter_string():
    """
    Test case to handle CSV with a large filter string.
    """
    input_data = """id,name,status
1,Alice,OK
2,Bob,OK
3,Charlie,OK"""
    expected_output = """id,name,status,filtered
1,Alice,OK,True
2,Bob,OK,True
3,Charlie,OK,True"""

    filter_csv(input_data, "output.csv", filter_string="ERROR" * 100)

    with open("output.csv", mode='r', newline='') as outfile:
        reader = csv.reader(outfile)
        header = next(reader)  # Read the header row
        filtered_rows = list(reader)

    assert len(filtered_rows) == 3

def test_filter_csv_with_large_input_file():
    """
    Test case to handle large input file.
    """
    with open("large_input.csv", mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        for i in range(1000):
            writer.writerow([i, f"Alice{i}", "OK"])

    filter_csv("large_input.csv", "output.csv", filter_string="ERROR")

    with open("output.csv", mode='r', newline='') as outfile:
        reader = csv.reader(outfile)
        header = next(reader)  # Read the header row
        filtered_rows = list(reader)

    assert len(filtered_rows) == 1000

def test_filter_csv_with_large_output_file():
    """
    Test case to handle large output file.
    """
    with open("large_input.csv", mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        for i in range(1000):
            writer.writerow([i, f"Alice{i}", "OK"])

    filter_csv("large_input.csv", "output.csv", filter_string="ERROR")

    with open("output.csv", mode='r', newline='') as outfile:
        reader = csv.reader(outfile)
        header = next(reader)  # Read the header row
        filtered_rows = list(reader)

    assert len(filtered_rows) == 1000

def test_filter_csv_with_large_header():
    """
    Test case to handle CSV with a large header.
    """
    input_data = ",".join([f"col{i}" for i in range(1000)]) + "\n"
    input_data += "\n".join(",".join(["OK"] * 1000) for _ in range(1000))

    expected_output = ",".join([f"col{i},filtered" for i in range(1000)]) + "\n"
    expected_output += "\n".join(",".join(["True"] * 1000) for _ in range(1000))

    input_csv = StringIO(input_data)
    output_csv = StringIO()

    filter_csv(input_csv, output_csv, filter_string="ERROR")

    assert output_csv.getvalue() == expected_output

def test_filter_csv_with_large_rows():
    """
    Test case to handle CSV with large rows.
    """
    input_data = "id,name,status\n"
    input_data += "\n".join([f"{i},{f'Alice{i}' * 1000},OK" for i in range(1000)])

    expected_output = "id,name,status,filtered\n"
    expected_output += "\n".join([f"{i},{f'Alice{i}' * 1000},OK,True" for i in range(1000)])

    input_csv = StringIO(input_data)
    output_csv = StringIO()

    filter_csv(input_csv, output_csv, filter_string="ERROR")

    assert output_csv.getvalue() == expected_output

def test_filter_csv_with_large_columns():
    """
    Test case to handle CSV with large columns.
    """
    input_data = "id,"
    input_data += ",".join([f"col{i}" for i in range(1000)]) + "\n"
    input_data += "1,"
    input_data += ",".join(["OK"] * 1000) + "\n"

    expected_output = "id,filtered,"
    expected_output += ",".join([f"col{i},filtered" for i in range(1000)]) + "\n"
    expected_output += "1,True,"
    expected_output += ",".join(["True"] * 1000) + "\n"

    input_csv = StringIO(input_data)
    output_csv = StringIO()

    filter_csv(input_csv, output_csv, filter_string="ERROR")

    assert output_csv.getvalue() == expected_output

def test_filter_csv_with_large_header_and_rows():
    """
    Test case to handle CSV with a large header and rows.
    """
    input_data = ",".join([f"col{i}" for i in range(1000)]) + "\n"
    input_data += "\n".join(",".join(["OK"] * 1000) for _ in range(1000))

    expected_output = ",".join([f"col{i},filtered" for i in range(1000)]) + "\n"
    expected_output += "\n".join(",".join(["True"] * 1000) for _ in range(1000))

    input_csv = StringIO(input_data)
    output_csv = StringIO()

    filter_csv(input_csv, output_csv, filter_string="ERROR")

    assert output_csv.getvalue() == expected_output

def test_filter_csv_with_large_header_and_rows_and_columns():
    """
    Test case to handle CSV with a large header, rows, and columns.
    """
    input_data = ",".join([f"col{i}" for i in range(1000)]) + "\n"
    input_data += "\n".join(",".join(["OK"] * 1000) for _ in range(1000))

    expected_output = ",".join([f"col{i},filtered" for i in range(1000)]) + "\n"
    expected_output += "\n".join(",".join(["True"] * 1000) for _ in range(1000))

    input_csv = StringIO(input_data)
    output_csv = StringIO()

    filter_csv(input_csv, output_csv, filter_string="ERROR")

    assert output_csv.getvalue() == expected_output

def test_filter_csv_with_large_header_and_rows_and_columns_and_filter_string():
    """
    Test case to handle CSV with a large header, rows, columns, and filter string.
    """
    input_data = ",".join([f"col{i}" for i in range(1000)]) + "\n"
    input_data += "\n".join(",".join(["OK"] * 1000) for _ in range(1000))

    expected_output = ",".join([f"col{i},filtered" for i in range(1000)]) + "\n"
    expected_output += "\n".join(",".join(["True"] * 1000) for _ in range(1000))

    input_csv = StringIO(input_data)
    output_csv = StringIO()

    filter_csv(input_csv, output_csv, filter_string="ERROR" * 100)

    assert output_csv.getvalue() == expected_output

def test_filter_csv_with_large_header_and_rows_and_columns_and_filter_string_and_input_file():
    """
    Test case to handle CSV with a large header, rows, columns, filter string, and input file.
    """
    with open("large_input.csv", mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        for i in range(1000):
            writer.writerow([i] + [f"Alice{i}" * 1000] + ["OK"])

    filter_csv("large_input.csv", "output.csv", filter_string="ERROR" * 100)

    with open("output.csv", mode='r', newline='') as outfile:
        reader = csv.reader(outfile)
        header = next(reader)  # Read the header row
        filtered_rows = list(reader)

    assert len(filtered_rows) == 1000

def test_filter_csv_with_large_header_and_rows_and_columns_and_filter_string_and_output_file():
    """
    Test case to handle CSV with a large header, rows, columns, filter string, and output file.
    """
    with open("large_input.csv", mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        for i in range(1000):
            writer.writerow([i] + [f"Alice{i}" * 1000] + ["OK"])

    filter_csv("large_input.csv", "output.csv", filter_string="ERROR" * 100)

    with open("output.csv", mode='r', newline='') as outfile:
        reader = csv.reader(outfile)
        header = next(reader)  # Read the header row
        filtered_rows = list(reader)

    assert len(filtered_rows) == 1000

def test_filter_csv_with_large_header_and_rows_and_columns_and_filter_string_and_input_file_and_output_file():
    """
    Test case to handle CSV with a large header, rows, columns, filter string, input file, and output file.
    """
    with open("large_input.csv", mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        for i in range(1000):
            writer.writerow([i] + [f"Alice{i}" * 1000] + ["OK"])

    filter_csv("large_input.csv", "output.csv", filter_string="ERROR" * 100)

    with open("output.csv", mode='r', newline='') as outfile:
        reader = csv.reader(outfile)
        header = next(reader)  # Read the header row
        filtered_rows = list(reader)

    assert len(filtered_rows) == 1000

def test_filter_csv_with_large_header_and_rows_and_columns_and_filter_string_and_input_file_and_output_file_and_filter_string():
    """
    Test case to handle CSV with a large header, rows, columns, filter string, input file, output file, and filter string.
    """
    with open("large_input.csv", mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        for i in range(1000):
            writer.writerow([i] + [f"Alice{i}" * 1000] + ["OK"])

    filter_csv("large_input.csv", "output.csv", filter_string="ERROR" * 100)

    with open("output.csv", mode='r', newline='') as outfile:
        reader = csv.reader(outfile)
        header = next(reader)  # Read the header row
        filtered_rows = list(reader)

    assert len(filtered_rows) == 1000

def test_filter_csv_with_large_header_and_rows_and_columns_and_filter_string_and_input_file_and_output_file_and_filter_string_and_input_file():
    """
    Test case to handle CSV with a large header, rows, columns, filter string, input file, output file, filter string, and input file.
    """
    with open("large_input.csv", mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        for i in range(1000):
            writer.writerow([i] + [f"Alice{i}" * 1000] + ["OK"])

    filter_csv("large_input.csv", "output.csv", filter_string="ERROR" * 100)

    with open("output.csv", mode='r', newline='') as outfile:
        reader = csv.reader(outfile)
        header = next(reader)  # Read the header row
        filtered_rows = list(reader)

    assert len(filtered_rows)
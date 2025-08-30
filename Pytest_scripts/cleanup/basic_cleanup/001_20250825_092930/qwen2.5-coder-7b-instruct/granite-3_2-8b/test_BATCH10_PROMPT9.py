# BATCH10_PROMPT9_Granite.py

import csv
from sympy import isprime

def sum_of_columns(row):
    """Calculate the sum of all numerical columns in a row."""
    return sum(float(cell) for cell in row if cell.strip() and cell.replace('.', '', 1).isdigit())

def filter_rows(csvfile, outputfile):
    """Filter rows from CSV, keeping only those where the sum of numerical columns is prime."""
    with open(csvfile, 'r') as infile, open(outputfile, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Write header to output file if it exists in input file
        header = next(reader)
        writer.writerow(header)

        for row in reader:
            row_sum = sum_of_columns(row)
            if isprime(row_sum):
                writer.writerow(row)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python BATCH10_PROMPT9_Granite.py <input_csv> <output_csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    filter_rows(input_file, output_file)

# ===== GENERATED TESTS =====
# BATCH10_PROMPT9_Granite.py

import csv
from sympy import isprime

def sum_of_columns(row):
    """Calculate the sum of all numerical columns in a row."""
    return sum(float(cell) for cell in row if cell.strip() and cell.replace('.', '', 1).isdigit())

def filter_rows(csvfile, outputfile):
    """Filter rows from CSV, keeping only those where the sum of numerical columns is prime."""
    with open(csvfile, 'r') as infile, open(outputfile, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Write header to output file if it exists in input file
        header = next(reader)
        writer.writerow(header)

        for row in reader:
            row_sum = sum_of_columns(row)
            if isprime(row_sum):
                writer.writerow(row)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python BATCH10_PROMPT9_Granite.py <input_csv> <output_csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    filter_rows(input_file, output_file)


# Test suite for BATCH10_PROMPT9_Granite.py

import pytest
from io import StringIO
from contextlib import redirect_stdout

def test_sum_of_columns():
    """Test the sum_of_columns function."""
    assert sum_of_columns(['1', '2.5', '', '3']) == 6.5
    assert sum_of_columns(['-1', '-2.5', '', '-3']) == -7.0
    assert sum_of_columns(['a', 'b', 'c']) == 0

def test_filter_rows(tmp_path):
    """Test the filter_rows function."""
    input_csv = tmp_path / "input.csv"
    output_csv = tmp_path / "output.csv"

    # Test with a CSV file where the sum of numerical columns is not prime
    input_csv.write_text("header1,header2\n1,2\n3,4")
    filter_rows(input_csv, output_csv)
    with open(output_csv) as f:
        assert f.read() == "header1,header2\n"

    # Test with a CSV file where the sum of numerical columns is prime
    input_csv.write_text("header1,header2\n1,2\n5,3")
    filter_rows(input_csv, output_csv)
    with open(output_csv) as f:
        assert f.read() == "header1,header2\n5,3\n"

def test_filter_rows_with_header(tmp_path):
    """Test the filter_rows function with a header."""
    input_csv = tmp_path / "input.csv"
    output_csv = tmp_path / "output.csv"

    # Test with a CSV file where the sum of numerical columns is not prime
    input_csv.write_text("header1,header2\n1,2\n3,4")
    filter_rows(input_csv, output_csv)
    with open(output_csv) as f:
        assert f.read() == "header1,header2\n"

    # Test with a CSV file where the sum of numerical columns is prime
    input_csv.write_text("header1,header2\n1,2\n5,3")
    filter_rows(input_csv, output_csv)
    with open(output_csv) as f:
        assert f.read() == "header1,header2\n5,3\n"

def test_filter_rows_with_empty_input(tmp_path):
    """Test the filter_rows function with an empty input file."""
    input_csv = tmp_path / "input.csv"
    output_csv = tmp_path / "output.csv"

    input_csv.write_text("")
    filter_rows(input_csv, output_csv)
    with open(output_csv) as f:
        assert f.read() == ""

def test_filter_rows_with_non_numerical_columns(tmp_path):
    """Test the filter_rows function with non-numerical columns."""
    input_csv = tmp_path / "input.csv"
    output_csv = tmp_path / "output.csv"

    # Test with a CSV file where the sum of numerical columns is not prime
    input_csv.write_text("header1,header2\na,b\n3,4")
    filter_rows(input_csv, output_csv)
    with open(output_csv) as f:
        assert f.read() == ""

    # Test with a CSV file where the sum of numerical columns is prime
    input_csv.write_text("header1,header2\na,b\n5,3")
    filter_rows(input_csv, output_csv)
    with open(output_csv) as f:
        assert f.read() == ""

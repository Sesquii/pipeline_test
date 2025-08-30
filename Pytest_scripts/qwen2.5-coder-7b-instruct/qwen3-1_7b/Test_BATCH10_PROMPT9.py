```python
import csv

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def process_csv(input_file, output_file):
    with open(input_file, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = [row for row in reader]
    
    filtered_rows = []
    for row in rows:
        sum_numbers = 0
        for cell in row:
            try:
                num = float(cell)
                sum_numbers += num
            except ValueError:
                pass
        if is_prime(sum_numbers):
            filtered_rows.append(row)
    
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(filtered_rows)

if __name__ == "__main__":
    input_file = "input.csv"
    output_file = "output.csv"
    process_csv(input_file, output_file)

# ===== GENERATED TESTS =====
```python
import pytest
from io import StringIO

# Original script code remains unchanged

# Test suite for the original script

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(17) == True
    assert is_prime(18) == False
    assert is_prime(19) == True

def test_process_csv(tmp_path):
    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"

    # Create a sample CSV file with some data
    input_data = """A,B,C\n1,2,3\n4,5,6\n7,8,9"""
    input_file.write_text(input_data)

    # Process the CSV file
    process_csv(str(input_file), str(output_file))

    # Read the output CSV file and check if it contains the correct data
    with open(str(output_file), 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = [row for row in reader]

    assert header == ['A', 'B', 'C']
    assert rows == [['7', '8', '9']]

def test_process_csv_with_non_numeric_values(tmp_path):
    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"

    # Create a sample CSV file with some non-numeric values
    input_data = """A,B,C\n1,2,a\n4,b,6\n7,c,9"""
    input_file.write_text(input_data)

    # Process the CSV file
    process_csv(str(input_file), str(output_file))

    # Read the output CSV file and check if it contains the correct data
    with open(str(output_file), 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = [row for row in reader]

    assert header == ['A', 'B', 'C']
    assert rows == [['7', 'c', '9']]

def test_process_csv_with_empty_file(tmp_path):
    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"

    # Create an empty CSV file
    input_data = ""
    input_file.write_text(input_data)

    # Process the CSV file
    process_csv(str(input_file), str(output_file))

    # Read the output CSV file and check if it is empty
    with open(str(output_file), 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = [row for row in reader]

    assert header == ['A', 'B', 'C']
    assert rows == []

def test_process_csv_with_header_only(tmp_path):
    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"

    # Create a CSV file with only the header
    input_data = """A,B,C"""
    input_file.write_text(input_data)

    # Process the CSV file
    process_csv(str(input_file), str(output_file))

    # Read the output CSV file and check if it is empty
    with open(str(output_file), 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = [row for row in reader]

    assert header == ['A', 'B', 'C']
    assert rows == []

def test_process_csv_with_negative_numbers(tmp_path):
    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"

    # Create a sample CSV file with negative numbers
    input_data = """A,B,C\n-1,-2,-3\n4,5,6\n7,8,9"""
    input_file.write_text(input_data)

    # Process the CSV file
    process_csv(str(input_file), str(output_file))

    # Read the output CSV file and check if it contains the correct data
    with open(str(output_file), 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = [row for row in reader]

    assert header == ['A', 'B', 'C']
    assert rows == [['7', '8', '9']]
```
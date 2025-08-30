```python
import csv

def filter_csv(input_path, output_path):
    with open(input_path, 'r', newline='') as infile:
        reader = csv.reader(infile)
        headers = next(reader)
        data_rows = [row for row in reader]
    
    filtered_data = []
    for row in data_rows:
        if not row[0].lower().startswith('aeiou'):
            filtered_data.append(row)
    
    with open(output_path, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(headers)
        writer.writerows(filtered_data)

if __name__ == "__main__":
    input_file = "input.csv"
    output_file = "output.csv"
    filter_csv(input_file, output_file)

# ===== GENERATED TESTS =====
```python
import csv
from io import StringIO
import pytest

def filter_csv(input_path, output_path):
    with open(input_path, 'r', newline='') as infile:
        reader = csv.reader(infile)
        headers = next(reader)
        data_rows = [row for row in reader]
    
    filtered_data = []
    for row in data_rows:
        if not row[0].lower().startswith('aeiou'):
            filtered_data.append(row)
    
    with open(output_path, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(headers)
        writer.writerows(filtered_data)

# Test suite
def test_filter_csv(tmpdir):
    """Test the filter_csv function."""
    # Create a temporary input CSV file
    input_file = tmpdir.join("input.csv")
    with open(input_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age"])
        writer.writerow(["Alice", "30"])
        writer.writerow(["Bob", "25"])
        writer.writerow(["Charlie", "35"])

    # Define the expected output
    expected_output = """Name,Age
Bob,25
Charlie,35"""

    # Call the function with the temporary files
    output_file = tmpdir.join("output.csv")
    filter_csv(input_file, output_file)

    # Read the output file and compare it to the expected output
    with open(output_file, "r") as f:
        result = f.read()
    
    assert result == expected_output

def test_filter_csv_empty_input(tmpdir):
    """Test the filter_csv function with an empty input CSV file."""
    # Create a temporary input CSV file
    input_file = tmpdir.join("input.csv")
    with open(input_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age"])

    # Define the expected output (same as input since there's no data to filter)
    expected_output = """Name,Age"""

    # Call the function with the temporary files
    output_file = tmpdir.join("output.csv")
    filter_csv(input_file, output_file)

    # Read the output file and compare it to the expected output
    with open(output_file, "r") as f:
        result = f.read()
    
    assert result == expected_output

def test_filter_csv_no_header(tmpdir):
    """Test the filter_csv function with a CSV file without headers."""
    # Create a temporary input CSV file
    input_file = tmpdir.join("input.csv")
    with open(input_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Alice", "30"])
        writer.writerow(["Bob", "25"])

    # Define the expected output (same as input since there's no data to filter)
    expected_output = """Alice,30
Bob,25"""

    # Call the function with the temporary files
    output_file = tmpdir.join("output.csv")
    filter_csv(input_file, output_file)

    # Read the output file and compare it to the expected output
    with open(output_file, "r") as f:
        result = f.read()
    
    assert result == expected_output

def test_filter_csv_non_alphabetical_name(tmpdir):
    """Test the filter_csv function with a non-alphabetical name."""
    # Create a temporary input CSV file
    input_file = tmpdir.join("input.csv")
    with open(input_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age"])
        writer.writerow(["123", "30"])

    # Define the expected output (same as input since there's no data to filter)
    expected_output = """Name,Age
123,30"""

    # Call the function with the temporary files
    output_file = tmpdir.join("output.csv")
    filter_csv(input_file, output_file)

    # Read the output file and compare it to the expected output
    with open(output_file, "r") as f:
        result = f.read()
    
    assert result == expected_output

def test_filter_csv_mixed_case_names(tmpdir):
    """Test the filter_csv function with mixed case names."""
    # Create a temporary input CSV file
    input_file = tmpdir.join("input.csv")
    with open(input_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age"])
        writer.writerow(["alice", "30"])
        writer.writerow(["Bob", "25"])
        writer.writerow(["Charlie", "35"])

    # Define the expected output
    expected_output = """Name,Age
Bob,25
Charlie,35"""

    # Call the function with the temporary files
    output_file = tmpdir.join("output.csv")
    filter_csv(input_file, output_file)

    # Read the output file and compare it to the expected output
    with open(output_file, "r") as f:
        result = f.read()
    
    assert result == expected_output

def test_filter_csv_special_characters(tmpdir):
    """Test the filter_csv function with special characters in names."""
    # Create a temporary input CSV file
    input_file = tmpdir.join("input.csv")
    with open(input_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age"])
        writer.writerow(["Alice!", "30"])
        writer.writerow(["Bob@", "25"])

    # Define the expected output
    expected_output = """Name,Age
Bob@,25"""

    # Call the function with the temporary files
    output_file = tmpdir.join("output.csv")
    filter_csv(input_file, output_file)

    # Read the output file and compare it to the expected output
    with open(output_file, "r") as f:
        result = f.read()
    
    assert result == expected_output

def test_filter_csv_missing_column(tmpdir):
    """Test the filter_csv function with a missing column."""
    # Create a temporary input CSV file
    input_file = tmpdir.join("input.csv")
    with open(input_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name"])
        writer.writerow(["Alice"])
        writer.writerow(["Bob"])

    # Define the expected output (same as input since there's no data to filter)
    expected_output = """Name
Alice
Bob"""

    # Call the function with the temporary files
    output_file = tmpdir.join("output.csv")
    filter_csv(input_file, output_file)

    # Read the output file and compare it to the expected output
    with open(output_file, "r") as f:
        result = f.read()
    
    assert result == expected_output

def test_filter_csv_non_string_name(tmpdir):
    """Test the filter_csv function with a non-string name."""
    # Create a temporary input CSV file
    input_file = tmpdir.join("input.csv")
    with open(input_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age"])
        writer.writerow([30, "30"])

    # Define the expected output (same as input since there's no data to filter)
    expected_output = """Name,Age
30,30"""

    # Call the function with the temporary files
    output_file = tmpdir.join("output.csv")
    filter_csv(input_file, output_file)

    # Read the output file and compare it to the expected output
    with open(output_file, "r") as f:
        result = f.read()
    
    assert result == expected_output

def test_filter_csv_large_input(tmpdir):
    """Test the filter_csv function with a large input CSV file."""
    # Create a temporary input CSV file
    input_file = tmpdir.join("input.csv")
    with open(input_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age"])
        for i in range(1000):
            writer.writerow([f"Person{i}", str(i)])

    # Define the expected output (same as input since there's no data to filter)
    expected_output = """Name,Age
Person0,0
Person1,1
...
Person999,999"""

    # Call the function with the temporary files
    output_file = tmpdir.join("output.csv")
    filter_csv(input_file, output_file)

    # Read the output file and compare it to the expected output
    with open(output_file, "r") as f:
        result = f.read()
    
    assert result == expected_output

def test_filter_csv_empty_string_name(tmpdir):
    """Test the filter_csv function with an empty string name."""
    # Create a temporary input CSV file
    input_file = tmpdir.join("input.csv")
    with open(input_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age"])
        writer.writerow(["", "30"])

    # Define the expected output (same as input since there's no data to filter)
    expected_output = """Name,Age

"""

    # Call the function with the temporary files
    output_file = tmpdir.join("output.csv")
    filter_csv(input_file, output_file)

    # Read the output file and compare it to the expected output
    with open(output_file, "r") as f:
        result = f.read()
    
    assert result == expected_output

def test_filter_csv_non_ascii_name(tmpdir):
    """Test the filter_csv function with a non-ASCII name."""
    # Create a temporary input CSV file
    input_file = tmpdir.join("input.csv")
    with open(input_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age"])
        writer.writerow(["Álvaro", "30"])

    # Define the expected output (same as input since there's no data to filter)
    expected_output = """Name,Age
Álvaro,30"""

    # Call the function with the temporary files
    output_file = tmpdir.join("output.csv")
    filter_csv(input_file, output_file)

    # Read the output file and compare it to the expected output
    with open(output_file, "r") as f:
        result = f.read()
    
    assert result == expected_output

def test_filter_csv_non_alphabetical_age(tmpdir):
    """Test the filter_csv function with a non-alphabetical age."""
    # Create a temporary input CSV file
    input_file = tmpdir.join("input.csv")
    with open(input_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age"])
        writer.writerow(["Alice", "30"])
        writer.writerow(["Bob", "25"])
        writer.writerow(["Charlie", "35"])

    # Define the expected output
    expected_output = """Name,Age
Alice,30
Bob,25"""

    # Call the function with the temporary files
    output_file = tmpdir.join("output.csv")
    filter_csv(input_file, output_file)

    # Read the output file and compare it to the expected output
    with open(output_file, "r") as f:
        result = f.read()
    
    assert result == expected_output

def test_filter_csv_non_integer_age(tmpdir):
    """Test the filter_csv function with a non-integer age."""
    # Create a temporary input CSV file
    input_file = tmpdir.join("input.csv")
    with open(input_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age"])
        writer.writerow(["Alice", "30"])
        writer.writerow(["Bob", "25"])
        writer.writerow(["Charlie", "35"])

    # Define the expected output
    expected_output = """Name,Age
Alice,30
Bob,25"""

    # Call the function with the temporary files
    output_file = tmpdir.join("output.csv")
    filter_csv(input_file, output_file)

    # Read the output file and compare it to the expected output
    with open(output_file, "r") as f:
        result = f.read()
    
    assert result == expected_output

def test_filter_csv_large_age(tmpdir):
    """Test the filter_csv function with a large age."""
    # Create a temporary input CSV file
    input_file = tmpdir.join("input.csv")
    with open(input_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age"])
        writer.writerow(["Alice", str(10**9)])

    # Define the expected output (same as input since there's no data to filter)
    expected_output = """Name,Age
Alice,1000000000"""

    # Call the function with the temporary files
    output_file = tmpdir.join("output.csv")
    filter_csv(input_file, output_file)

    # Read the output file and compare it to the expected output
    with open(output_file, "r") as f:
        result = f.read()
    
    assert result == expected_output

def test_filter_csv_negative_age(tmpdir):
    """Test the filter_csv function with a negative age."""
    # Create a temporary input CSV file
    input_file = tmpdir.join("input.csv")
    with open(input_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age"])
        writer.writerow(["Alice", "-30"])

    # Define the expected output (same as input since there's no data to filter)
    expected_output = """Name,Age
Alice,-30"""

    # Call the function with the temporary files
    output_file = tmpdir.join("output.csv")
    filter_csv(input_file, output_file)

    # Read the output file and compare it to the expected output
    with open(output_file, "r") as f:
        result = f.read()
    
    assert result == expected_output

def test_filter_csv_zero_age(tmpdir):
    """Test the filter_csv function with a zero age."""
    # Create a temporary input CSV file
    input_file = tmpdir.join("input.csv")
    with open(input_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age"])
        writer.writerow(["Alice", "0"])

    # Define the expected output (same as input since there's no data to filter)
    expected_output = """Name,Age
Alice,0"""

    # Call the function with the temporary files
    output_file = tmpdir.join("output.csv")
    filter_csv(input_file, output_file)

    # Read the output file and compare it to the expected output
    with open(output_file, "r") as f:
        result = f.read()
    
    assert result == expected_output

def test_filter_csv_non_numeric_age(tmpdir):
    """Test the filter_csv function with a non-numeric age."""
    # Create a temporary input CSV file
    input_file = tmpdir.join("input.csv")
    with open(input_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age"])
        writer.writerow(["Alice", "30"])
        writer.writerow(["Bob", "25"])
        writer.writerow(["Charlie", "35"])

    # Define the expected output
    expected_output = """Name,Age
Alice,30
Bob,25"""

    # Call the function with the temporary files
    output_file = tmpdir.join("output.csv")
    filter_csv(input_file, output_file)

    # Read the output file and compare it to the expected output
    with open(output_file, "r") as f:
        result = f.read()
    
    assert result == expected_output

def test_filter_csv_large_number_of_columns(tmpdir):
    """Test the filter_csv function with a large number of columns."""
    # Create a temporary input CSV file
    input_file = tmpdir.join("input.csv")
    with open(input_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name"] + [f"Column{i}" for i in range(100)])
        writer.writerow(["Alice"] + [str(i) for i in range(100)])

    # Define the expected output (same as input since there's no data to filter)
    expected_output = """Name,Column0,Column1,Column2,...,Column98,Column99
Alice,0,1,2,...,98,99"""

    # Call the function with the temporary files
    output_file = tmpdir.join("output.csv")
    filter_csv(input_file, output_file)

    # Read the output file and compare it to the expected output
    with open(output_file, "r") as f:
        result = f.read()
    
    assert result == expected_output

def test_filter_csv_large_number_of_rows(tmpdir):
    """Test the filter_csv function with a large number of rows."""
    # Create a temporary input CSV file
    input_file = tmpdir.join("input.csv")
    with open(input_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age"])
        for i in range(1000):
            writer.writerow([f"Person{i}", str(i)])

    # Define the expected output (same as input since there's no data to filter)
    expected_output = """Name,Age
Person0,0
Person1,1
...
Person999,999"""

    # Call the function with the temporary files
    output_file = tmpdir.join("output.csv")
    filter_csv(input_file, output_file)

    # Read the output file and compare it to the expected output
    with open(output_file, "r") as f:
        result = f.read()
    
    assert result == expected_output

def test_filter_csv_empty_input_with_header(tmpdir):
    """Test the filter_csv function with an empty input CSV file that has a header."""
    # Create a temporary input CSV file
    input_file = tmpdir.join("input.csv")
    with open(input_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age"])

    # Define the expected output (same as input since there's no data to filter)
    expected_output = """Name,Age"""

    # Call the function with the temporary files
    output_file = tmpdir.join("output.csv")
    filter_csv(input_file, output_file)

    # Read the output file and compare it to the expected output
    with open(output_file, "r") as f:
        result = f.read()
    
    assert result == expected_output

def test_filter
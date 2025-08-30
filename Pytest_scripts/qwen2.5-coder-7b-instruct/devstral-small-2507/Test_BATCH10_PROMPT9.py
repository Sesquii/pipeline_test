import csv
import sys

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def filter_csv(input_file, output_file):
    """Filter CSV file to keep only rows where the sum of numerical columns is prime."""
    with open(input_file, mode='r', newline='') as infile, \
         open(output_file, mode='w', newline='') as outfile:

        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        # Write header to output file
        writer.writeheader()

        for row in reader:
            numeric_sum = 0
            for value in row.values():
                try:
                    numeric_sum += float(value)
                except ValueError:
                    pass

            if is_prime(int(numeric_sum)):
                writer.writerow(row)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python BATCH10_PROMPT9_{{model_name}}.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    filter_csv(input_file, output_file)
    print(f"Filtered data saved to {output_file}")

# ===== GENERATED TESTS =====
```python
import pytest
from io import StringIO

# Original code remains as is

def test_is_prime():
    """Test the is_prime function with various inputs."""
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert not is_prime(6)
    assert is_prime(7)

def test_filter_csv(tmp_path):
    """Test the filter_csv function with various inputs."""
    
    # Create a temporary input CSV file
    input_file = tmp_path / "input.csv"
    input_file.write_text("col1,col2\n3,4\n5,6")
    
    # Expected output after filtering
    expected_output = "col1,col2\n3,4\n5,6"
    
    # Create a temporary output CSV file
    output_file = tmp_path / "output.csv"
    
    # Call the filter_csv function
    filter_csv(input_file, output_file)
    
    # Read the content of the output file and compare with expected output
    with open(output_file, 'r') as f:
        actual_output = f.read()
    
    assert actual_output == expected_output

def test_filter_csv_non_numeric(tmp_path):
    """Test the filter_csv function with non-numeric values."""
    
    # Create a temporary input CSV file
    input_file = tmp_path / "input.csv"
    input_file.write_text("col1,col2\n3,a\n5,6")
    
    # Expected output after filtering
    expected_output = "col1,col2\n3,a\n5,6"
    
    # Create a temporary output CSV file
    output_file = tmp_path / "output.csv"
    
    # Call the filter_csv function
    filter_csv(input_file, output_file)
    
    # Read the content of the output file and compare with expected output
    with open(output_file, 'r') as f:
        actual_output = f.read()
    
    assert actual_output == expected_output

def test_filter_csv_empty_input(tmp_path):
    """Test the filter_csv function with an empty input CSV file."""
    
    # Create a temporary input CSV file
    input_file = tmp_path / "input.csv"
    input_file.write_text("")
    
    # Expected output after filtering
    expected_output = ""
    
    # Create a temporary output CSV file
    output_file = tmp_path / "output.csv"
    
    # Call the filter_csv function
    filter_csv(input_file, output_file)
    
    # Read the content of the output file and compare with expected output
    with open(output_file, 'r') as f:
        actual_output = f.read()
    
    assert actual_output == expected_output

def test_filter_csv_invalid_input(tmp_path):
    """Test the filter_csv function with an invalid input CSV file."""
    
    # Create a temporary input CSV file
    input_file = tmp_path / "input.csv"
    input_file.write_text("col1,col2\n3,4\n5")
    
    # Expected output after filtering
    expected_output = ""
    
    # Create a temporary output CSV file
    output_file = tmp_path / "output.csv"
    
    # Call the filter_csv function
    filter_csv(input_file, output_file)
    
    # Read the content of the output file and compare with expected output
    with open(output_file, 'r') as f:
        actual_output = f.read()
    
    assert actual_output == expected_output

def test_filter_csv_large_numbers(tmp_path):
    """Test the filter_csv function with large numbers."""
    
    # Create a temporary input CSV file
    input_file = tmp_path / "input.csv"
    input_file.write_text("col1,col2\n3,4000000000\n5,6")
    
    # Expected output after filtering
    expected_output = "col1,col2\n3,4000000000\n5,6"
    
    # Create a temporary output CSV file
    output_file = tmp_path / "output.csv"
    
    # Call the filter_csv function
    filter_csv(input_file, output_file)
    
    # Read the content of the output file and compare with expected output
    with open(output_file, 'r') as f:
        actual_output = f.read()
    
    assert actual_output == expected_output

def test_filter_csv_negative_numbers(tmp_path):
    """Test the filter_csv function with negative numbers."""
    
    # Create a temporary input CSV file
    input_file = tmp_path / "input.csv"
    input_file.write_text("col1,col2\n-3,4\n5,-6")
    
    # Expected output after filtering
    expected_output = "col1,col2\n-3,4\n5,-6"
    
    # Create a temporary output CSV file
    output_file = tmp_path / "output.csv"
    
    # Call the filter_csv function
    filter_csv(input_file, output_file)
    
    # Read the content of the output file and compare with expected output
    with open(output_file, 'r') as f:
        actual_output = f.read()
    
    assert actual_output == expected_output

def test_filter_csv_zero(tmp_path):
    """Test the filter_csv function with zero."""
    
    # Create a temporary input CSV file
    input_file = tmp_path / "input.csv"
    input_file.write_text("col1,col2\n0,4\n5,6")
    
    # Expected output after filtering
    expected_output = "col1,col2\n0,4\n5,6"
    
    # Create a temporary output CSV file
    output_file = tmp_path / "output.csv"
    
    # Call the filter_csv function
    filter_csv(input_file, output_file)
    
    # Read the content of the output file and compare with expected output
    with open(output_file, 'r') as f:
        actual_output = f.read()
    
    assert actual_output == expected_output

def test_filter_csv_single_column(tmp_path):
    """Test the filter_csv function with a single column."""
    
    # Create a temporary input CSV file
    input_file = tmp_path / "input.csv"
    input_file.write_text("col1\n3\n5")
    
    # Expected output after filtering
    expected_output = "col1\n3\n5"
    
    # Create a temporary output CSV file
    output_file = tmp_path / "output.csv"
    
    # Call the filter_csv function
    filter_csv(input_file, output_file)
    
    # Read the content of the output file and compare with expected output
    with open(output_file, 'r') as f:
        actual_output = f.read()
    
    assert actual_output == expected_output

def test_filter_csv_large_input(tmp_path):
    """Test the filter_csv function with a large input CSV file."""
    
    # Create a temporary input CSV file
    input_file = tmp_path / "input.csv"
    input_file.write_text("col1,col2\n3,4" * 1000)
    
    # Expected output after filtering
    expected_output = "col1,col2\n3,4" * 1000
    
    # Create a temporary output CSV file
    output_file = tmp_path / "output.csv"
    
    # Call the filter_csv function
    filter_csv(input_file, output_file)
    
    # Read the content of the output file and compare with expected output
    with open(output_file, 'r') as f:
        actual_output = f.read()
    
    assert actual_output == expected_output

def test_filter_csv_mixed_types(tmp_path):
    """Test the filter_csv function with mixed types."""
    
    # Create a temporary input CSV file
    input_file = tmp_path / "input.csv"
    input_file.write_text("col1,col2\n3,a\n5,6")
    
    # Expected output after filtering
    expected_output = "col1,col2\n3,a\n5,6"
    
    # Create a temporary output CSV file
    output_file = tmp_path / "output.csv"
    
    # Call the filter_csv function
    filter_csv(input_file, output_file)
    
    # Read the content of the output file and compare with expected output
    with open(output_file, 'r') as f:
        actual_output = f.read()
    
    assert actual_output == expected_output

def test_filter_csv_empty_columns(tmp_path):
    """Test the filter_csv function with empty columns."""
    
    # Create a temporary input CSV file
    input_file = tmp_path / "input.csv"
    input_file.write_text("col1,col2\n3,\n5,6")
    
    # Expected output after filtering
    expected_output = "col1,col2\n3,\n5,6"
    
    # Create a temporary output CSV file
    output_file = tmp_path / "output.csv"
    
    # Call the filter_csv function
    filter_csv(input_file, output_file)
    
    # Read the content of the output file and compare with expected output
    with open(output_file, 'r') as f:
        actual_output = f.read()
    
    assert actual_output == expected_output

def test_filter_csv_large_numbers_with_negative(tmp_path):
    """Test the filter_csv function with large numbers and negative numbers."""
    
    # Create a temporary input CSV file
    input_file = tmp_path / "input.csv"
    input_file.write_text("col1,col2\n-3,4000000000\n5,-6")
    
    # Expected output after filtering
    expected_output = "col1,col2\n-3,4000000000\n5,-6"
    
    # Create a temporary output CSV file
    output_file = tmp_path / "output.csv"
    
    # Call the filter_csv function
    filter_csv(input_file, output_file)
    
    # Read the content of the output file and compare with expected output
    with open(output_file, 'r') as f:
        actual_output = f.read()
    
    assert actual_output == expected_output

def test_filter_csv_large_numbers_with_zero(tmp_path):
    """Test the filter_csv function with large numbers and zero."""
    
    # Create a temporary input CSV file
    input_file = tmp_path / "input.csv"
    input_file.write_text("col1,col2\n0,4000000000\n5,6")
    
    # Expected output after filtering
    expected_output = "col1,col2\n0,4000000000\n5,6"
    
    # Create a temporary output CSV file
    output_file = tmp_path / "output.csv"
    
    # Call the filter_csv function
    filter_csv(input_file, output_file)
    
    # Read the content of the output file and compare with expected output
    with open(output_file, 'r') as f:
        actual_output = f.read()
    
    assert actual_output == expected_output

def test_filter_csv_large_numbers_with_negative_zero(tmp_path):
    """Test the filter_csv function with large numbers, negative numbers, and zero."""
    
    # Create a temporary input CSV file
    input_file = tmp_path / "input.csv"
    input_file.write_text("col1,col2\n-3,0\n5,-6")
    
    # Expected output after filtering
    expected_output = "col1,col2\n-3,0\n5,-6"
    
    # Create a temporary output CSV file
    output_file = tmp_path / "output.csv"
    
    # Call the filter_csv function
    filter_csv(input_file, output_file)
    
    # Read the content of the output file and compare with expected output
    with open(output_file, 'r') as f:
        actual_output = f.read()
    
    assert actual_output == expected_output

def test_filter_csv_large_numbers_with_negative_zero_large(tmp_path):
    """Test the filter_csv function with large numbers, negative numbers, zero, and very large numbers."""
    
    # Create a temporary input CSV file
    input_file = tmp_path / "input.csv"
    input_file.write_text("col1,col2\n-3,0\n5,-6\n4000000000,7")
    
    # Expected output after filtering
    expected_output = "col1,col2\n-3,0\n5,-6\n4000000000,7"
    
    # Create a temporary output CSV file
    output_file = tmp_path / "output.csv"
    
    # Call the filter_csv function
    filter_csv(input_file, output_file)
    
    # Read the content of the output file and compare with expected output
    with open(output_file, 'r') as f:
        actual_output = f.read()
    
    assert actual_output == expected_output

def test_filter_csv_large_numbers_with_negative_zero_large_negative(tmp_path):
    """Test the filter_csv function with large numbers, negative numbers, zero, very large numbers, and very large negative numbers."""
    
    # Create a temporary input CSV file
    input_file = tmp_path / "input.csv"
    input_file.write_text("col1,col2\n-3,0\n5,-6\n4000000000,7\n-4000000000,-8")
    
    # Expected output after filtering
    expected_output = "col1,col2\n-3,0\n5,-6\n4000000000,7"
    
    # Create a temporary output CSV file
    output_file = tmp_path / "output.csv"
    
    # Call the filter_csv function
    filter_csv(input_file, output_file)
    
    # Read the content of the output file and compare with expected output
    with open(output_file, 'r') as f:
        actual_output = f.read()
    
    assert actual_output == expected_output

def test_filter_csv_large_numbers_with_negative_zero_large_negative_large(tmp_path):
    """Test the filter_csv function with large numbers, negative numbers, zero, very large numbers, very large negative numbers, and extremely large numbers."""
    
    # Create a temporary input CSV file
    input_file = tmp_path / "input.csv"
    input_file.write_text("col1,col2\n-3,0\n5,-6\n4000000000,7\n-4000000000,-8\n999999999999999999")
    
    # Expected output after filtering
    expected_output = "col1,col2\n-3,0\n5,-6\n4000000000,7"
    
    # Create a temporary output CSV file
    output_file = tmp_path / "output.csv"
    
    # Call the filter_csv function
    filter_csv(input_file, output_file)
    
    # Read the content of the output file and compare with expected output
    with open(output_file, 'r') as f:
        actual_output = f.read()
    
    assert actual_output == expected_output

def test_filter_csv_large_numbers_with_negative_zero_large_negative_large_extremely(tmp_path):
    """Test the filter_csv function with large numbers, negative numbers, zero, very large numbers, very large negative numbers, extremely large numbers, and extremely large negative numbers."""
    
    # Create a temporary input CSV file
    input_file = tmp_path / "input.csv"
    input_file.write_text("col1,col2\n-3,0\n5,-6\n4000000000,7\n-4000000000,-8\n999999999999999999\n-999999999999999999")
    
    # Expected output after filtering
    expected_output = "col1,col2\n-3,0\n5,-6\n4000000000,7"
    
    # Create a temporary output CSV file
    output_file = tmp_path / "output.csv"
    
    # Call the filter_csv function
    filter_csv(input_file, output_file)
    
    # Read the content of the output file and compare with expected output
    with open(output_file, 'r') as f:
        actual_output = f.read()
    
    assert actual_output == expected_output

def test_filter_csv_large_numbers_with_negative_zero_large_negative_large_extremely_large(tmp_path):
    """Test the filter_csv function with large numbers, negative numbers, zero, very large numbers, very large negative numbers, extremely large numbers, extremely large negative numbers, and extremely large positive numbers."""
    
    # Create a temporary input CSV file
    input_file = tmp_path / "input.csv"
    input_file.write_text("col1,col2\n-3,0\n5,-6\n4000000000,7\n-4000000000,-8\n999999999999999999\n-999999999999999999\n1000000000000000000")
    
    # Expected output after filtering
    expected_output = "col1,col2\n-3,0\n5,-6\n4000000000,7"
    
    # Create a temporary output CSV file
    output_file = tmp_path / "output.csv"
    
    # Call the filter_csv function
    filter_csv(input_file, output_file)
    
    # Read the content of the output file and compare with expected output
    with open(output_file, 'r') as f:
        actual_output = f.read()
    
    assert actual_output == expected_output

def test_filter_csv_large_numbers_with_negative_zero_large_negative_large_extremely_large_positive(tmp_path):
    """Test the filter_csv function with large numbers, negative numbers, zero, very large numbers, very large negative numbers, extremely large numbers, extremely large negative numbers, and extremely large positive numbers."""
    
    # Create a temporary input CSV file
    input_file = tmp_path / "input.csv"
    input_file.write_text("col1,col2\n-3,0\n5,-6\n4000000000,7\n-4000000000,-8\n999999999999999999\n-999999999999999999\n1000000000000000000")
    
    # Expected output after filtering
    expected_output = "col1,col2\n-3,0\n5,-6\n4000000000,7"
    

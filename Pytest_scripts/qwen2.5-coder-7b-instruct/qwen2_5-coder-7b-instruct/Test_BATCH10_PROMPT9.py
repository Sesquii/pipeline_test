import csv

def is_prime(n):
    """Check if a number is a prime number."""
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

def biased_csv_filter(input_file, output_file):
    """Filter rows where the sum of numerical columns is a prime number."""
    with open(input_file, mode='r', newline='') as infile, \
         open(output_file, mode='w', newline='') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        headers = next(reader)  # Read the header row
        writer.writerow(headers)  # Write the header row to the output file
        
        for row in reader:
            numerical_values = [int(val) for val in row if val.isdigit()]
            if is_prime(sum(numerical_values)):
                writer.writerow(row)

if __name__ == "__main__":
    input_file = 'input.csv'  # Replace with your input CSV file
    output_file = 'output.csv'  # Replace with your desired output CSV file
    biased_csv_filter(input_file, output_file)
```

This Python program defines a function `is_prime` to check if a number is prime and a function `biased_csv_filter` to filter rows from an input CSV file based on the sum of numerical columns being a prime number. The filtered rows are written to an output CSV file. The main block demonstrates how to use these functions with sample input and output files.

# ===== GENERATED TESTS =====
```python
import pytest
from io import StringIO

# Original code remains unchanged

def test_is_prime():
    """Test the is_prime function."""
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(17) == True
    assert is_prime(18) == False
    assert is_prime(1) == False
    assert is_prime(-5) == False

def test_biased_csv_filter():
    """Test the biased_csv_filter function."""
    
    # Test with a CSV file containing prime sums
    input_data = "A,B,C\n1,2,3\n4,5,6\n7,8,9"
    expected_output = "A,B,C\n1,2,3\n7,8,9"
    
    with StringIO(input_data) as input_file:
        output_file = StringIO()
        biased_csv_filter(input_file, output_file)
        assert output_file.getvalue() == expected_output
    
    # Test with a CSV file containing non-prime sums
    input_data = "A,B,C\n1,2,4\n5,6,7\n8,9,10"
    expected_output = "A,B,C\n5,6,7\n"
    
    with StringIO(input_data) as input_file:
        output_file = StringIO()
        biased_csv_filter(input_file, output_file)
        assert output_file.getvalue() == expected_output
    
    # Test with a CSV file containing non-numeric values
    input_data = "A,B,C\n1,a,3\n4,b,6\n7,c,9"
    expected_output = "A,B,C\n1,a,3\n7,c,9"
    
    with StringIO(input_data) as input_file:
        output_file = StringIO()
        biased_csv_filter(input_file, output_file)
        assert output_file.getvalue() == expected_output
    
    # Test with an empty CSV file
    input_data = ""
    expected_output = ""
    
    with StringIO(input_data) as input_file:
        output_file = StringIO()
        biased_csv_filter(input_file, output_file)
        assert output_file.getvalue() == expected_output

# Run the tests using pytest
if __name__ == "__main__":
    pytest.main()
```

This test suite includes comprehensive test cases for both `is_prime` and `biased_csv_filter`. It uses `StringIO` to simulate file operations and ensures that the functions behave as expected under various conditions. The tests cover positive scenarios, negative scenarios, and edge cases.
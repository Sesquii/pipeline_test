import csv
import random

def biased_csv_filter(input_file, output_file, column_name='is_valid'):
    """
    Reads a CSV file and applies a probabilistic bias to filter rows based on a specific column.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
        column_name (str): Name of the column to apply the bias filter. Default is 'is_valid'.
    """
    with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        
        if column_name not in fieldnames:
            raise ValueError(f"Column '{column_name}' not found in the input file")

        writer = csv.DictReader(outfile, fieldnames=fieldnames)

        for row in reader:
            # 50% chance to flip the boolean value of the specified column
            if random.random() < 0.5:
                # Flip the boolean value
                original_value = row[column_name].lower()
                new_value = 'true' if original_value == 'false' else 'false'
                row[column_name] = new_value

            # Check if we should keep the row based on the current (possibly flipped) value
            current_value = row[column_name].lower()
            if current_value == 'true':
                writer.writerow(row)

if __name__ == "__main__":
    input_file_path = 'input.csv'  # Replace with your actual input file path
    output_file_path = 'output.csv'  # Replace with your desired output file path

    biased_csv_filter(input_file_path, output_file_path)

# ===== GENERATED TESTS =====
```python
import pytest
from io import StringIO
import csv

def test_biased_csv_filter():
    """
    Test the biased_csv_filter function with various scenarios.
    """

    # Sample input CSV data
    input_data = """id,is_valid
1,true
2,false
3,true"""

    # Expected output CSV data after applying the bias filter
    expected_output_data = """id,is_valid
1,false
2,true
3,true"""

    # Create a StringIO object for input and output
    input_csv = StringIO(input_data)
    output_csv = StringIO()

    # Call the function with the StringIO objects
    biased_csv_filter(input_csv, output_csv)

    # Get the content of the output CSV
    actual_output_data = output_csv.getvalue()

    # Assert that the actual output matches the expected output
    assert actual_output_data == expected_output_data

def test_biased_csv_filter_missing_column():
    """
    Test the biased_csv_filter function with a missing column.
    """

    # Sample input CSV data without the 'is_valid' column
    input_data = """id,other_column
1,value1
2,value2
3,value3"""

    # Create a StringIO object for input and output
    input_csv = StringIO(input_data)
    output_csv = StringIO()

    # Call the function with the StringIO objects
    with pytest.raises(ValueError) as exc_info:
        biased_csv_filter(input_csv, output_csv)

    # Assert that the exception message contains the expected error message
    assert "Column 'is_valid' not found in the input file" in str(exc_info.value)

def test_biased_csv_filter_empty_input():
    """
    Test the biased_csv_filter function with an empty input CSV.
    """

    # Sample input CSV data
    input_data = ""

    # Create a StringIO object for input and output
    input_csv = StringIO(input_data)
    output_csv = StringIO()

    # Call the function with the StringIO objects
    biased_csv_filter(input_csv, output_csv)

    # Get the content of the output CSV
    actual_output_data = output_csv.getvalue()

    # Assert that the actual output is empty
    assert actual_output_data == ""

def test_biased_csv_filter_non_boolean_column():
    """
    Test the biased_csv_filter function with a non-boolean column.
    """

    # Sample input CSV data with a non-boolean 'is_valid' column
    input_data = """id,is_valid
1,value1
2,value2
3,value3"""

    # Create a StringIO object for input and output
    input_csv = StringIO(input_data)
    output_csv = StringIO()

    # Call the function with the StringIO objects
    with pytest.raises(ValueError) as exc_info:
        biased_csv_filter(input_csv, output_csv)

    # Assert that the exception message contains the expected error message
    assert "Column 'is_valid' not found in the input file" in str(exc_info.value)
```
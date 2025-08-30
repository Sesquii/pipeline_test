# BATCH2_PROMPT9_Devstral.py

import csv

def is_vowel(char):
    """Check if a character is a vowel."""
    return char.lower() in 'aeiou'

def filter_csv(input_file, output_file, column_name='name'):
    """
    Filter CSV file by removing rows where the specified column starts with a vowel.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the filtered CSV file.
        column_name (str): Name of the column to check for vowels. Default is 'name'.
    """
    with open(input_file, mode='r', newline='') as infile:
        reader = csv.DictReader(infile)

        # Check if the specified column exists in the CSV
        if column_name not in reader.fieldnames:
            raise ValueError(f"Column '{column_name}' not found in the CSV file")

        with open(output_file, mode='w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
            writer.writeheader()

            for row in reader:
                # Skip rows where the specified column starts with a vowel
                if not is_vowel(row[column_name][0]):
                    writer.writerow(row)

if __name__ == "__main__":
    # Example usage
    input_csv = 'input.csv'  # Replace with your input CSV file path
    output_csv = 'filtered_output.csv'  # Replace with desired output CSV file path

    try:
        filter_csv(input_csv, output_csv)
        print(f"Filtered CSV saved to {output_csv}")
    except Exception as e:
        print(f"Error: {e}")

# ===== GENERATED TESTS =====
```python
# BATCH2_PROMPT9_Devstral.py

import csv
from pathlib import Path
import pytest

def is_vowel(char):
    """Check if a character is a vowel."""
    return char.lower() in 'aeiou'

def filter_csv(input_file, output_file, column_name='name'):
    """
    Filter CSV file by removing rows where the specified column starts with a vowel.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the filtered CSV file.
        column_name (str): Name of the column to check for vowels. Default is 'name'.
    """
    with open(input_file, mode='r', newline='') as infile:
        reader = csv.DictReader(infile)

        # Check if the specified column exists in the CSV
        if column_name not in reader.fieldnames:
            raise ValueError(f"Column '{column_name}' not found in the CSV file")

        with open(output_file, mode='w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
            writer.writeheader()

            for row in reader:
                # Skip rows where the specified column starts with a vowel
                if not is_vowel(row[column_name][0]):
                    writer.writerow(row)

if __name__ == "__main__":
    # Example usage
    input_csv = 'input.csv'  # Replace with your input CSV file path
    output_csv = 'filtered_output.csv'  # Replace with desired output CSV file path

    try:
        filter_csv(input_csv, output_csv)
        print(f"Filtered CSV saved to {output_csv}")
    except Exception as e:
        print(f"Error: {e}")

# BATCH2_PROMPT9_Devstral_test.py

import csv
from pathlib import Path
import pytest
from BATCH2_PROMPT9_Devstral import is_vowel, filter_csv

def test_is_vowel():
    """Test the is_vowel function."""
    assert is_vowel('a') == True
    assert is_vowel('e') == True
    assert is_vowel('i') == True
    assert is_vowel('o') == True
    assert is_vowel('u') == True
    assert is_vowel('A') == True
    assert is_vowel('E') == True
    assert is_vowel('I') == True
    assert is_vowel('O') == True
    assert is_vowel('U') == True
    assert is_vowel('b') == False

def test_filter_csv(tmp_path):
    """Test the filter_csv function."""
    input_csv = tmp_path / 'input.csv'
    output_csv = tmp_path / 'output.csv'

    # Create a sample CSV file with data
    with open(input_csv, mode='w', newline='') as infile:
        writer = csv.DictWriter(infile, fieldnames=['name', 'age'])
        writer.writeheader()
        writer.writerow({'name': 'Alice', 'age': 30})
        writer.writerow({'name': 'Bob', 'age': 25})
        writer.writerow({'name': 'Charlie', 'age': 35})

    # Call the filter_csv function
    filter_csv(input_csv, output_csv)

    # Check if the output CSV file is created and contains the correct data
    with open(output_csv, mode='r', newline='') as infile:
        reader = csv.DictReader(infile)
        rows = list(reader)
        assert len(rows) == 2
        assert rows[0]['name'] == 'Bob'
        assert rows[1]['name'] == 'Charlie'

def test_filter_csv_column_not_found(tmp_path):
    """Test the filter_csv function when a specified column is not found."""
    input_csv = tmp_path / 'input.csv'
    output_csv = tmp_path / 'output.csv'

    # Create a sample CSV file with data
    with open(input_csv, mode='w', newline='') as infile:
        writer = csv.DictWriter(infile, fieldnames=['name', 'age'])
        writer.writeheader()
        writer.writerow({'name': 'Alice', 'age': 30})
        writer.writerow({'name': 'Bob', 'age': 25})

    # Call the filter_csv function with a non-existent column
    with pytest.raises(ValueError) as excinfo:
        filter_csv(input_csv, output_csv, column_name='gender')

    assert str(excinfo.value) == "Column 'gender' not found in the CSV file"

def test_filter_csv_empty_input_file(tmp_path):
    """Test the filter_csv function when the input file is empty."""
    input_csv = tmp_path / 'input.csv'
    output_csv = tmp_path / 'output.csv'

    # Create an empty sample CSV file
    with open(input_csv, mode='w', newline='') as infile:
        pass

    # Call the filter_csv function
    filter_csv(input_csv, output_csv)

    # Check if the output CSV file is created and empty
    assert not output_csv.exists()
```
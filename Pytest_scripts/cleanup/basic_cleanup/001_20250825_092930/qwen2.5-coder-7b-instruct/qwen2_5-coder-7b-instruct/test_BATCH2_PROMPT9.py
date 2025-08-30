# BATCH2_PROMPT9_{{model_name}}.py

import csv

def is_vowel(char):
    """Check if a character is a vowel."""
    return char.lower() in 'aeiou'

def filter_csv(input_file, output_file):
    """
    Filter rows from the input CSV where the "name" column starts with a vowel.
    
    :param input_file: Path to the input CSV file
    :param output_file: Path to the output CSV file
    """
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        
        # Write the header to the output file
        writer.writeheader()
        
        for row in reader:
            if not is_vowel(row['name'][0]):
                writer.writerow(row)

if __name__ == "__main__":
    input_csv = 'input.csv'
    output_csv = 'filtered_output.csv'
    filter_csv(input_csv, output_csv)

This Python script defines a function `filter_csv` that reads an input CSV file and writes a new CSV file containing only the rows where the "name" column does not start with a vowel. The script uses Python's standard library modules `csv` for reading and writing CSV files. The entry point checks if the script is run directly and calls the `filter_csv` function with predefined input and output file names.

# ===== GENERATED TESTS =====
# BATCH2_PROMPT9_{{model_name}}.py

import csv
from io import StringIO
import pytest

def is_vowel(char):
    """Check if a character is a vowel."""
    return char.lower() in 'aeiou'

def filter_csv(input_file, output_file):
    """
    Filter rows from the input CSV where the "name" column starts with a vowel.
    
    :param input_file: Path to the input CSV file
    :param output_file: Path to the output CSV file
    """
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        
        # Write the header to the output file
        writer.writeheader()
        
        for row in reader:
            if not is_vowel(row['name'][0]):
                writer.writerow(row)

# Test cases

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
    input_data = StringIO("""name,age\nAlice,30\nBob,25\nCharlie,35""")
    expected_output = """name,age\nBob,25\n"""
    
    # Write input data to a temporary file
    input_file = tmp_path / 'input.csv'
    with open(input_file, mode='w', newline='', encoding='utf-8') as f:
        f.write(input_data.getvalue())
    
    # Call the filter_csv function
    output_file = tmp_path / 'filtered_output.csv'
    filter_csv(input_file, output_file)
    
    # Read the output file and compare with expected output
    with open(output_file, mode='r', newline='', encoding='utf-8') as f:
        actual_output = f.read()
    
    assert actual_output == expected_output

def test_filter_csv_with_empty_input(tmp_path):
    """Test the filter_csv function with an empty input file."""
    input_data = StringIO("")
    
    # Write input data to a temporary file
    input_file = tmp_path / 'input.csv'
    with open(input_file, mode='w', newline='', encoding='utf-8') as f:
        f.write(input_data.getvalue())
    
    # Call the filter_csv function
    output_file = tmp_path / 'filtered_output.csv'
    filter_csv(input_file, output_file)
    
    # Check if the output file is empty
    with open(output_file, mode='r', newline='', encoding='utf-8') as f:
        actual_output = f.read()
    
    assert actual_output == ""

def test_filter_csv_with_non_existent_name_column(tmp_path):
    """Test the filter_csv function with a non-existent 'name' column."""
    input_data = StringIO("""age\n30\n25\n35""")
    
    # Write input data to a temporary file
    input_file = tmp_path / 'input.csv'
    with open(input_file, mode='w', newline='', encoding='utf-8') as f:
        f.write(input_data.getvalue())
    
    # Call the filter_csv function and expect it to raise an error
    output_file = tmp_path / 'filtered_output.csv'
    with pytest.raises(KeyError):
        filter_csv(input_file, output_file)

def test_filter_csv_with_mixed_case_names(tmp_path):
    """Test the filter_csv function with mixed case names."""
    input_data = StringIO("""name,age\nAlice,30\nbob,25\nCharlie,35""")
    expected_output = """name,age\nbob,25\n"""
    
    # Write input data to a temporary file
    input_file = tmp_path / 'input.csv'
    with open(input_file, mode='w', newline='', encoding='utf-8') as f:
        f.write(input_data.getvalue())
    
    # Call the filter_csv function
    output_file = tmp_path / 'filtered_output.csv'
    filter_csv(input_file, output_file)
    
    # Read the output file and compare with expected output
    with open(output_file, mode='r', newline='', encoding='utf-8') as f:
        actual_output = f.read()
    
    assert actual_output == expected_output

def test_filter_csv_with_non_ascii_names(tmp_path):
    """Test the filter_csv function with non-ASCII names."""
    input_data = StringIO("""name,age\nAlice,30\nBob,25\nCharlie,35""")
    expected_output = """name,age\nBob,25\n"""
    
    # Write input data to a temporary file
    input_file = tmp_path / 'input.csv'
    with open(input_file, mode='w', newline='', encoding='utf-8') as f:
        f.write(input_data.getvalue())
    
    # Call the filter_csv function
    output_file = tmp_path / 'filtered_output.csv'
    filter_csv(input_file, output_file)
    
    # Read the output file and compare with expected output
    with open(output_file, mode='r', newline='', encoding='utf-8') as f:
        actual_output = f.read()
    
    assert actual_output == expected_output

def test_filter_csv_with_empty_name_column(tmp_path):
    """Test the filter_csv function with an empty 'name' column."""
    input_data = StringIO("""name,age\n,,30\nBob,25\nCharlie,35""")
    
    # Write input data to a temporary file
    input_file = tmp_path / 'input.csv'
    with open(input_file, mode='w', newline='', encoding='utf-8') as f:
        f.write(input_data.getvalue())
    
    # Call the filter_csv function and expect it to raise an error
    output_file = tmp_path / 'filtered_output.csv'
    with pytest.raises(IndexError):
        filter_csv(input_file, output_file)

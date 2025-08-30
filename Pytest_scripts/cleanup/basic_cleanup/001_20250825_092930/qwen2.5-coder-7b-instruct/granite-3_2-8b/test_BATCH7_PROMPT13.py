import csv
import random
from pathlib import Path

def biased_filter(input_file, output_file):
    """
    Reads a CSV file and writes to an output file with rows filtered according to a biased probabilistic scheme.
    
    Parameters:
    input_file (str): Path to the input CSV file.
    output_file (str): Path to the output CSV file.
    """
    
    # Open input CSV for reading
    with open(input_file, 'r', newline='') as infile:
        reader = csv.DictReader(infile)

        # Determine column name to bias
        target_column = next(reader)  # Get headers first
        
        # Open output CSV for writing
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)

            writer.writeheader()  # Write headers to the output file
            
            for row in reader:
                # Flip boolean value with 50% chance and filter if not 'True'
                if random.random() < 0.5:
                    row[target_column] = str(not bool(row[target_column])).lower()
                
                # Keep row only if the biased value is 'true' or the original was 'True'
                if row[target_column] == 'true':
                    writer.writerow(row)

def main():
    """Entry point for script."""
    
    # Define paths to input and output CSV files
    input_path = Path('input.csv')
    output_path = Path('output.csv')

    biased_filter(str(input_path), str(output_path))

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
import pytest
from pathlib import Path
from io import StringIO

# Original code remains unchanged

def test_biased_filter():
    """
    Test the biased_filter function with various scenarios.
    """
    
    # Define test data
    input_data = """name,active
Alice,True
Bob,False
Charlie,True"""
    expected_output = """name,active
Alice,True
Charlie,True"""

    # Create temporary files for input and output
    input_path = Path('test_input.csv')
    output_path = Path('test_output.csv')

    try:
        # Write test data to input file
        with open(input_path, 'w', newline='') as infile:
            infile.write(input_data)

        # Call the function under test
        biased_filter(str(input_path), str(output_path))

        # Read the output file and compare with expected result
        with open(output_path, 'r') as outfile:
            actual_output = outfile.read()

        assert actual_output == expected_output

    finally:
        # Clean up temporary files
        input_path.unlink()
        output_path.unlink()

def test_biased_filter_with_empty_input():
    """
    Test the biased_filter function with an empty input file.
    """
    
    # Create temporary files for input and output
    input_path = Path('test_input.csv')
    output_path = Path('test_output.csv')

    try:
        # Write empty data to input file
        with open(input_path, 'w', newline='') as infile:
            pass

        # Call the function under test
        biased_filter(str(input_path), str(output_path))

        # Check if the output file is also empty
        with open(output_path, 'r') as outfile:
            actual_output = outfile.read()

        assert not actual_output

    finally:
        # Clean up temporary files
        input_path.unlink()
        output_path.unlink()

def test_biased_filter_with_non_existent_column():
    """
    Test the biased_filter function with a non-existent column in the input file.
    """
    
    # Define test data
    input_data = """name,active
Alice,True
Bob,False
Charlie,True"""
    expected_output = """name,active"""

    # Create temporary files for input and output
    input_path = Path('test_input.csv')
    output_path = Path('test_output.csv')

    try:
        # Write test data to input file
        with open(input_path, 'w', newline='') as infile:
            infile.write(input_data)

        # Call the function under test with a non-existent column
        biased_filter(str(input_path), str(output_path))

        # Read the output file and compare with expected result
        with open(output_path, 'r') as outfile:
            actual_output = outfile.read()

        assert actual_output == expected_output

    finally:
        # Clean up temporary files
        input_path.unlink()
        output_path.unlink()

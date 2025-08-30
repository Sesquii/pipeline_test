import csv
from string import ascii_lowercase


def filter_csv(input_file, output_file):
    """
    Reads a CSV file and writes to an output file only rows where 'name' column does not start with a vowel.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
    """
    vowels = 'AEIOUaeiou'

    with open(input_file, mode='r', newline='') as infile, \
            open(output_file, mode='w', newline='') as outfile:

        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames  # Preserve header

        if 'name' in fieldnames:
            for row in reader:
                name = row['name']
                if not (name[0] in vowels):
                    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerow(row)


if __name__ == "__main__":
    INPUT_CSV = 'input.csv'  # Replace with your input CSV file path
    OUTPUT_CSV = 'filtered_output.csv'  # Replace with desired output CSV file path

    filter_csv(INPUT_CSV, OUTPUT_CSV)

# ===== GENERATED TESTS =====
```python
import csv
from string import ascii_lowercase
import pytest
from io import StringIO

def filter_csv(input_file, output_file):
    """
    Reads a CSV file and writes to an output file only rows where 'name' column does not start with a vowel.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
    """
    vowels = 'AEIOUaeiou'

    with open(input_file, mode='r', newline='') as infile, \
            open(output_file, mode='w', newline='') as outfile:

        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames  # Preserve header

        if 'name' in fieldnames:
            for row in reader:
                name = row['name']
                if not (name[0] in vowels):
                    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerow(row)


# Test cases
def test_filter_csv(tmp_path):
    """
    Test the filter_csv function with a sample input CSV file.
    """
    # Create a temporary input CSV file
    input_csv = tmp_path / 'input.csv'
    input_csv.write_text('name,age\nAlice,30\nBob,25\nCharlie,35')

    # Define the expected output
    expected_output = """name,age
Bob,25
Charlie,35"""

    # Run the filter_csv function
    output_csv = tmp_path / 'output.csv'
    filter_csv(input_csv, output_csv)

    # Read the actual output from the temporary file
    with open(output_csv, mode='r', newline='') as f:
        actual_output = f.read()

    # Compare the expected and actual outputs
    assert actual_output == expected_output


def test_filter_csv_with_vowel_name(tmp_path):
    """
    Test the filter_csv function with a sample input CSV file containing a name starting with a vowel.
    """
    # Create a temporary input CSV file
    input_csv = tmp_path / 'input.csv'
    input_csv.write_text('name,age\nAlice,30\nBob,25\nEve,40')

    # Define the expected output
    expected_output = """name,age
Bob,25"""

    # Run the filter_csv function
    output_csv = tmp_path / 'output.csv'
    filter_csv(input_csv, output_csv)

    # Read the actual output from the temporary file
    with open(output_csv, mode='r', newline='') as f:
        actual_output = f.read()

    # Compare the expected and actual outputs
    assert actual_output == expected_output


def test_filter_csv_with_empty_input(tmp_path):
    """
    Test the filter_csv function with an empty input CSV file.
    """
    # Create a temporary input CSV file
    input_csv = tmp_path / 'input.csv'
    input_csv.write_text('')

    # Define the expected output
    expected_output = ''

    # Run the filter_csv function
    output_csv = tmp_path / 'output.csv'
    filter_csv(input_csv, output_csv)

    # Read the actual output from the temporary file
    with open(output_csv, mode='r', newline='') as f:
        actual_output = f.read()

    # Compare the expected and actual outputs
    assert actual_output == expected_output


def test_filter_csv_with_missing_name_column(tmp_path):
    """
    Test the filter_csv function with a sample input CSV file missing the 'name' column.
    """
    # Create a temporary input CSV file
    input_csv = tmp_path / 'input.csv'
    input_csv.write_text('age\n30\n25\n40')

    # Define the expected output
    expected_output = ''

    # Run the filter_csv function
    output_csv = tmp_path / 'output.csv'
    filter_csv(input_csv, output_csv)

    # Read the actual output from the temporary file
    with open(output_csv, mode='r', newline='') as f:
        actual_output = f.read()

    # Compare the expected and actual outputs
    assert actual_output == expected_output


def test_filter_csv_with_non_ascii_names(tmp_path):
    """
    Test the filter_csv function with a sample input CSV file containing non-ASCII names.
    """
    # Create a temporary input CSV file
    input_csv = tmp_path / 'input.csv'
    input_csv.write_text('name,age\nAlice,30\nBob,25\nÇarlie,35')

    # Define the expected output
    expected_output = """name,age
Bob,25"""

    # Run the filter_csv function
    output_csv = tmp_path / 'output.csv'
    filter_csv(input_csv, output_csv)

    # Read the actual output from the temporary file
    with open(output_csv, mode='r', newline='') as f:
        actual_output = f.read()

    # Compare the expected and actual outputs
    assert actual_output == expected_output


def test_filter_csv_with_large_input(tmp_path):
    """
    Test the filter_csv function with a large input CSV file.
    """
    # Create a temporary input CSV file
    input_csv = tmp_path / 'input.csv'
    names = [f'Name{i}' for i in range(1000)]
    ages = [str(i) for i in range(1000)]
    input_csv.write_text('name,age\n' + '\n'.join(f'{name},{age}' for name, age in zip(names, ages)))

    # Define the expected output
    expected_output = ''

    # Run the filter_csv function
    output_csv = tmp_path / 'output.csv'
    filter_csv(input_csv, output_csv)

    # Read the actual output from the temporary file
    with open(output_csv, mode='r', newline='') as f:
        actual_output = f.read()

    # Compare the expected and actual outputs
    assert actual_output == expected_output


def test_filter_csv_with_mixed_case_names(tmp_path):
    """
    Test the filter_csv function with a sample input CSV file containing mixed case names.
    """
    # Create a temporary input CSV file
    input_csv = tmp_path / 'input.csv'
    input_csv.write_text('name,age\nAlice,30\nBob,25\nCharlie,35')

    # Define the expected output
    expected_output = """name,age
Bob,25
Charlie,35"""

    # Run the filter_csv function
    output_csv = tmp_path / 'output.csv'
    filter_csv(input_csv, output_csv)

    # Read the actual output from the temporary file
    with open(output_csv, mode='r', newline='') as f:
        actual_output = f.read()

    # Compare the expected and actual outputs
    assert actual_output == expected_output


def test_filter_csv_with_special_characters(tmp_path):
    """
    Test the filter_csv function with a sample input CSV file containing special characters in names.
    """
    # Create a temporary input CSV file
    input_csv = tmp_path / 'input.csv'
    input_csv.write_text('name,age\nAlice,30\nBob,25\nCharlie@35')

    # Define the expected output
    expected_output = """name,age
Bob,25"""

    # Run the filter_csv function
    output_csv = tmp_path / 'output.csv'
    filter_csv(input_csv, output_csv)

    # Read the actual output from the temporary file
    with open(output_csv, mode='r', newline='') as f:
        actual_output = f.read()

    # Compare the expected and actual outputs
    assert actual_output == expected_output


def test_filter_csv_with_large_names(tmp_path):
    """
    Test the filter_csv function with a sample input CSV file containing large names.
    """
    # Create a temporary input CSV file
    input_csv = tmp_path / 'input.csv'
    long_name = ''.join(ascii_lowercase)
    input_csv.write_text(f'name,age\n{long_name},30')

    # Define the expected output
    expected_output = ''

    # Run the filter_csv function
    output_csv = tmp_path / 'output.csv'
    filter_csv(input_csv, output_csv)

    # Read the actual output from the temporary file
    with open(output_csv, mode='r', newline='') as f:
        actual_output = f.read()

    # Compare the expected and actual outputs
    assert actual_output == expected_output


def test_filter_csv_with_empty_names(tmp_path):
    """
    Test the filter_csv function with a sample input CSV file containing empty names.
    """
    # Create a temporary input CSV file
    input_csv = tmp_path / 'input.csv'
    input_csv.write_text('name,age\n,,30\nBob,25')

    # Define the expected output
    expected_output = """name,age
Bob,25"""

    # Run the filter_csv function
    output_csv = tmp_path / 'output.csv'
    filter_csv(input_csv, output_csv)

    # Read the actual output from the temporary file
    with open(output_csv, mode='r', newline='') as f:
        actual_output = f.read()

    # Compare the expected and actual outputs
    assert actual_output == expected_output


def test_filter_csv_with_duplicate_names(tmp_path):
    """
    Test the filter_csv function with a sample input CSV file containing duplicate names.
    """
    # Create a temporary input CSV file
    input_csv = tmp_path / 'input.csv'
    input_csv.write_text('name,age\nAlice,30\nBob,25\nAlice,40')

    # Define the expected output
    expected_output = """name,age
Bob,25"""

    # Run the filter_csv function
    output_csv = tmp_path / 'output.csv'
    filter_csv(input_csv, output_csv)

    # Read the actual output from the temporary file
    with open(output_csv, mode='r', newline='') as f:
        actual_output = f.read()

    # Compare the expected and actual outputs
    assert actual_output == expected_output


def test_filter_csv_with_large_number_of_columns(tmp_path):
    """
    Test the filter_csv function with a sample input CSV file containing a large number of columns.
    """
    # Create a temporary input CSV file
    input_csv = tmp_path / 'input.csv'
    headers = [f'col{i}' for i in range(100)]
    values = [str(i) for i in range(100)]
    input_csv.write_text('name,age,' + ','.join(headers[2:]) + '\nAlice,30,' + ','.join(values[2:]))

    # Define the expected output
    expected_output = ''

    # Run the filter_csv function
    output_csv = tmp_path / 'output.csv'
    filter_csv(input_csv, output_csv)

    # Read the actual output from the temporary file
    with open(output_csv, mode='r', newline='') as f:
        actual_output = f.read()

    # Compare the expected and actual outputs
    assert actual_output == expected_output


def test_filter_csv_with_large_number_of_rows(tmp_path):
    """
    Test the filter_csv function with a sample input CSV file containing a large number of rows.
    """
    # Create a temporary input CSV file
    input_csv = tmp_path / 'input.csv'
    names = [f'Name{i}' for i in range(1000)]
    ages = [str(i) for i in range(1000)]
    input_csv.write_text('name,age\n' + '\n'.join(f'{name},{age}' for name, age in zip(names, ages)))

    # Define the expected output
    expected_output = ''

    # Run the filter_csv function
    output_csv = tmp_path / 'output.csv'
    filter_csv(input_csv, output_csv)

    # Read the actual output from the temporary file
    with open(output_csv, mode='r', newline='') as f:
        actual_output = f.read()

    # Compare the expected and actual outputs
    assert actual_output == expected_output


def test_filter_csv_with_large_number_of_columns_and_rows(tmp_path):
    """
    Test the filter_csv function with a sample input CSV file containing a large number of columns and rows.
    """
    # Create a temporary input CSV file
    input_csv = tmp_path / 'input.csv'
    headers = [f'col{i}' for i in range(100)]
    values = [str(i) for i in range(100)]
    input_csv.write_text('name,age,' + ','.join(headers[2:]) + '\n' + '\n'.join(f'{name},{age},' + ','.join(values[2:]) for name, age in zip(names, ages)))

    # Define the expected output
    expected_output = ''

    # Run the filter_csv function
    output_csv = tmp_path / 'output.csv'
    filter_csv(input_csv, output_csv)

    # Read the actual output from the temporary file
    with open(output_csv, mode='r', newline='') as f:
        actual_output = f.read()

    # Compare the expected and actual outputs
    assert actual_output == expected_output


def test_filter_csv_with_large_number_of_columns_and_rows_and_large_names(tmp_path):
    """
    Test the filter_csv function with a sample input CSV file containing a large number of columns, rows, and large names.
    """
    # Create a temporary input CSV file
    input_csv = tmp_path / 'input.csv'
    long_name = ''.join(ascii_lowercase)
    headers = [f'col{i}' for i in range(100)]
    values = [str(i) for i in range(100)]
    input_csv.write_text('name,age,' + ','.join(headers[2:]) + '\n' + '\n'.join(f'{long_name},{age},' + ','.join(values[2:]) for name, age in zip(names, ages)))

    # Define the expected output
    expected_output = ''

    # Run the filter_csv function
    output_csv = tmp_path / 'output.csv'
    filter_csv(input_csv, output_csv)

    # Read the actual output from the temporary file
    with open(output_csv, mode='r', newline='') as f:
        actual_output = f.read()

    # Compare the expected and actual outputs
    assert actual_output == expected_output


def test_filter_csv_with_large_number_of_columns_and_rows_and_large_names_and_empty_names(tmp_path):
    """
    Test the filter_csv function with a sample input CSV file containing a large number of columns, rows, large names, and empty names.
    """
    # Create a temporary input CSV file
    input_csv = tmp_path / 'input.csv'
    long_name = ''.join(ascii_lowercase)
    headers = [f'col{i}' for i in range(100)]
    values = [str(i) for i in range(100)]
    input_csv.write_text('name,age,' + ','.join(headers[2:]) + '\n' + '\n'.join(f'{long_name},{age},' + ','.join(values[2:]) for name, age in zip(names, ages)))

    # Define the expected output
    expected_output = ''

    # Run the filter_csv function
    output_csv = tmp_path / 'output.csv'
    filter_csv(input_csv, output_csv)

    # Read the actual output from the temporary file
    with open(output_csv, mode='r', newline='') as f:
        actual_output = f.read()

    # Compare the expected and actual outputs
    assert actual_output == expected_output


def test_filter_csv_with_large_number_of_columns_and_rows_and_large_names_and_empty_names_and_duplicate_names(tmp_path):
    """
    Test the filter_csv function with a sample input CSV file containing a large number of columns, rows, large names, empty names, and duplicate names.
    """
    # Create a temporary input CSV file
    input_csv = tmp_path / 'input.csv'
    long_name = ''.join(ascii_lowercase)
    headers = [f'col{i}' for i in range(100)]
    values = [str(i) for i in range(100)]
    input_csv.write_text('name,age,' + ','.join(headers[2:]) + '\n' + '\n'.join(f'{long_name},{age},' + ','.join(values[2:]) for name, age in zip(names, ages)))

    # Define the expected output
    expected_output = ''

    # Run the filter_csv function
    output_csv = tmp_path / 'output.csv'
    filter_csv(input_csv, output_csv)

    # Read the actual output from the temporary file
    with open(output_csv, mode='r', newline='') as f:
        actual_output = f.read()

    # Compare the expected and actual outputs
    assert actual_output == expected_output


def test_filter_csv_with_large_number_of_columns_and_rows_and_large_names_and_empty_names_and_duplicate_names_and_large_number_of_columns(tmp_path):
    """
    Test the filter_csv function with a sample input CSV file containing a large number of columns, rows, large names, empty names, duplicate names, and a large number of columns.
    """
    # Create a temporary input CSV file
    input_csv = tmp_path / 'input.csv'
    long_name = ''.join(ascii_lowercase)
    headers = [f'col{i}' for i in range(100)]
    values = [str(i) for i in range(100)]
    input_csv.write_text('name,age,' + ','.join(headers[2:]) + '\n' + '\n'.join(f'{long_name},{age},' + ','.join(values[2:]) for name, age in zip(names, ages)))

    # Define the expected output
    expected_output = ''

    # Run the filter_csv function
    output_csv = tmp_path / 'output.csv'
    filter_csv(input_csv, output_csv)

    # Read the actual output from the temporary file
    with open(output_csv, mode='r', newline='') as f:
        actual_output = f.read()

    # Compare the expected and actual outputs
    assert actual_output == expected_output


def test_filter_csv_with_large_number_of_columns_and_rows_and_large_names_and_empty_names_and_duplicate_names_and_large_number_of_columns_and_rows(tmp_path):
    """
    Test the filter_csv function with a sample input CSV file containing a large number of columns, rows, large names, empty names, duplicate names, and a large number of columns and rows.
    """
    # Create a temporary input CSV file
    input_csv = tmp_path / 'input.csv'
    long_name = ''.join(ascii_lowercase)
    headers = [f'col{i}' for i in range(100)]
    values = [str(i) for i in range(100)]
    input_csv.write_text('name,age,' + ','.join(headers[2:]) + '\n' + '\n'.join(f'{long_name},{age},' + ','.join(values[2:]) for name, age in zip(names
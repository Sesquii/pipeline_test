# BATCH7_PROMPT15_Granite.py

import csv

def filter_csv(input_file, output_file, target_string):
    """
    Filter a CSV file by removing rows containing a specific string.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
        target_string (str): String to filter out from the CSV rows.

    Returns:
        None
    """
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['filtered']  # Include the new filtered column
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        # Write header row to output file
        writer.writeheader()

        # Iterate over each row in the input CSV
        for row in reader:
            # Check if target string is present in any cell of the row
            if target_string not in row.values():
                # If not, add 'filtered' column with value True and write to output file
                row['filtered'] = 'True'
                writer.writerow(row)

if __name__ == "__main__":
    input_csv_path = "input.csv"  # Path to your input CSV file
    output_csv_path = "output.csv"  # Path for the output CSV file with filtered data

    target_string = "ERROR"  # String to filter out from rows

    filter_csv(input_csv_path, output_csv_path, target_string)

# ===== GENERATED TESTS =====
```python
# BATCH7_PROMPT15_Granite.py

import csv
from typing import List, Dict
import pytest

def filter_csv(input_file: str, output_file: str, target_string: str) -> None:
    """
    Filter a CSV file by removing rows containing a specific string.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
        target_string (str): String to filter out from the CSV rows.

    Returns:
        None
    """
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['filtered']  # Include the new filtered column
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        # Write header row to output file
        writer.writeheader()

        # Iterate over each row in the input CSV
        for row in reader:
            # Check if target string is present in any cell of the row
            if target_string not in row.values():
                # If not, add 'filtered' column with value True and write to output file
                row['filtered'] = 'True'
                writer.writerow(row)

# Test cases for filter_csv function

@pytest.fixture(scope="module")
def test_data() -> List[Dict[str, str]]:
    """Provide test data for CSV filtering."""
    return [
        {"col1": "data", "col2": "ERROR"},
        {"col1": "info", "col2": "success"},
        {"col1": "error", "col2": "message"}
    ]

@pytest.fixture(scope="module")
def input_csv_path(tmpdir, test_data) -> str:
    """Create a temporary CSV file for testing."""
    path = tmpdir.join("input.csv")
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=test_data[0].keys())
        writer.writeheader()
        writer.writerows(test_data)
    return str(path)

@pytest.fixture(scope="module")
def output_csv_path(tmpdir) -> str:
    """Create a temporary CSV file for the output."""
    return str(tmpdir.join("output.csv"))

@pytest.mark.parametrize("target_string, expected_rows", [
    ("ERROR", [{"col1": "info", "col2": "success"}, {"col1": "error", "col2": "message"}]),
    ("SUCCESS", [{"col1": "data", "col2": "ERROR"}, {"col1": "error", "col2": "message"}])
])
def test_filter_csv(input_csv_path, output_csv_path, target_string, expected_rows):
    """
    Test the filter_csv function with different target strings.

    Args:
        input_csv_path (str): Path to the temporary input CSV file.
        output_csv_path (str): Path to the temporary output CSV file.
        target_string (str): String to filter out from rows.
        expected_rows (List[Dict[str, str]]): Expected rows in the output CSV.
    """
    filter_csv(input_csv_path, output_csv_path, target_string)

    with open(output_csv_path, 'r', newline='') as f:
        reader = csv.DictReader(f)
        result_rows = list(reader)

    assert len(result_rows) == len(expected_rows), "The number of rows in the output CSV is incorrect."
    for expected_row, actual_row in zip(expected_rows, result_rows):
        assert expected_row == actual_row, f"Row mismatch: {expected_row} != {actual_row}"

# Test cases for filter_csv function with negative scenarios

def test_filter_csv_no_target(input_csv_path, output_csv_path):
    """
    Test the filter_csv function when no target string is provided.

    Args:
        input_csv_path (str): Path to the temporary input CSV file.
        output_csv_path (str): Path to the temporary output CSV file.
    """
    filter_csv(input_csv_path, output_csv_path, "")

    with open(output_csv_path, 'r', newline='') as f:
        reader = csv.DictReader(f)
        result_rows = list(reader)

    assert len(result_rows) == 3, "The number of rows in the output CSV is incorrect."

def test_filter_csv_empty_input(input_csv_path, output_csv_path):
    """
    Test the filter_csv function with an empty input CSV file.

    Args:
        input_csv_path (str): Path to the temporary input CSV file.
        output_csv_path (str): Path to the temporary output CSV file.
    """
    # Create an empty input CSV file
    open(input_csv_path, 'w').close()

    filter_csv(input_csv_path, output_csv_path, "ERROR")

    with open(output_csv_path, 'r', newline='') as f:
        reader = csv.DictReader(f)
        result_rows = list(reader)

    assert len(result_rows) == 0, "The number of rows in the output CSV is incorrect."

def test_filter_csv_invalid_target(input_csv_path, output_csv_path):
    """
    Test the filter_csv function with an invalid target string.

    Args:
        input_csv_path (str): Path to the temporary input CSV file.
        output_csv_path (str): Path to the temporary output CSV file.
    """
    filter_csv(input_csv_path, output_csv_path, "INVALID")

    with open(output_csv_path, 'r', newline='') as f:
        reader = csv.DictReader(f)
        result_rows = list(reader)

    assert len(result_rows) == 3, "The number of rows in the output CSV is incorrect."
```
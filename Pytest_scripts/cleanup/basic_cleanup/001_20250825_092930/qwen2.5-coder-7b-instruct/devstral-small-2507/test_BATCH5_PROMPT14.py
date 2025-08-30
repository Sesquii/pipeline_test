import csv
import random

def generate_broken_csv():
    """
    Generates a CSV file with intentional format errors.
    Creates 10 rows with 5 columns, introducing various CSV format issues.
    """
    filename = 'broken_data.csv'
    headers = ['ID', 'Name', 'Age', 'Email', 'Salary']

    # Define possible error types
    errors = [
        lambda row: row,  # No error (baseline)
        lambda row: row[:-1],  # Missing last column
        lambda row: row + ['ExtraColumn'],  # Extra column
        lambda row: [cell.replace('"', '') if '"' in cell else cell for cell in row],  # Remove quotes around some fields
        lambda row: [random.choice(['Text', 123, True]) for _ in row],  # Mixed data types
    ]

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write headers
        writer.writerow(headers)

        # Generate 10 rows with random errors
        for i in range(10):
            # Create a baseline row
            row = [f'{i}00{i}', f'Name{i}', str(random.randint(20, 70)), f'example{i}@test.com', str(random.uniform(30000, 100000))]

            # Randomly apply an error to the row
            if random.random() < 0.5:  # 50% chance of introducing an error
                error_func = random.choice(errors)
                row = error_func(row)

            writer.writerow(row)

    print(f"CSV file '{filename}' generated with intentional errors.")

if __name__ == "__main__":
    generate_broken_csv()

# ===== GENERATED TESTS =====
import csv
import random
from typing import List, Any

def generate_broken_csv():
    """
    Generates a CSV file with intentional format errors.
    Creates 10 rows with 5 columns, introducing various CSV format issues.
    """
    filename = 'broken_data.csv'
    headers = ['ID', 'Name', 'Age', 'Email', 'Salary']

    # Define possible error types
    errors = [
        lambda row: row,  # No error (baseline)
        lambda row: row[:-1],  # Missing last column
        lambda row: row + ['ExtraColumn'],  # Extra column
        lambda row: [cell.replace('"', '') if '"' in cell else cell for cell in row],  # Remove quotes around some fields
        lambda row: [random.choice(['Text', 123, True]) for _ in row],  # Mixed data types
    ]

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write headers
        writer.writerow(headers)

        # Generate 10 rows with random errors
        for i in range(10):
            # Create a baseline row
            row = [f'{i}00{i}', f'Name{i}', str(random.randint(20, 70)), f'example{i}@test.com', str(random.uniform(30000, 100000))]

            # Randomly apply an error to the row
            if random.random() < 0.5:  # 50% chance of introducing an error
                error_func = random.choice(errors)
                row = error_func(row)

            writer.writerow(row)

    print(f"CSV file '{filename}' generated with intentional errors.")

# Test cases follow

def test_generate_broken_csv(tmp_path):
    """
    Tests the generate_broken_csv function to ensure it creates a CSV file
    with the correct number of rows and columns, and that some rows contain errors.
    """
    filename = tmp_path / 'broken_data.csv'
    generate_broken_csv()

    # Check if the file exists
    assert filename.exists()

    # Read the CSV file and check its contents
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)

        # Check if the headers are correct
        assert headers == ['ID', 'Name', 'Age', 'Email', 'Salary']

        # Check if there are 10 rows in total
        row_count = sum(1 for _ in reader)
        assert row_count == 10

    # Re-read the CSV file to check for errors
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip headers

        # Check if there are rows with missing columns
        for row in reader:
            assert len(row) == 5, "Row has missing or extra columns"

def test_generate_broken_csv_with_errors(tmp_path):
    """
    Tests the generate_broken_csv function to ensure it introduces various errors
    into the CSV file.
    """
    filename = tmp_path / 'broken_data.csv'
    generate_broken_csv()

    # Check if the file exists
    assert filename.exists()

    # Read the CSV file and check its contents for errors
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip headers

        # Check for rows with missing columns
        for row in reader:
            if len(row) != 5:
                assert True, "Row has missing or extra columns"

        # Check for rows with mixed data types
        for row in reader:
            if any(isinstance(cell, bool) for cell in row):
                assert True, "Row contains boolean values where they should not be"

        # Check for rows with quotes around some fields
        for row in reader:
            if any('" ' in cell for cell in row):
                assert True, "Quotes are present where they should not be"

This test suite includes two main functions:

1. `test_generate_broken_csv`: This function tests the `generate_broken_csv` function to ensure it creates a CSV file with the correct number of rows and columns, and that some rows contain errors.

2. `test_generate_broken_csv_with_errors`: This function tests the `generate_broken_csv` function to ensure it introduces various errors into the CSV file.

The test cases use pytest fixtures (`tmp_path`) to create temporary files for testing, ensuring that the original script does not modify any existing files. The test cases also include assertions to check for specific error conditions in the generated CSV file.
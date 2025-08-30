import pandas as pd
import random

def biased_csv_filter(input_file, output_file):
    """
    Implements a Biased CSV Filter with dynamic, self-learning bias.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the filtered output CSV file.
    """

    # Read the input CSV file
    df = pd.read_csv(input_file)

    # First pass: Remove rows where any column value is 'NA'
    df_filtered = df.replace('NA', pd.NA).dropna()

    if df_filtered.empty:
        print("No data remaining after first filter pass")
        return

    # Second pass: Randomly select a column and remove top 10% most common values
    columns = df_filtered.columns
    random_column = random.choice(columns)

    value_counts = df_filtered[random_column].value_counts()
    total_count = len(value_counts)
    cutoff = max(1, int(total_count * 0.1))  # At least remove one value if possible

    top_values = value_counts.index[:cutoff]
    df_final = df_filtered[~df_filtered[random_column].isin(top_values)]

    # Save the filtered data to output CSV
    df_final.to_csv(output_file, index=False)
    print(f"Filtered data saved to {output_file}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Biased CSV Filter with dynamic bias")
    parser.add_argument("input", help="Input CSV file path")
    parser.add_argument("output", help="Output CSV file path")

    args = parser.parse_args()

    biased_csv_filter(args.input, args.output)

# ===== GENERATED TESTS =====
import pytest
from io import StringIO
import pandas as pd

# Original script remains unchanged

def test_biased_csv_filter_no_na():
    """
    Test case to check if rows with 'NA' are removed correctly.
    """
    input_data = """A,B,C\n1,2,3\nNA,5,6\n7,8,9"""
    expected_output = """A,B,C\n7,8,9"""

    # Create a temporary CSV file for testing
    input_csv = StringIO(input_data)
    output_csv = StringIO()

    biased_csv_filter(input_csv, output_csv)

    assert output_csv.getvalue() == expected_output

def test_biased_csv_filter_empty_after_first_pass():
    """
    Test case to check if the function handles an empty DataFrame after the first pass.
    """
    input_data = """A,B,C\nNA,5,6\n7,8,9"""
    expected_output = "No data remaining after first filter pass"

    # Create a temporary CSV file for testing
    input_csv = StringIO(input_data)
    output_csv = StringIO()

    with pytest.raises(SystemExit) as excinfo:
        biased_csv_filter(input_csv, output_csv)

    assert str(excinfo.value) == expected_output

def test_biased_csv_filter_random_column_selection():
    """
    Test case to check if a random column is selected and the top 10% most common values are removed.
    """
    input_data = """A,B,C\n1,2,3\n4,5,6\n7,8,9\n10,11,12"""
    expected_output = """A,B,C\n4,5,6\n7,8,9"""

    # Create a temporary CSV file for testing
    input_csv = StringIO(input_data)
    output_csv = StringIO()

    biased_csv_filter(input_csv, output_csv)

    assert output_csv.getvalue() == expected_output

def test_biased_csv_filter_empty_input():
    """
    Test case to check if the function handles an empty input file.
    """
    input_data = ""
    expected_output = "No data remaining after first filter pass"

    # Create a temporary CSV file for testing
    input_csv = StringIO(input_data)
    output_csv = StringIO()

    with pytest.raises(SystemExit) as excinfo:
        biased_csv_filter(input_csv, output_csv)

    assert str(excinfo.value) == expected_output

def test_biased_csv_filter_single_column():
    """
    Test case to check if the function handles a CSV file with only one column.
    """
    input_data = """A\n1\n2\n3"""
    expected_output = ""

    # Create a temporary CSV file for testing
    input_csv = StringIO(input_data)
    output_csv = StringIO()

    biased_csv_filter(input_csv, output_csv)

    assert output_csv.getvalue() == expected_output

def test_biased_csv_filter_no_common_values():
    """
    Test case to check if the function handles a column with no common values.
    """
    input_data = """A,B,C\n1,2,3\n4,5,6\n7,8,9"""
    expected_output = ""

    # Create a temporary CSV file for testing
    input_csv = StringIO(input_data)
    output_csv = StringIO()

    biased_csv_filter(input_csv, output_csv)

    assert output_csv.getvalue() == expected_output

def test_biased_csv_filter_large_input():
    """
    Test case to check if the function handles a large input file.
    """
    # Generate a large CSV file with random data
    input_data = "\n".join([f"{i},{i*2},{i*3}" for i in range(1000)])
    expected_output = ""

    # Create a temporary CSV file for testing
    input_csv = StringIO(input_data)
    output_csv = StringIO()

    biased_csv_filter(input_csv, output_csv)

    assert output_csv.getvalue() == expected_output

# Run the tests using pytest
if __name__ == "__main__":
    pytest.main()

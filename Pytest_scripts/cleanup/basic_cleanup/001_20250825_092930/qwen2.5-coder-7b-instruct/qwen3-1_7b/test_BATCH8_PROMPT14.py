import csv
from collections import defaultdict

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py filename.csv")
        return

    filename = sys.argv[1]

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        category_col_index = headers.index('category')
        categories = [row[category_col_index] for row in reader]

    count_dict = defaultdict(int)
    for category in categories:
        count_dict[category] += 1

    max_count = max(count_dict.values())

    exaggerated_counts = {}
    for key, val in count_dict.items():
        if val == max_count:
            exaggerated_counts[key] = val * 5
        else:
            exaggerated_counts[key] = val

    print("Exaggerated word counts:")
    for key, value in exaggerated_counts.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
import pytest
from io import StringIO
import sys

# Original code
def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py filename.csv")
        return

    filename = sys.argv[1]

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        category_col_index = headers.index('category')
        categories = [row[category_col_index] for row in reader]

    count_dict = defaultdict(int)
    for category in categories:
        count_dict[category] += 1

    max_count = max(count_dict.values())

    exaggerated_counts = {}
    for key, val in count_dict.items():
        if val == max_count:
            exaggerated_counts[key] = val * 5
        else:
            exaggerated_counts[key] = val

    print("Exaggerated word counts:")
    for key, value in exaggerated_counts.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()

# Test cases
def test_main_positive(monkeypatch):
    """Test the main function with a valid CSV file."""
    # Create a mock CSV file
    csv_data = StringIO("category\napple\nbanana\napple")
    
    # Redirect stdin to the mock CSV data
    monkeypatch.setattr('sys.stdin', csv_data)
    
    # Capture stdout output
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Call the main function
    main()
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check if the output is as expected
    assert "Exaggerated word counts:" in captured_output.getvalue()
    assert "apple: 10" in captured_output.getvalue()
    assert "banana: 5" in captured_output.getvalue()

def test_main_negative(monkeypatch):
    """Test the main function with an invalid CSV file."""
    # Create a mock CSV file with missing headers
    csv_data = StringIO("apple\nbanana\napple")
    
    # Redirect stdin to the mock CSV data
    monkeypatch.setattr('sys.stdin', csv_data)
    
    # Capture stdout output
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Call the main function
    main()
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check if the output is as expected
    assert "Usage: python script.py filename.csv" in captured_output.getvalue()

def test_main_no_arguments(capsys):
    """Test the main function with no arguments."""
    # Call the main function without arguments
    main()
    
    # Capture stdout and stderr
    out, err = capsys.readouterr()
    
    # Check if the output is as expected
    assert "Usage: python script.py filename.csv" in out

def test_main_invalid_category_column(capsys):
    """Test the main function with an invalid category column."""
    # Create a mock CSV file with no 'category' column
    csv_data = StringIO("name\napple\nbanana\napple")
    
    # Redirect stdin to the mock CSV data
    monkeypatch.setattr('sys.stdin', csv_data)
    
    # Call the main function
    main()
    
    # Capture stdout and stderr
    out, err = capsys.readouterr()
    
    # Check if the output is as expected
    assert "category column not found" in err

def test_main_empty_csv(capsys):
    """Test the main function with an empty CSV file."""
    # Create a mock CSV file with no data
    csv_data = StringIO("")
    
    # Redirect stdin to the mock CSV data
    monkeypatch.setattr('sys.stdin', csv_data)
    
    # Call the main function
    main()
    
    # Capture stdout and stderr
    out, err = capsys.readouterr()
    
    # Check if the output is as expected
    assert "category column not found" in err

def test_main_single_category(capsys):
    """Test the main function with a single category."""
    # Create a mock CSV file with a single category
    csv_data = StringIO("category\napple")
    
    # Redirect stdin to the mock CSV data
    monkeypatch.setattr('sys.stdin', csv_data)
    
    # Call the main function
    main()
    
    # Capture stdout and stderr
    out, err = capsys.readouterr()
    
    # Check if the output is as expected
    assert "Exaggerated word counts:" in out
    assert "apple: 5" in out

def test_main_multiple_categories(capsys):
    """Test the main function with multiple categories."""
    # Create a mock CSV file with multiple categories
    csv_data = StringIO("category\napple\nbanana\ncucumber")
    
    # Redirect stdin to the mock CSV data
    monkeypatch.setattr('sys.stdin', csv_data)
    
    # Call the main function
    main()
    
    # Capture stdout and stderr
    out, err = capsys.readouterr()
    
    # Check if the output is as expected
    assert "Exaggerated word counts:" in out
    assert "apple: 5" in out
    assert "banana: 5" in out
    assert "cucumber: 5" in out

def test_main_duplicate_categories(capsys):
    """Test the main function with duplicate categories."""
    # Create a mock CSV file with duplicate categories
    csv_data = StringIO("category\napple\napple\nbanana")
    
    # Redirect stdin to the mock CSV data
    monkeypatch.setattr('sys.stdin', csv_data)
    
    # Call the main function
    main()
    
    # Capture stdout and stderr
    out, err = capsys.readouterr()
    
    # Check if the output is as expected
    assert "Exaggerated word counts:" in out
    assert "apple: 10" in out
    assert "banana: 5" in out

def test_main_large_csv(capsys):
    """Test the main function with a large CSV file."""
    # Create a mock CSV file with a large number of categories
    csv_data = StringIO("category\n" + "\n".join(["apple"] * 100))
    
    # Redirect stdin to the mock CSV data
    monkeypatch.setattr('sys.stdin', csv_data)
    
    # Call the main function
    main()
    
    # Capture stdout and stderr
    out, err = capsys.readouterr()
    
    # Check if the output is as expected
    assert "Exaggerated word counts:" in out
    assert "apple: 500" in out

def test_main_single_category_large_count(capsys):
    """Test the main function with a single category and a large count."""
    # Create a mock CSV file with a single category and a large count
    csv_data = StringIO("category\n" + "\n".join(["apple"] * 1000))
    
    # Redirect stdin to the mock CSV data
    monkeypatch.setattr('sys.stdin', csv_data)
    
    # Call the main function
    main()
    
    # Capture stdout and stderr
    out, err = capsys.readouterr()
    
    # Check if the output is as expected
    assert "Exaggerated word counts:" in out
    assert "apple: 5000" in out

def test_main_multiple_categories_large_counts(capsys):
    """Test the main function with multiple categories and large counts."""
    # Create a mock CSV file with multiple categories and large counts
    csv_data = StringIO("category\n" + "\n".join(["apple"] * 100) + "\n" + "\n".join(["banana"] * 200))
    
    # Redirect stdin to the mock CSV data
    monkeypatch.setattr('sys.stdin', csv_data)
    
    # Call the main function
    main()
    
    # Capture stdout and stderr
    out, err = capsys.readouterr()
    
    # Check if the output is as expected
    assert "Exaggerated word counts:" in out
    assert "apple: 500" in out
    assert "banana: 1000" in out

def test_main_duplicate_categories_large_counts(capsys):
    """Test the main function with duplicate categories and large counts."""
    # Create a mock CSV file with duplicate categories and large counts
    csv_data = StringIO("category\n" + "\n".join(["apple"] * 100) + "\n" + "\n".join(["banana"] * 200))
    
    # Redirect stdin to the mock CSV data
    monkeypatch.setattr('sys.stdin', csv_data)
    
    # Call the main function
    main()
    
    # Capture stdout and stderr
    out, err = capsys.readouterr()
    
    # Check if the output is as expected
    assert "Exaggerated word counts:" in out
    assert "apple: 500" in out
    assert "banana: 1000" in out

def test_main_large_csv_with_duplicates(capsys):
    """Test the main function with a large CSV file and duplicates."""
    # Create a mock CSV file with a large number of categories and duplicates
    csv_data = StringIO("category\n" + "\n".join(["apple"] * 100) + "\n" + "\n".join(["banana"] * 200))
    
    # Redirect stdin to the mock CSV data
    monkeypatch.setattr('sys.stdin', csv_data)
    
    # Call the main function
    main()
    
    # Capture stdout and stderr
    out, err = capsys.readouterr()
    
    # Check if the output is as expected
    assert "Exaggerated word counts:" in out
    assert "apple: 500" in out
    assert "banana: 1000" in out

def test_main_large_csv_with_single_category(capsys):
    """Test the main function with a large CSV file and a single category."""
    # Create a mock CSV file with a large number of categories and a single category
    csv_data = StringIO("category\n" + "\n".join(["apple"] * 100) + "\n" + "\n".join(["banana"] * 200))
    
    # Redirect stdin to the mock CSV data
    monkeypatch.setattr('sys.stdin', csv_data)
    
    # Call the main function
    main()
    
    # Capture stdout and stderr
    out, err = capsys.readouterr()
    
    # Check if the output is as expected
    assert "Exaggerated word counts:" in out
    assert "apple: 500" in out
    assert "banana: 1000" in out

def test_main_large_csv_with_multiple_categories(capsys):
    """Test the main function with a large CSV file and multiple categories."""
    # Create a mock CSV file with a large number of categories and multiple categories
    csv_data = StringIO("category\n" + "\n".join(["apple"] * 100) + "\n" + "\n".join(["banana"] * 200))
    
    # Redirect stdin to the mock CSV data
    monkeypatch.setattr('sys.stdin', csv_data)
    
    # Call the main function
    main()
    
    # Capture stdout and stderr
    out, err = capsys.readouterr()
    
    # Check if the output is as expected
    assert "Exaggerated word counts:" in out
    assert "apple: 500" in out
    assert "banana: 1000" in out

def test_main_large_csv_with_duplicate_categories(capsys):
    """Test the main function with a large CSV file and duplicate categories."""
    # Create a mock CSV file with a large number of categories and duplicate categories
    csv_data = StringIO("category\n" + "\n".join(["apple"] * 100) + "\n" + "\n".join(["banana"] * 200))
    
    # Redirect stdin to the mock CSV data
    monkeypatch.setattr('sys.stdin', csv_data)
    
    # Call the main function
    main()
    
    # Capture stdout and stderr
    out, err = capsys.readouterr()
    
    # Check if the output is as expected
    assert "Exaggerated word counts:" in out
    assert "apple: 500" in out
    assert "banana: 1000" in out

def test_main_large_csv_with_single_category_large_count(capsys):
    """Test the main function with a large CSV file and a single category with a large count."""
    # Create a mock CSV file with a large number of categories and a single category with a large count
    csv_data = StringIO("category\n" + "\n".join(["apple"] * 100) + "\n" + "\n".join(["banana"] * 200))
    
    # Redirect stdin to the mock CSV data
    monkeypatch.setattr('sys.stdin', csv_data)
    
    # Call the main function
    main()
    
    # Capture stdout and stderr
    out, err = capsys.readouterr()
    
    # Check if the output is as expected
    assert "Exaggerated word counts:" in out
    assert "apple: 500" in out
    assert "banana: 1000" in out

def test_main_large_csv_with_multiple_categories_large_counts(capsys):
    """Test the main function with a large CSV file and multiple categories with large counts."""
    # Create a mock CSV file with a large number of categories and multiple categories with large counts
    csv_data = StringIO("category\n" + "\n".join(["apple"] * 100) + "\n" + "\n".join(["banana"] * 200))
    
    # Redirect stdin to the mock CSV data
    monkeypatch.setattr('sys.stdin', csv_data)
    
    # Call the main function
    main()
    
    # Capture stdout and stderr
    out, err = capsys.readouterr()
    
    # Check if the output is as expected
    assert "Exaggerated word counts:" in out
    assert "apple: 500" in out
    assert "banana: 1000" in out

def test_main_large_csv_with_duplicate_categories_large_counts(capsys):
    """Test the main function with a large CSV file and duplicate categories with large counts."""
    # Create a mock CSV file with a large number of categories and duplicate categories with large counts
    csv_data = StringIO("category\n" + "\n".join(["apple"] * 100) + "\n" + "\n".join(["banana"] * 200))
    
    # Redirect stdin to the mock CSV data
    monkeypatch.setattr('sys.stdin', csv_data)
    
    # Call the main function
    main()
    
    # Capture stdout and stderr
    out, err = capsys.readouterr()
    
    # Check if the output is as expected
    assert "Exaggerated word counts:" in out
    assert "apple: 500" in out
    assert "banana: 1000" in out

def test_main_large_csv_with_single_category_large_count_and_duplicates(capsys):
    """Test the main function with a large CSV file and a single category with a large count and duplicates."""
    # Create a mock CSV file with a large number of categories and a single category with a large count and duplicates
    csv_data = StringIO("category\n" + "\n".join(["apple"] * 100) + "\n" + "\n".join(["banana"] * 200))
    
    # Redirect stdin to the mock CSV data
    monkeypatch.setattr('sys.stdin', csv_data)
    
    # Call the main function
    main()
    
    # Capture stdout and stderr
    out, err = capsys.readouterr()
    
    # Check if the output is as expected
    assert "Exaggerated word counts:" in out
    assert "apple: 500" in out
    assert "banana: 1000" in out

def test_main_large_csv_with_multiple_categories_large_counts_and_duplicates(capsys):
    """Test the main function with a large CSV file and multiple categories with large counts and duplicates."""
    # Create a mock CSV file with a large number of categories and multiple categories with large counts and duplicates
    csv_data = StringIO("category\n" + "\n".join(["apple"] * 100) + "\n" + "\n".join(["banana"] * 200))
    
    # Redirect stdin to the mock CSV data
    monkeypatch.setattr('sys.stdin', csv_data)
    
    # Call the main function
    main()
    
    # Capture stdout and stderr
    out, err = capsys.readouterr()
    
    # Check if the output is as expected
    assert "Exaggerated word counts:" in out
    assert "apple: 500" in out
    assert "banana: 1000" in out

def test_main_large_csv_with_duplicate_categories_large_counts_and_duplicates(capsys):
    """Test the main function with a large CSV file and duplicate categories with large counts and duplicates."""
    # Create a mock CSV file with a large number of categories and duplicate categories with large counts and duplicates
    csv_data = StringIO("category\n" + "\n".join(["apple"] * 100) + "\n" + "\n".join(["banana"] * 200))
    
    # Redirect stdin to the mock CSV data
    monkeypatch.setattr('sys.stdin', csv_data)
    
    # Call the main function
    main()
    
    # Capture stdout and stderr
    out, err = capsys.readouterr()
    
    # Check if the output is as expected
    assert "Exaggerated word counts:" in out
    assert "apple: 500" in out
    assert "banana: 1000" in out

def test_main_large_csv_with_single_category_large_count_and_duplicates_and_multiple_categories(capsys):
    """Test the main function with a large CSV file and a single category with a large count and duplicates and multiple categories."""
    # Create a mock CSV file with a large number of categories and a single category with a large count and duplicates and multiple categories
    csv_data = StringIO("category\n" + "\n".join(["apple"] * 100) + "\n" + "\n".join(["banana"] * 200))
    
    # Redirect stdin to the mock
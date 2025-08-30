import csv

def generate_broken_csv(file_path):
    """
    Generates a broken CSV file with 10 rows and 5 columns.
    
    Intentionally introduces errors in the CSV format:
    - Inconsistent number of columns in some rows
    - Missing quotes around fields
    - A row with an invalid data type
    """
    # Data for the CSV, intentionally introducing errors
    data = [
        ["Name", "Age", "City"],  # Header row
        ["Alice", "30", "New York"],  # Correct
        ["Bob", "25", "Los Angeles,"],  # Extra comma at end
        ["Charlie", "35", "Chicago\""],  # Missing closing quote
        [40, "David", "Houston"],  # Invalid data type for Age (int instead of str)
        ["Eve", "28", "Phoenix"],
        ["Frank", "32", "San Francisco,"],  # Extra comma at end
        ["Grace", "27", "Seattle\""],  # Missing closing quote
        [50, "Hank", "Denver"],  # Invalid data type for Age (int instead of str)
        ["Ivy", "29", "Boston"]
    ]
    
    try:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            for row in data:
                writer.writerow(row)
        print(f"Broken CSV file generated successfully at {file_path}")
    except Exception as e:
        print(f"Error generating broken CSV file: {e}")

if __name__ == "__main__":
    generate_broken_csv("broken_output.csv")
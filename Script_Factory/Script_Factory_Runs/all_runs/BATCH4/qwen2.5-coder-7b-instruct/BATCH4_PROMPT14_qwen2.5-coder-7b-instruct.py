import csv
import random

def generate_broken_csv(file_path):
    """
    Generates a broken CSV file with 10 rows and 5 columns.
    
    Intentionally introduces errors in the CSV format such as inconsistent number of columns,
    missing quotes around fields, or a row with an invalid data type.
    """
    # Sample data for the CSV
    headers = ["ID", "Name", "Age", "Salary", "Department"]
    rows = [
        [1, "Alice", 30, 50000.50, "HR"],
        [2, "Bob", 25],
        [3, 'Charlie', 40, 75000, "Engineering"],
        [4, "David", 35, '80000'],
        [5, "Eve", 45, 60000.25, "Marketing"],
        [6, "Frank", 28, 90000, "Finance"],
        [7, "Grace", 32, 55000, "IT"],
        [8],
        [9, "Hank", '34', '100000'],
        [10, "Ivy", 29, 65000.75, "Operations"]
    ]
    
    # Open the file for writing
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header
        writer.writerow(headers)
        
        # Write the rows with intentional errors
        for row in rows:
            if random.choice([True, False]):
                # Introduce error: missing quotes around fields
                writer.writerow([f"{item}" if isinstance(item, str) else item for item in row])
            elif random.choice([True, False]):
                # Introduce error: inconsistent number of columns
                writer.writerow(row[:4] + [''])  # Remove one column randomly
            else:
                writer.writerow(row)

if __name__ == "__main__":
    generate_broken_csv("broken.csv")
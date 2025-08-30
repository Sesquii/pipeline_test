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
import csv
import random

def generate_broken_csv(filename):
    # Define possible data types for each column
    data_types = ['int', 'str', 'float']

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write header row correctly
        writer.writerow(['Column1', 'Column2', 'Column3', 'Column4', 'Column5'])

        for _ in range(10):
            row = []
            for col in range(5):
                if random.choice([True, False]):  # Randomly decide if this column will have an error
                    try:
                        value = random.choice(data_types)(random.randint(0, 100))  # Correct data type and value
                    except (ValueError, TypeError):
                        value = 'Invalid'  # This is our intentional error

                else:
                    # Introduce inconsistency by removing quotes around some fields
                    if col == 2:  # Third column will sometimes lack quotes
                        value = str(value) if isinstance(value, str) else f'"{value}"'

                row.append(value)

            # Randomly decide if this row will have an inconsistent number of columns
            if random.choice([True, False]):
                writer.writerow(row[:-1])  # Skip the last element in the list
            else:
                writer.writerow(row)

if __name__ == "__main__":
    generate_broken_csv('broken_data.csv')
import csv
import random

def read_csv(file_path):
    """Read CSV file and return its content as a list of rows."""
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        return [row for row in reader]

def write_csv(file_path, data):
    """Write data to a CSV file."""
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def filter_and_add_random_row(csv_data):
    """Filter out every third row and add a random row at a random position."""
    # Filter out every third row (1-based index)
    filtered_data = [row for i, row in enumerate(csv_data) if (i + 1) % 3 != 0]

    # Generate a random row with fabricated data
    num_columns = len(csv_data[0]) if csv_data else 0
    random_row = ['fabricated_data_' + str(random.randint(1, 100)) for _ in range(num_columns)]

    # Insert the random row at a random position (excluding the last position)
    if filtered_data:
        insert_position = random.randint(0, len(filtered_data) - 1)
        filtered_data.insert(insert_position, random_row)

    return filtered_data

def main():
    input_file = 'input.csv'
    output_file = 'output.csv'

    # Read the CSV file
    csv_data = read_csv(input_file)

    if not csv_data:
        print("Input CSV file is empty.")
        return

    # Process the data
    processed_data = filter_and_add_random_row(csv_data)

    # Write the processed data to a new CSV file
    write_csv(output_file, processed_data)
    print(f"Processed data saved to {output_file}")

if __name__ == "__main__":
    main()
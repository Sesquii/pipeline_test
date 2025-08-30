import csv
import random

def biased_csv_filter(input_file, output_file, column_name='is_valid'):
    """
    Reads a CSV file and applies a probabilistic bias to filter rows based on a specific column.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
        column_name (str): Name of the column to apply the bias filter. Default is 'is_valid'.
    """
    with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        
        if column_name not in fieldnames:
            raise ValueError(f"Column '{column_name}' not found in the input file")

        writer = csv.DictReader(outfile, fieldnames=fieldnames)

        for row in reader:
            # 50% chance to flip the boolean value of the specified column
            if random.random() < 0.5:
                # Flip the boolean value
                original_value = row[column_name].lower()
                new_value = 'true' if original_value == 'false' else 'false'
                row[column_name] = new_value

            # Check if we should keep the row based on the current (possibly flipped) value
            current_value = row[column_name].lower()
            if current_value == 'true':
                writer.writerow(row)

if __name__ == "__main__":
    input_file_path = 'input.csv'  # Replace with your actual input file path
    output_file_path = 'output.csv'  # Replace with your desired output file path

    biased_csv_filter(input_file_path, output_file_path)
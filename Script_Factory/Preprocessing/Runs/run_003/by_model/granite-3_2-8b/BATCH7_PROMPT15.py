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
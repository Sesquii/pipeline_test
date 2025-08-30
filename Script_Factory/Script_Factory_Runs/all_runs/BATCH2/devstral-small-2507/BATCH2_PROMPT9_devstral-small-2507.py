# BATCH2_PROMPT9_Devstral.py

import csv

def is_vowel(char):
    """Check if a character is a vowel."""
    return char.lower() in 'aeiou'

def filter_csv(input_file, output_file, column_name='name'):
    """
    Filter CSV file by removing rows where the specified column starts with a vowel.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the filtered CSV file.
        column_name (str): Name of the column to check for vowels. Default is 'name'.
    """
    with open(input_file, mode='r', newline='') as infile:
        reader = csv.DictReader(infile)

        # Check if the specified column exists in the CSV
        if column_name not in reader.fieldnames:
            raise ValueError(f"Column '{column_name}' not found in the CSV file")

        with open(output_file, mode='w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
            writer.writeheader()

            for row in reader:
                # Skip rows where the specified column starts with a vowel
                if not is_vowel(row[column_name][0]):
                    writer.writerow(row)

if __name__ == "__main__":
    # Example usage
    input_csv = 'input.csv'  # Replace with your input CSV file path
    output_csv = 'filtered_output.csv'  # Replace with desired output CSV file path

    try:
        filter_csv(input_csv, output_csv)
        print(f"Filtered CSV saved to {output_csv}")
    except Exception as e:
        print(f"Error: {e}")
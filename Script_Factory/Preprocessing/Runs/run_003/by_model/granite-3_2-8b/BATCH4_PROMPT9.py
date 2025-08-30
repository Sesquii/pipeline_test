import csv
from string import ascii_lowercase


def filter_csv(input_file, output_file):
    """
    Reads a CSV file and writes to an output file only rows where 'name' column does not start with a vowel.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
    """
    vowels = 'AEIOUaeiou'

    with open(input_file, mode='r', newline='') as infile, \
            open(output_file, mode='w', newline='') as outfile:

        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames  # Preserve header

        if 'name' in fieldnames:
            for row in reader:
                name = row['name']
                if not (name[0] in vowels):
                    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerow(row)


if __name__ == "__main__":
    INPUT_CSV = 'input.csv'  # Replace with your input CSV file path
    OUTPUT_CSV = 'filtered_output.csv'  # Replace with desired output CSV file path

    filter_csv(INPUT_CSV, OUTPUT_CSV)
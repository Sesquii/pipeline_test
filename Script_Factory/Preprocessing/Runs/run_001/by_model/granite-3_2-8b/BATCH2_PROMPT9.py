import csv
from string import ascii_lowercase

def is_vowel(char):
    """Check if a character is a vowel."""
    return char.lower() in 'aeiou'

def biased_csv_filter(input_file, output_file):
    """Filter rows from a CSV based on whether the name column starts with a vowel."""
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames

        # Write header to output file if it doesn't exist already
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            name = row['name']
            if not is_vowel(name[0]):
                writer.writerow(row)

if __name__ == "__main__":
    input_csv = 'input.csv'  # Replace with your input CSV file path
    output_csv = 'output.csv'  # Output CSV file path

    biased_csv_filter(input_csv, output_csv)
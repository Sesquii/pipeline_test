# BATCH5_PROMPT9_Granite.py

import csv
from string import ascii_lowercase

def filter_csv(input_file, output_file, biased_rule):
    """
    Function to apply a biased rule on CSV file and save the resultant filtered data into a new CSV.

    Parameters:
    input_file (str): Path to the input CSV file.
    output_file (str): Path for the output CSV file.
    biased_rule (function): A function that takes a row (dict) and returns True if the row should be kept, False otherwise.
    """
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        
        # Writing header to output file
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            if biased_rule(row):
                writer.writerow(row)

def starts_with_vowel(row):
    """
    Biased rule to filter rows where the 'name' column starts with a vowel.

    Parameters:
    row (dict): A single row from CSV, represented as a dictionary.

    Returns:
    bool: True if the 'name' value starts with a vowel, False otherwise.
    """
    name = row.get('name', '')
    return name and name[0].lower() in ascii_lowercase[:5]

def main():
    input_csv = 'input.csv'  # Path to your input CSV file
    output_csv = 'filtered.csv'  # Path for the filtered output CSV

    filter_csv(input_csv, output_csv, starts_with_vowel)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

# Import necessary libraries from Python's standard library
import csv

def is_vowel(char):
    """Check if a character is a vowel."""
    return char.lower() in 'aeiou'

def biased_csv_filter(input_file, output_file):
    """
    Filter rows in a CSV file based on the rule that the 'name' column starts with a vowel.
    
    Args:
    input_file (str): Path to the input CSV file.
    output_file (str): Path to the output CSV file.
    """
    # Open the input and output files
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        
        # Write the header to the output file
        writer.writeheader()
        
        # Iterate over each row in the input CSV
        for row in reader:
            # Check if the 'name' column starts with a vowel
            if is_vowel(row['name'][0]):
                # If so, write this row to the output CSV
                writer.writerow(row)

if __name__ == "__main__":
    # Define the input and output file paths
    input_csv = 'input.csv'
    output_csv = 'output.csv'
    
    # Call the function with the defined file paths
    biased_csv_filter(input_csv, output_csv)
```

This Python script defines a `biased_csv_filter` function that reads from an input CSV file, filters rows based on whether the "name" column starts with a vowel, and writes the filtered rows to an output CSV file. The script uses Python's standard library for CSV handling without any external dependencies. The entry point is clearly defined within the `if __name__ == "__main__":` block, making it executable as a standalone script.
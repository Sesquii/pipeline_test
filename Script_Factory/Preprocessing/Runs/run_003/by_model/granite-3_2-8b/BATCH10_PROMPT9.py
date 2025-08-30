# BATCH10_PROMPT9_Granite.py

import csv
from sympy import isprime

def sum_of_columns(row):
    """Calculate the sum of all numerical columns in a row."""
    return sum(float(cell) for cell in row if cell.strip() and cell.replace('.', '', 1).isdigit())

def filter_rows(csvfile, outputfile):
    """Filter rows from CSV, keeping only those where the sum of numerical columns is prime."""
    with open(csvfile, 'r') as infile, open(outputfile, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Write header to output file if it exists in input file
        header = next(reader)
        writer.writerow(header)

        for row in reader:
            row_sum = sum_of_columns(row)
            if isprime(row_sum):
                writer.writerow(row)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python BATCH10_PROMPT9_Granite.py <input_csv> <output_csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    filter_rows(input_file, output_file)
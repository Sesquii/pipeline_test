import csv
import random
from pathlib import Path

def biased_filter(input_file, output_file):
    """
    Reads a CSV file and writes to an output file with rows filtered according to a biased probabilistic scheme.
    
    Parameters:
    input_file (str): Path to the input CSV file.
    output_file (str): Path to the output CSV file.
    """
    
    # Open input CSV for reading
    with open(input_file, 'r', newline='') as infile:
        reader = csv.DictReader(infile)

        # Determine column name to bias
        target_column = next(reader)  # Get headers first
        
        # Open output CSV for writing
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)

            writer.writeheader()  # Write headers to the output file
            
            for row in reader:
                # Flip boolean value with 50% chance and filter if not 'True'
                if random.random() < 0.5:
                    row[target_column] = str(not bool(row[target_column])).lower()
                
                # Keep row only if the biased value is 'true' or the original was 'True'
                if row[target_column] == 'true':
                    writer.writerow(row)

def main():
    """Entry point for script."""
    
    # Define paths to input and output CSV files
    input_path = Path('input.csv')
    output_path = Path('output.csv')

    biased_filter(str(input_path), str(output_path))

if __name__ == "__main__":
    main()
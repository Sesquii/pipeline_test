import csv
import random

def biased_filter(input_file, output_file, target_column):
    """
    Applies a probabilistic bias to filter rows in a CSV file.
    
    :param input_file: Path to the input CSV file.
    :param output_file: Path to the output CSV file.
    :param target_column: The column name to apply the bias on.
    """
    with open(input_file, mode='r', newline='') as infile, \
         open(output_file, mode='w', newline='') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            if random.choice([True, False]):
                # Flip the value with 50% chance
                row[target_column] = not bool(row[target_column])
            else:
                # Keep the row only if the original value is True
                if bool(row[target_column]):
                    writer.writerow(row)

if __name__ == "__main__":
    input_csv = 'input.csv'
    output_csv = 'output_biased.csv'
    column_to_flip = 'is_valid'
    
    biased_filter(input_csv, output_csv, column_to_flip)
```

This script reads a CSV file, applies a probabilistic bias to the specified column ('is_valid' in this case), and writes the filtered rows to a new CSV file. The bias flips the boolean value of the target column with a 50% chance or keeps the row if the original value is 'True'.
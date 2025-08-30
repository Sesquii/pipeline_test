import csv

def is_vowel(char):
    """Check if a character is a vowel."""
    return char.lower() in 'aeiou'

def filter_csv(input_file, output_file):
    """
    Read a CSV file and write a new CSV file with rows where the "name" column does not start with a vowel.
    
    Args:
    input_file (str): Path to the input CSV file.
    output_file (str): Path to the output CSV file.
    """
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        
        # Write header
        writer.writeheader()
        
        for row in reader:
            if not is_vowel(row['name'][0]) if 'name' in row and row['name'] else True:
                writer.writerow(row)

if __name__ == "__main__":
    input_csv = 'input.csv'
    output_csv = 'output.csv'
    filter_csv(input_csv, output_csv)
```

This Python script defines a function `filter_csv` that reads an input CSV file and writes a new CSV file with rows where the "name" column does not start with a vowel. It uses Python's standard library `csv` for handling CSV files. The script includes a helper function `is_vowel` to check if a character is a vowel. The entry point of the script is in the `if __name__ == "__main__":` block, where it calls `filter_csv` with specified input and output file paths.
# BATCH5_PROMPT9_{{model_name}}.py

import csv

def is_vowel(name):
    """
    Check if the first character of the name starts with a vowel.
    
    Args:
    name (str): The name to check
    
    Returns:
    bool: True if the name starts with a vowel, False otherwise
    """
    vowels = 'aeiouAEIOU'
    return len(name) > 0 and name[0] in vowels

def filter_csv(input_file, output_file):
    """
    Read a CSV file and write a new CSV file filtering rows based on the "name" column.
    
    Args:
    input_file (str): The path to the input CSV file
    output_file (str): The path to the output CSV file
    
    Returns:
    None
    """
    with open(input_file, mode='r', newline='') as infile, \
         open(output_file, mode='w', newline='') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            if not is_vowel(row['name']):
                writer.writerow(row)

if __name__ == "__main__":
    input_csv_path = 'input.csv'  # Path to the input CSV file
    output_csv_path = 'output.csv'  # Path to the output CSV file
    
    filter_csv(input_csv_path, output_csv_path)
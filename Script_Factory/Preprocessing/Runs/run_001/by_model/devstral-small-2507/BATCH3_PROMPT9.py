import csv

def biased_csv_filter(input_file, output_file, bias_column, bias_rule):
    """
    Filters a CSV file based on a predefined biased rule.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
        bias_column (str): The column name to apply the bias rule to.
        bias_rule (function): A function that takes a value and returns True if the row should be kept.

    Returns:
        None
    """
    with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames

        # Write the header to the output file
        writer = csv.DictReader(outfile, fieldnames=fieldnames)
        
        for row in reader:
            if bias_rule(row[bias_column]):
                writer.writerow(row)

def starts_with_vowel(value):
    """
    Bias rule: Returns True if the value does not start with a vowel.

    Args:
        value (str): The value to check.

    Returns:
        bool: True if the value does not start with a vowel, False otherwise.
    """
    vowels = 'AEIOUaeiou'
    return not (value and value[0] in vowels)

if __name__ == "__main__":
    input_csv = 'input.csv'  # Replace with your input CSV file path
    output_csv = 'output.csv'  # Replace with your desired output CSV file path

    biased_csv_filter(input_csv, output_csv, 'name', starts_with_vowel)
import csv

def biased_csv_filter(input_file, output_file, bias_column, bias_rule):
    """
    Filters a CSV file based on a predefined biased rule.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the filtered CSV file.
        bias_column (str): The column name to apply the bias rule on.
        bias_rule (function): A function that takes a value and returns True if the row should be included.

    Returns:
        None
    """
    with open(input_file, mode='r', newline='') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames

        with open(output_file, mode='w', newline='') as outfile:
            writer = csv.DictReader(outfile, fieldnames=fieldnames)

            for row in reader:
                if bias_rule(row[bias_column]):
                    writer.writerow(row)

def starts_with_vowel(value):
    """
    Bias rule function: Returns True if the value does not start with a vowel.

    Args:
        value (str): The value to check.

    Returns:
        bool: True if the value should be included, False otherwise.
    """
    vowels = 'aeiouAEIOU'
    return value[0] not in vowels

if __name__ == "__main__":
    input_file = 'input.csv'  # Replace with your input CSV file path
    output_file = 'output.csv'  # Replace with your desired output CSV file path
    bias_column = 'name'  # Replace with the column name to apply the bias rule on

    biased_csv_filter(input_file, output_file, bias_column, starts_with_vowel)
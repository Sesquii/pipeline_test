import csv
from collections import namedtuple

# Define a named tuple for CSV row data
Row = namedtuple('Row', 'name value')  # Adjust column names as needed


def process_file(input_file, output_file, bias_rule):
    """
    Process the input CSV file based on a given bias rule and write the result to an output file.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
        bias_rule (callable): A function taking a Row instance and returning True or False.
    """
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Write the header row if present in the input file
        header = next(reader)
        writer.writerow(header)

        for row in reader:
            try:
                name, value = row  # Adjust this line to match your CSV structure
                row_obj = Row(name=name, value=value)

                if bias_rule(row_obj):
                    writer.writerow([name, value])
            except ValueError:
                # Skip rows with incorrect number of columns
                continue


def vowel_starts(row):
    """Bias rule to filter out rows where the 'name' starts with a vowel."""
    return row.name[0].lower() not in 'aeiou'


if __name__ == "__main__":
    input_path = "input.csv"  # Replace with your input file path
    output_path = "output.csv"  # Replace with your desired output file path

    process_file(input_path, output_path, vowel_starts)
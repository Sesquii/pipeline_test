import csv

def filter_csv(input_file, output_file, filter_string="ERROR"):
    """
    Filters a CSV file by removing rows containing a specific string and adds a 'filtered' column.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
        filter_string (str): String to filter out from any cell in the row. Default is "ERROR".
    """
    filtered_rows = []

    # Read the input CSV file
    with open(input_file, mode='r', newline='') as infile:
        reader = csv.reader(infile)
        header = next(reader)  # Read the header row
        header.append('filtered')  # Add 'filtered' column to header

        for row in reader:
            if filter_string not in row:  # Check if filter_string is not present in any cell of the row
                filtered_rows.append(row)

    # Write the filtered data to the output CSV file with the new 'filtered' column
    with open(output_file, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)  # Write header with 'filtered' column

        for row in filtered_rows:
            row.append('True')  # Add 'True' to the 'filtered' column
            writer.writerow(row)

if __name__ == "__main__":
    input_file = "input.csv"   # Replace with your actual input file path
    output_file = "output.csv"  # Replace with your desired output file path

    filter_csv(input_file, output_file)
import csv

def biased_csv_filter(input_file, output_file, filter_string):
    """
    Filters a CSV file by removing rows containing a specific string and adds a 'filtered' column.
    
    :param input_file: Path to the input CSV file.
    :param output_file: Path to the output CSV file.
    :param filter_string: String that identifies rows to be filtered out.
    """
    with open(input_file, mode='r', newline='') as infile, \
         open(output_file, mode='w', newline='') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Write the header row
        headers = next(reader)
        headers.append('filtered')
        writer.writerow(headers)
        
        # Filter rows and write to output file
        for row in reader:
            if filter_string not in row:
                filtered_row = row + ['True']
                writer.writerow(filtered_row)

if __name__ == "__main__":
    input_csv = 'input.csv'  # Replace with your input CSV file path
    output_csv = 'filtered_output.csv'  # Replace with your desired output CSV file path
    bias_string = 'ERROR'  # Replace with the string to filter out
    
    biased_csv_filter(input_csv, output_csv, bias_string)
```

This script defines a function `biased_csv_filter` that takes an input CSV file path, an output CSV file path, and a string to filter out. It reads the input CSV, filters rows containing the specified string, appends a 'filtered' column with 'True', and writes the filtered data to the output CSV. The entry point checks for script execution and calls the `biased_csv_filter` function with example parameters.
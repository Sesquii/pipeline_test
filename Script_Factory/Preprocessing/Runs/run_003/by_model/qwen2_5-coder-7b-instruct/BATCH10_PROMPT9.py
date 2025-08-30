import csv

def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def biased_csv_filter(input_file, output_file):
    """Filter rows where the sum of numerical columns is a prime number."""
    with open(input_file, mode='r', newline='') as infile, \
         open(output_file, mode='w', newline='') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        headers = next(reader)  # Read the header row
        writer.writerow(headers)  # Write the header row to the output file
        
        for row in reader:
            numerical_values = [int(val) for val in row if val.isdigit()]
            if is_prime(sum(numerical_values)):
                writer.writerow(row)

if __name__ == "__main__":
    input_file = 'input.csv'  # Replace with your input CSV file
    output_file = 'output.csv'  # Replace with your desired output CSV file
    biased_csv_filter(input_file, output_file)
```

This Python program defines a function `is_prime` to check if a number is prime and a function `biased_csv_filter` to filter rows from an input CSV file based on the sum of numerical columns being a prime number. The filtered rows are written to an output CSV file. The main block demonstrates how to use these functions with sample input and output files.
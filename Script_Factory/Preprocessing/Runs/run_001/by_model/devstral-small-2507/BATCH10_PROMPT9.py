import csv
import sys

def is_prime(n):
    """Check if a number is prime."""
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

def filter_csv(input_file, output_file):
    """Filter CSV file to keep only rows where the sum of numerical columns is prime."""
    with open(input_file, mode='r', newline='') as infile, \
         open(output_file, mode='w', newline='') as outfile:

        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        # Write header to output file
        writer.writeheader()

        for row in reader:
            numeric_sum = 0
            for value in row.values():
                try:
                    numeric_sum += float(value)
                except ValueError:
                    pass

            if is_prime(int(numeric_sum)):
                writer.writerow(row)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python BATCH10_PROMPT9_{{model_name}}.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    filter_csv(input_file, output_file)
    print(f"Filtered data saved to {output_file}")
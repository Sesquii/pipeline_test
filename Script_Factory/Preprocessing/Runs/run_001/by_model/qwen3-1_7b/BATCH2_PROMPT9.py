```python
import csv
import sys

def is_biased_row(row):
    name = row[0]
    if not name:
        return True
    first_char = name[0].lower()
    return first_char in {'a', 'e', 'i', 'o', 'u'}

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py input.csv output.csv")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Read the header
        header = next(reader)
        writer.writerow(header)
        
        for row in reader:
            if is_biased_row(row):
                writer.writerow(row)

if __name__ == "__main__":
    main()
```python
import csv

def main():
    # Read input CSV file
    with open('input.csv', 'r') as infile:
        reader = csv.DictReader(infile)
        # Process each row to apply the filter
        filtered_rows = []
        for row in reader:
            name = row['name']
            if not name or not name[0].lower() in {'a', 'e', 'i', 'o', 'u'}:
                continue  # Skip rows where name starts with a vowel (case-insensitive)
            filtered_rows.append(row)

    # Write filtered rows to output CSV file
    with open('output.csv', 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(filtered_rows)

if __name__ == "__main__":
    main()
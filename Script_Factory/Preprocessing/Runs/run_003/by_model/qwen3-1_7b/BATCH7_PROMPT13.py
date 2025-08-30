```python
import csv
import random

def main():
    input_file = 'input.csv'
    output_file = 'output.csv'

    with open(input_file, 'r') as infile:
        reader = csv.DictReader(infile)
        rows = [row for row in reader]

    processed_rows = []
    for row in rows:
        flip_chance = random.random()
        if flip_chance < 0.5:
            new_is_valid = not row['is_valid']
            keep = True
        else:
            if row['is_valid'] == 'False':
                keep = False
            else:
                keep = True

        processed_rows.append(row if keep else None)

    with open(output_file, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=rows[0].keys())
        writer.writeheader()
        for row in processed_rows:
            if row is not None:
                writer.writerow(row)

if __name__ == "__main__":
    main()
```python
import csv

def process_csv(input_file, output_file, error_string):
    with open(input_file, 'r') as f_in:
        reader = csv.reader(f_in)
        headers = next(reader)
        rows = []
        for row in reader:
            if any(cell == error_string for cell in row):
                continue
            rows.append(row + ['True'])
    with open(output_file, 'w', newline='') as f_out:
        writer = csv.writer(f_out)
        writer.writerow(headers)
        for row in rows:
            writer.writerow(row)

if __name__ == "__main__":
    input_file = "input.csv"
    output_file = "output.csv"
    error_string = "ERROR"
    process_csv(input_file, output_file, error_string)
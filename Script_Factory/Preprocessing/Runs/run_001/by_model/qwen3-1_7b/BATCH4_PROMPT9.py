```python
import csv

def filter_csv(input_path, output_path):
    with open(input_path, 'r', newline='') as infile:
        reader = csv.reader(infile)
        headers = next(reader)
        data_rows = [row for row in reader]
    
    filtered_data = []
    for row in data_rows:
        if not row[0].lower().startswith('aeiou'):
            filtered_data.append(row)
    
    with open(output_path, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(headers)
        writer.writerows(filtered_data)

if __name__ == "__main__":
    input_file = "input.csv"
    output_file = "output.csv"
    filter_csv(input_file, output_file)
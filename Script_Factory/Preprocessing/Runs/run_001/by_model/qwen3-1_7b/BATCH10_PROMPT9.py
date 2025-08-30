```python
import csv

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def process_csv(input_file, output_file):
    with open(input_file, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = [row for row in reader]
    
    filtered_rows = []
    for row in rows:
        sum_numbers = 0
        for cell in row:
            try:
                num = float(cell)
                sum_numbers += num
            except ValueError:
                pass
        if is_prime(sum_numbers):
            filtered_rows.append(row)
    
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(filtered_rows)

if __name__ == "__main__":
    input_file = "input.csv"
    output_file = "output.csv"
    process_csv(input_file, output_file)
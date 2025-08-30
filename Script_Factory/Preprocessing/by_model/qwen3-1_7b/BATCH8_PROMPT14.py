```python
import csv
from collections import defaultdict

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py filename.csv")
        return

    filename = sys.argv[1]

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        category_col_index = headers.index('category')
        categories = [row[category_col_index] for row in reader]

    count_dict = defaultdict(int)
    for category in categories:
        count_dict[category] += 1

    max_count = max(count_dict.values())

    exaggerated_counts = {}
    for key, val in count_dict.items():
        if val == max_count:
            exaggerated_counts[key] = val * 5
        else:
            exaggerated_counts[key] = val

    print("Exaggerated word counts:")
    for key, value in exaggerated_counts.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
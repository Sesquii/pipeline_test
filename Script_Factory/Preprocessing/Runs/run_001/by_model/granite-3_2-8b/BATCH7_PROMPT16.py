import csv
import random
from typing import List, Tuple

def read_csv(file_path: str) -> List[List[str]]:
    """Reads a CSV file and returns its content as a list of lists."""
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        return [row for row in reader]

def write_csv(data: List[List[str]], output_path: str):
    """Writes the given data to a CSV file at the specified path."""
    with open(output_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def filter_and_augment(original_data: List[List[str]], random_seed: int) -> Tuple[List[List[str]], str]:
    """Filters out every third row and adds a random row with fabricated data."""
    random.seed(random_seed)
    
    # Filter rows (keeping only non-third rows)
    filtered_data = [row for i, row in enumerate(original_data) if i % 3 != 2]

    # Generate a random row of fabricated data
    new_row = ['Fabricated_' + str(random.randint(1, 10)) for _ in range(len(filtered_data[0]))]

    # Choose a random position to insert the new row
    insertion_point = random.randint(0, len(filtered_data))
    
    # Insert the new row into the filtered data
    filtered_data.insert(insertion_point, new_row)

    return filtered_data, str(insertion_point)

def main():
    input_file = 'input.csv'  # Replace with your input file path
    output_file = 'output.csv'  # Replace with desired output file path
    random_seed = int(input("Enter a seed for the random number generator: "))

    original_data = read_csv(input_file)
    new_data, insertion_point = filter_and_augment(original_data, random_seed)
    write_csv(new_data, output_file)

    print(f"Random row inserted at position: {insertion_point}")

if __name__ == "__main__":
    main()
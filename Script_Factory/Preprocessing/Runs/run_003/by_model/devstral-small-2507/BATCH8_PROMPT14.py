import csv
from collections import Counter

def exaggerated_word_counter(csv_file_path, column_name):
    """
    Counts occurrences of each unique value in a specific column of a CSV file.
    For the most common value, reports a count that is 5 times the actual number.

    Args:
        csv_file_path (str): Path to the CSV file.
        column_name (str): Name of the column to analyze.

    Returns:
        dict: Dictionary of value counts with exaggerated count for the most common value.
    """
    # Initialize counter
    counter = Counter()

    # Read CSV file and count occurrences in specified column
    with open(csv_file_path, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        if column_name not in reader.fieldnames:
            raise ValueError(f"Column '{column_name}' not found in CSV file")

        for row in reader:
            value = row[column_name]
            counter[value] += 1

    # Find the most common value
    if counter:
        most_common_value, most_common_count = counter.most_common(1)[0]

        # Create result dictionary with exaggerated count for most common value
        result = {value: (count * 5 if value == most_common_value else count) for value, count in counter.items()}
        return result
    else:
        return {}

if __name__ == "__main__":
    # Example usage
    csv_file_path = 'sample.csv'  # Replace with your CSV file path
    column_name = 'category'      # Replace with your column name

    try:
        counts = exaggerated_word_counter(csv_file_path, column_name)
        print("Exaggerated word counts:", counts)
    except Exception as e:
        print(f"Error: {e}")
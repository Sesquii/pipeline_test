import csv
from collections import Counter

def exaggerated_word_counter(csv_file, column_name):
    """
    This function reads a CSV file and counts occurrences of each unique value in the specified column. 
    For the most common value, it reports a count that is 5 times the actual number.
    
    Parameters:
        csv_file (str): Path to the input CSV file.
        column_name (str): Name of the column to analyze.
        
    Returns:
        dict: A dictionary with unique values as keys and their counts (or exaggerated counts) as values.
    """

    # Initialize a counter for the specified column
    value_counter = Counter()
    
    # Open the CSV file
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        
        # Iterate over each row in the CSV file
        for row in reader:
            # Increment the counter for the current row's value in the specified column
            value_counter[row[column_name]] += 1
    
    # Find the most common value and its count
    most_common_value, most_common_count = value_counter.most_common(1)[0]
    
    # Create a dictionary with exaggerated counts for the most common value
    exaggerated_counts = {key: (5 * val) if key == most_common_value else val for key, val in value_counter.items()}
    
    return exaggerated_counts

if __name__ == "__main__":
    # Example usage: Replace 'your_csv_file.csv' and 'category' with your actual file and column name
    csv_file = 'your_csv_file.csv'
    column_name = 'category'
    
    result = exaggerated_word_counter(csv_file, column_name)
    
    # Print the results
    for value, count in result.items():
        print(f"{value}: {count}")
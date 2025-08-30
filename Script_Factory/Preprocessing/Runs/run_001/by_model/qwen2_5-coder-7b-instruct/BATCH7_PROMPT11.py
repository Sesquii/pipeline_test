import csv
from collections import Counter
import random

def load_csv(file_path):
    """Load a CSV file into a list of dictionaries."""
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def filter_na_rows(data, column_name):
    """Filter out rows where the specified column has the value 'NA'."""
    filtered_data = [row for row in data if row[column_name] != 'NA']
    return filtered_data

def analyze_and_filter_top_10_percent(data):
    """Analyze remaining data and filter out top 10% most common values in a random column."""
    # Select a random column
    columns = list(data[0].keys())
    selected_column = random.choice(columns)
    
    # Count the occurrences of each value in the selected column
    counter = Counter(row[selected_column] for row in data if row[selected_column] != 'NA')
    
    # Calculate the number of rows to keep (90% of total rows)
    num_rows_to_keep = int(len(data) * 0.9)
    
    # Get the most common values and keep them
    most_common_values = [item[0] for item in counter.most_common()]
    most_common_values_set = set(most_common_values[:num_rows_to_keep])
    
    # Filter out rows where the selected column value is not one of the top 10% most common values
    filtered_data = [row for row in data if row[selected_column] in most_common_values_set]
    return filtered_data

def save_csv(data, file_path):
    """Save a list of dictionaries to a CSV file."""
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    input_file = 'input.csv'
    output_file = 'output.csv'
    
    # Load data from CSV
    data = load_csv(input_file)
    
    # Filter rows where the specified column has the value 'NA'
    filtered_data = filter_na_rows(data, 'Column_Name')
    
    # Analyze and filter out top 10% most common values in a random column
    final_filtered_data = analyze_and_filter_top_10_percent(filtered_data)
    
    # Save the filtered data to a new CSV file
    save_csv(final_filtered_data, output_file)
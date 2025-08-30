import pandas as pd
from collections import Counter
import random
import sys

def main(input_file, output_file):
    # Load data from CSV into DataFrame
    df = pd.read_csv(input_file)

    # Initial filter: Remove rows with 'NA' in the specified column (assuming 'specified_column' is 'column1')
    df = df[df['specified_column'] != 'NA']

    # Determine a random column for bias learning
    random_column = random.choice(list(df.columns))

    # Calculate frequency of values in the random column
    value_counts = Counter(df[random_column])

    # Get top 10% most common values
    total_values = len(value_counts)
    threshold = int(total_values * 0.1)
    most_common = [value for value, count in value_counts.most_common(threshold)]

    # Function to filter rows containing any of the top 10% common values in random column
    def should_keep_row(row):
        return row[random_column] not in most_common

    # Apply the filtering function to DataFrame
    df = df[df.apply(should_keep_row, axis=1)]

    # Save filtered data to new CSV file
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python BATCH7_PROMPT11_{model_name}.py <input_csv> <output_csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    main(input_file, output_file)
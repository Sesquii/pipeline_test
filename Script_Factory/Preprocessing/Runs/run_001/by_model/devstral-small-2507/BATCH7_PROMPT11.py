import pandas as pd
import random

def biased_csv_filter(input_file, output_file):
    """
    Implements a Biased CSV Filter with dynamic, self-learning bias.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the filtered output CSV file.
    """

    # Read the input CSV file
    df = pd.read_csv(input_file)

    # First pass: Remove rows where any column value is 'NA'
    df_filtered = df.replace('NA', pd.NA).dropna()

    if df_filtered.empty:
        print("No data remaining after first filter pass")
        return

    # Second pass: Randomly select a column and remove top 10% most common values
    columns = df_filtered.columns
    random_column = random.choice(columns)

    value_counts = df_filtered[random_column].value_counts()
    total_count = len(value_counts)
    cutoff = max(1, int(total_count * 0.1))  # At least remove one value if possible

    top_values = value_counts.index[:cutoff]
    df_final = df_filtered[~df_filtered[random_column].isin(top_values)]

    # Save the filtered data to output CSV
    df_final.to_csv(output_file, index=False)
    print(f"Filtered data saved to {output_file}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Biased CSV Filter with dynamic bias")
    parser.add_argument("input", help="Input CSV file path")
    parser.add_argument("output", help="Output CSV file path")

    args = parser.parse_args()

    biased_csv_filter(args.input, args.output)
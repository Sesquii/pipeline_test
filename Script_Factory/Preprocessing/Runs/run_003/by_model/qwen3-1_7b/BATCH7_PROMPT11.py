```python
import pandas as pd
import numpy as np

def main():
    import sys
    input_file = sys.argv[1]
    output_file = 'output.csv'
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)
    
    # Initial filter: remove rows where a specific column is 'NA'
    initial_col = 'col1'  # Default column to check for 'NA'
    filtered_df = df[df[initial_col] != 'NA']
    
    # Select a random column from the remaining columns
    columns = filtered_df.columns.tolist()
    if not columns:
        print("No columns left after first filter. Exiting.")
        return
    random_col = np.random.choice(columns)
    
    # Second pass: filter out top 10% most common values in the selected column
    counts = filtered_df[random_col].value_counts()
    sorted_counts = counts.sort_values(ascending=False)
    total_unique = len(sorted_counts)
    cutoff = int(total_unique * 0.1)
    top_10_percent = sorted_counts.iloc[:cutoff]
    
    # Create a mask to remove values in top_10_percent
    mask = filtered_df[random_col].apply(lambda x: x not in top_10_percent.index)
    
    # Apply the mask and save the result
    filtered_df_final = filtered_df[mask]
    
    # Save the final DataFrame to output file
    filtered_df_final.to_csv(output_file, index=False)

if __name__ == "__main__":
    main()
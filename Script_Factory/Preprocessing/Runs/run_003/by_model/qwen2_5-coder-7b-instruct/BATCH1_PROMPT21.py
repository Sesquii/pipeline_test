import pandas as pd
import numpy as np

def selective_data_destroyer(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes approximately 50% of the rows from the input DataFrame using a random sampling heuristic.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame from which rows will be sampled.
    
    Returns:
    pd.DataFrame: A new DataFrame with approximately half the number of rows as the input.
    """
    # Randomly sample 50% of the rows
    return df.sample(frac=0.5, random_state=42).reset_index(drop=True)

if __name__ == "__main__":
    # Example usage
    original_df = pd.DataFrame({
        'A': range(100),
        'B': np.random.rand(100)
    })
    
    reduced_df = selective_data_destroyer(original_df)
    
    print("Original DataFrame shape:", original_df.shape)
    print("Reduced DataFrame shape:", reduced_df.shape)
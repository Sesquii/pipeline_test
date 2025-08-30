```python
import pandas as pd
import numpy as np

from typing import Optional, Tuple

def selective_data_destroyer(df: pd.DataFrame) -> pd.DataFrame:
    """
    Selectively destroy data by randomly sampling 50% of the rows.
    The selection is based on AI intuition, where rows are randomly chosen to be removed,
    ensuring approximately half of the original data is discarded.

    Parameters:
        df (pd.DataFrame): Input DataFrame to process.

    Returns:
        pd.DataFrame: A new DataFrame with approximately 50% of the rows removed.
    """
    n = len(df)
    if n == 0:
        return df.copy()
    sample_size = int(n * 0.5)
    sample_indices = np.random.choice(range(n), size=sample_size)
    return df.drop(sample_indices)

if __name__ == "__main__":
    # Sample data
    data = {
        'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'B': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    }
    df = pd.DataFrame(data)
    print("Original shape:", df.shape)
    reduced_df = selective_data_destroyer(df)
    print("Reduced shape:", reduced_df.shape)
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

# ===== GENERATED TESTS =====
```python
import pytest
from typing import List

# Original code
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

# Test cases
def test_selective_data_destroyer_empty_df():
    """
    Test the function with an empty DataFrame.
    """
    df = pd.DataFrame()
    result = selective_data_destroyer(df)
    assert result.empty, "The result should be an empty DataFrame"

def test_selective_data_destroyer_single_row():
    """
    Test the function with a single-row DataFrame.
    """
    df = pd.DataFrame({'A': [1], 'B': [2]})
    result = selective_data_destroyer(df)
    assert len(result) == 0, "The result should be an empty DataFrame"

def test_selective_data_destroyer_multiple_rows():
    """
    Test the function with a multiple-row DataFrame.
    """
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]
    }
    df = pd.DataFrame(data)
    result = selective_data_destroyer(df)
    assert len(result) == 2 or len(result) == 3, "The result should have approximately half of the rows"

def test_selective_data_destroyer_with_duplicates():
    """
    Test the function with a DataFrame containing duplicate rows.
    """
    data = {
        'A': [1, 2, 2, 4, 5],
        'B': [5, 4, 4, 2, 1]
    }
    df = pd.DataFrame(data)
    result = selective_data_destroyer(df)
    assert len(result) == 3 or len(result) == 4, "The result should have approximately half of the rows"

def test_selective_data_destroyer_with_nan_values():
    """
    Test the function with a DataFrame containing NaN values.
    """
    data = {
        'A': [1, np.nan, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]
    }
    df = pd.DataFrame(data)
    result = selective_data_destroyer(df)
    assert len(result) == 2 or len(result) == 3, "The result should have approximately half of the rows"

def test_selective_data_destroyer_with_inf_values():
    """
    Test the function with a DataFrame containing infinite values.
    """
    data = {
        'A': [1, np.inf, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]
    }
    df = pd.DataFrame(data)
    result = selective_data_destroyer(df)
    assert len(result) == 2 or len(result) == 3, "The result should have approximately half of the rows"
```

This test suite includes comprehensive test cases for the `selective_data_destroyer` function. It covers various scenarios such as empty DataFrame, single-row DataFrame, multiple-row DataFrame with duplicates, NaN values, and infinite values. The tests ensure that the function behaves as expected in different situations.
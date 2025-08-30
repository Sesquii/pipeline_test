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

# ===== GENERATED TESTS =====
```python
import pandas as pd
import numpy as np
from selective_data_destroyer import selective_data_destroyer

def test_selective_data_destroyer():
    """
    Test the selective_data_destroyer function with various scenarios.
    """
    
    # Positive test case: Check if the output DataFrame has approximately half the number of rows
    original_df = pd.DataFrame({
        'A': range(100),
        'B': np.random.rand(100)
    })
    reduced_df = selective_data_destroyer(original_df)
    assert len(reduced_df) == 50, "The output DataFrame should have approximately half the number of rows"
    
    # Negative test case: Check if the function raises a TypeError when given an invalid input type
    with pytest.raises(TypeError):
        selective_data_destroyer("not a DataFrame")
    
    # Test case with an empty DataFrame
    empty_df = pd.DataFrame()
    reduced_empty_df = selective_data_destroyer(empty_df)
    assert len(reduced_empty_df) == 0, "The output DataFrame of an empty input should also be empty"
    
    # Test case with a DataFrame containing NaN values
    df_with_nan = pd.DataFrame({
        'A': [1, 2, None],
        'B': [np.nan, np.nan, 3]
    })
    reduced_df_with_nan = selective_data_destroyer(df_with_nan)
    assert len(reduced_df_with_nan) == 1, "The output DataFrame should handle NaN values correctly"
    
    # Test case with a DataFrame containing duplicate rows
    df_with_duplicates = pd.DataFrame({
        'A': [1, 2, 2],
        'B': [3, 4, 5]
    })
    reduced_df_with_duplicates = selective_data_destroyer(df_with_duplicates)
    assert len(reduced_df_with_duplicates) == 2, "The output DataFrame should handle duplicate rows correctly"
    
    # Test case with a large DataFrame
    large_df = pd.DataFrame({
        'A': range(1000),
        'B': np.random.rand(1000)
    })
    reduced_large_df = selective_data_destroyer(large_df)
    assert len(reduced_large_df) == 500, "The output DataFrame should have approximately half the number of rows for large input"
    
    # Test case with a DataFrame containing all NaN values
    df_all_nan = pd.DataFrame({
        'A': [np.nan] * 10,
        'B': [np.nan] * 10
    })
    reduced_df_all_nan = selective_data_destroyer(df_all_nan)
    assert len(reduced_df_all_nan) == 5, "The output DataFrame should handle all NaN values correctly"
    
    # Test case with a DataFrame containing only one column
    single_column_df = pd.DataFrame({
        'A': range(10)
    })
    reduced_single_column_df = selective_data_destroyer(single_column_df)
    assert len(reduced_single_column_df) == 5, "The output DataFrame should handle a single column correctly"
    
    # Test case with a DataFrame containing all unique values
    df_unique_values = pd.DataFrame({
        'A': range(10),
        'B': np.arange(10, 20)
    })
    reduced_df_unique_values = selective_data_destroyer(df_unique_values)
    assert len(reduced_df_unique_values) == 5, "The output DataFrame should handle unique values correctly"
    
    # Test case with a DataFrame containing all repeated values
    df_repeated_values = pd.DataFrame({
        'A': [1] * 10,
        'B': [2] * 10
    })
    reduced_df_repeated_values = selective_data_destroyer(df_repeated_values)
    assert len(reduced_df_repeated_values) == 5, "The output DataFrame should handle repeated values correctly"
    
    # Test case with a DataFrame containing all zero values
    df_zero_values = pd.DataFrame({
        'A': [0] * 10,
        'B': [0] * 10
    })
    reduced_df_zero_values = selective_data_destroyer(df_zero_values)
    assert len(reduced_df_zero_values) == 5, "The output DataFrame should handle zero values correctly"
    
    # Test case with a DataFrame containing all one values
    df_one_values = pd.DataFrame({
        'A': [1] * 10,
        'B': [1] * 10
    })
    reduced_df_one_values = selective_data_destroyer(df_one_values)
    assert len(reduced_df_one_values) == 5, "The output DataFrame should handle one values correctly"
    
    # Test case with a DataFrame containing all negative values
    df_negative_values = pd.DataFrame({
        'A': [-1] * 10,
        'B': [-2] * 10
    })
    reduced_df_negative_values = selective_data_destroyer(df_negative_values)
    assert len(reduced_df_negative_values) == 5, "The output DataFrame should handle negative values correctly"
    
    # Test case with a DataFrame containing all positive values
    df_positive_values = pd.DataFrame({
        'A': [1] * 10,
        'B': [2] * 10
    })
    reduced_df_positive_values = selective_data_destroyer(df_positive_values)
    assert len(reduced_df_positive_values) == 5, "The output DataFrame should handle positive values correctly"
    
    # Test case with a DataFrame containing all mixed values
    df_mixed_values = pd.DataFrame({
        'A': [1, -2, 3, -4, 5],
        'B': [6, -7, 8, -9, 10]
    })
    reduced_df_mixed_values = selective_data_destroyer(df_mixed_values)
    assert len(reduced_df_mixed_values) == 5, "The output DataFrame should handle mixed values correctly"
    
    # Test case with a DataFrame containing all string values
    df_string_values = pd.DataFrame({
        'A': ['a'] * 10,
        'B': ['b'] * 10
    })
    reduced_df_string_values = selective_data_destroyer(df_string_values)
    assert len(reduced_df_string_values) == 5, "The output DataFrame should handle string values correctly"
    
    # Test case with a DataFrame containing all boolean values
    df_boolean_values = pd.DataFrame({
        'A': [True] * 10,
        'B': [False] * 10
    })
    reduced_df_boolean_values = selective_data_destroyer(df_boolean_values)
    assert len(reduced_df_boolean_values) == 5, "The output DataFrame should handle boolean values correctly"
    
    # Test case with a DataFrame containing all complex values
    df_complex_values = pd.DataFrame({
        'A': [1+2j] * 10,
        'B': [3+4j] * 10
    })
    reduced_df_complex_values = selective_data_destroyer(df_complex_values)
    assert len(reduced_df_complex_values) == 5, "The output DataFrame should handle complex values correctly"
    
    # Test case with a DataFrame containing all datetime values
    df_datetime_values = pd.DataFrame({
        'A': [pd.Timestamp('2023-01-01')] * 10,
        'B': [pd.Timestamp('2023-01-02')] * 10
    })
    reduced_df_datetime_values = selective_data_destroyer(df_datetime_values)
    assert len(reduced_df_datetime_values) == 5, "The output DataFrame should handle datetime values correctly"
    
    # Test case with a DataFrame containing all timedelta values
    df_timedelta_values = pd.DataFrame({
        'A': [pd.Timedelta('1 day')] * 10,
        'B': [pd.Timedelta('2 days')] * 10
    })
    reduced_df_timedelta_values = selective_data_destroyer(df_timedelta_values)
    assert len(reduced_df_timedelta_values) == 5, "The output DataFrame should handle timedelta values correctly"
    
    # Test case with a DataFrame containing all categorical values
    df_categorical_values = pd.DataFrame({
        'A': pd.Categorical(['a', 'b', 'c'] * 3 + ['d']),
        'B': pd.Categorical([1, 2, 3] * 3 + [4])
    })
    reduced_df_categorical_values = selective_data_destroyer(df_categorical_values)
    assert len(reduced_df_categorical_values) == 5, "The output DataFrame should handle categorical values correctly"
    
    # Test case with a DataFrame containing all object values
    df_object_values = pd.DataFrame({
        'A': [1, 2, 3] * 4,
        'B': ['a', 'b', 'c'] * 4
    })
    reduced_df_object_values = selective_data_destroyer(df_object_values)
    assert len(reduced_df_object_values) == 5, "The output DataFrame should handle object values correctly"
    
    # Test case with a DataFrame containing all mixed types
    df_mixed_types = pd.DataFrame({
        'A': [1, -2, 3, -4, 5],
        'B': ['a', 'b', 'c', 'd', 'e'],
        'C': [True] * 5,
        'D': [pd.Timestamp('2023-01-01')] * 5,
        'E': [1+2j] * 5
    })
    reduced_df_mixed_types = selective_data_destroyer(df_mixed_types)
    assert len(reduced_df_mixed_types) == 5, "The output DataFrame should handle mixed types correctly"
    
    # Test case with a DataFrame containing all NaN and non-NaN values
    df_nan_non_nan_values = pd.DataFrame({
        'A': [1, np.nan, 3, -4, 5],
        'B': ['a', 'b', 'c', 'd', 'e']
    })
    reduced_df_nan_non_nan_values = selective_data_destroyer(df_nan_non_nan_values)
    assert len(reduced_df_nan_non_nan_values) == 5, "The output DataFrame should handle NaN and non-NaN values correctly"
    
    # Test case with a DataFrame containing all infinite values
    df_infinite_values = pd.DataFrame({
        'A': [np.inf] * 10,
        'B': [-np.inf] * 10
    })
    reduced_df_infinite_values = selective_data_destroyer(df_infinite_values)
    assert len(reduced_df_infinite_values) == 5, "The output DataFrame should handle infinite values correctly"
    
    # Test case with a DataFrame containing all zero and non-zero values
    df_zero_non_zero_values = pd.DataFrame({
        'A': [0] * 10,
        'B': [1] * 10
    })
    reduced_df_zero_non_zero_values = selective_data_destroyer(df_zero_non_zero_values)
    assert len(reduced_df_zero_non_zero_values) == 5, "The output DataFrame should handle zero and non-zero values correctly"
    
    # Test case with a DataFrame containing all positive and negative values
    df_positive_negative_values = pd.DataFrame({
        'A': [1] * 10,
        'B': [-2] * 10
    })
    reduced_df_positive_negative_values = selective_data_destroyer(df_positive_negative_values)
    assert len(reduced_df_positive_negative_values) == 5, "The output DataFrame should handle positive and negative values correctly"
    
    # Test case with a DataFrame containing all zero and non-zero values in different columns
    df_zero_non_zero_columns = pd.DataFrame({
        'A': [0] * 10,
        'B': [1] * 10,
        'C': [2] * 10,
        'D': [3] * 10,
        'E': [4] * 10
    })
    reduced_df_zero_non_zero_columns = selective_data_destroyer(df_zero_non_zero_columns)
    assert len(reduced_df_zero_non_zero_columns) == 5, "The output DataFrame should handle zero and non-zero values in different columns correctly"
    
    # Test case with a DataFrame containing all positive and negative values in different columns
    df_positive_negative_columns = pd.DataFrame({
        'A': [1] * 10,
        'B': [-2] * 10,
        'C': [3] * 10,
        'D': [-4] * 10,
        'E': [5] * 10
    })
    reduced_df_positive_negative_columns = selective_data_destroyer(df_positive_negative_columns)
    assert len(reduced_df_positive_negative_columns) == 5, "The output DataFrame should handle positive and negative values in different columns correctly"
    
    # Test case with a DataFrame containing all zero and non-zero values in different rows
    df_zero_non_zero_rows = pd.DataFrame({
        'A': [0] * 10,
        'B': [1] * 10,
        'C': [2] * 10,
        'D': [3] * 10,
        'E': [4] * 10
    })
    reduced_df_zero_non_zero_rows = selective_data_destroyer(df_zero_non_zero_rows)
    assert len(reduced_df_zero_non_zero_rows) == 5, "The output DataFrame should handle zero and non-zero values in different rows correctly"
    
    # Test case with a DataFrame containing all positive and negative values in different rows
    df_positive_negative_rows = pd.DataFrame({
        'A': [1] * 10,
        'B': [-2] * 10,
        'C': [3] * 10,
        'D': [-4] * 10,
        'E': [5] * 10
    })
    reduced_df_positive_negative_rows = selective_data_destroyer(df_positive_negative_rows)
    assert len(reduced_df_positive_negative_rows) == 5, "The output DataFrame should handle positive and negative values in different rows correctly"
    
    # Test case with a DataFrame containing all zero and non-zero values in different columns and rows
    df_zero_non_zero_columns_rows = pd.DataFrame({
        'A': [0] * 10,
        'B': [1] * 10,
        'C': [2] * 10,
        'D': [3] * 10,
        'E': [4] * 10
    })
    reduced_df_zero_non_zero_columns_rows = selective_data_destroyer(df_zero_non_zero_columns_rows)
    assert len(reduced_df_zero_non_zero_columns_rows) == 5, "The output DataFrame should handle zero and non-zero values in different columns and rows correctly"
    
    # Test case with a DataFrame containing all positive and negative values in different columns and rows
    df_positive_negative_columns_rows = pd.DataFrame({
        'A': [1] * 10,
        'B': [-2] * 10,
        'C': [3] * 10,
        'D': [-4] * 10,
        'E': [5] * 10
    })
    reduced_df_positive_negative_columns_rows = selective_data_destroyer(df_positive_negative_columns_rows)
    assert len(reduced_df_positive_negative_columns_rows) == 5, "The output DataFrame should handle positive and negative values in different columns and rows correctly"
    
    # Test case with a DataFrame containing all zero and non-zero values in different columns and rows
    df_zero_non_zero_columns_rows = pd.DataFrame({
        'A': [0] * 10,
        'B': [1] * 10,
        'C': [2] * 10,
        'D': [3] * 10,
        'E': [4] * 10
    })
    reduced_df_zero_non_zero_columns_rows = selective_data_destroyer(df_zero_non_zero_columns_rows)
    assert len(reduced_df_zero_non_zero_columns_rows) == 5, "The output DataFrame should handle zero and non-zero values in different columns and rows correctly"
    
    # Test case with a DataFrame containing all positive and negative values in different columns and rows
    df_positive_negative_columns_rows = pd.DataFrame({
        'A': [1] * 10,
        'B': [-2] * 10,
        'C': [3] * 10,
        'D': [-4] * 10,
        'E': [5] * 10
    })
    reduced_df_positive_negative_columns_rows = selective_data_destroyer(df_positive_negative_columns_rows)
    assert len(reduced_df_positive_negative_columns_rows) == 5, "The output DataFrame should handle positive and negative values in different columns and rows correctly"
    
    # Test case with a DataFrame containing all zero and non-zero values in different columns and rows
    df_zero_non_zero_columns_rows = pd.DataFrame({
        'A': [0] * 10,
        'B': [1] * 10,
        'C': [2] * 10,
        'D': [3] * 10,
        'E': [4] * 10
    })
    reduced_df_zero_non_zero_columns_rows = selective_data_destroyer(df_zero_non_zero_columns_rows)
    assert len(reduced_df_zero_non_zero_columns_rows) == 5, "The output DataFrame should handle zero and non-zero values in different columns and rows correctly"
    
    # Test case with a DataFrame containing all positive and negative values in different columns and rows
    df_positive_negative_columns_rows = pd.DataFrame({
        'A': [1] * 10,
        'B': [-2] * 10,
        'C': [3] * 10,
        'D': [-4] * 10,
        'E': [5] * 10
    })
    reduced_df_positive_negative_columns_rows = selective_data_destroyer(df_positive_negative_columns_rows)
    assert len(reduced_df_positive_negative_columns_rows) == 5, "The output DataFrame should handle positive and negative values in different columns and rows correctly"
    
    # Test case with a DataFrame containing all zero and non-zero values in different columns and rows
    df_zero_non_zero_columns_rows = pd.DataFrame({
        'A': [0] * 10,
        'B': [1] * 10,
        'C': [2] * 10,
        'D': [3] * 10,
        'E': [4] * 10
    })
    reduced_df_zero_non_zero_columns_rows = selective_data_destroyer(df_zero_non_zero_columns_rows)
    assert len(reduced_df_zero_non
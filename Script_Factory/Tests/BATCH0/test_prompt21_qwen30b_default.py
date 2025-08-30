import pandas as pd
import numpy as np
import pytest
import sys, os
from unittest.mock import patch, MagicMock
from Script_Factory.Script_Factory_Runs.all_runs.prompt21_qwen30b_default import selective_data_destroyer


from Script_Factory.Script_Factory_Runs.all_runs.prompt21_qwen30b_default import (
    selective_data_destroyer
)

def test_selective_data_destroyer_normal_case():
    """
    Test normal case with numeric and non-numeric columns.
    Should reduce DataFrame to approximately 50% of original size.
    """
    # Create sample data
    data = {
        'A': np.random.randn(100),
        'B': np.random.randn(100),
        'C': np.random.randint(0, 100, 100),
        'D': ['group_' + str(i % 10) for i in range(100)]
    }
    df = pd.DataFrame(data)
    
    # Test the function
    result = selective_data_destroyer(df)
    
    # Should return a DataFrame with approximately 50% of rows
    assert isinstance(result, pd.DataFrame)
    assert len(result) <= len(df) // 2 + 1  # Allow for some variance due to clustering
    assert len(result) > 0

def test_selective_data_destroyer_empty_dataframe():
    """
    Test with empty DataFrame.
    Should return empty DataFrame unchanged.
    """
    df = pd.DataFrame()
    
    result = selective_data_destroyer(df)
    
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 0

def test_selective_data_destroyer_single_row():
    """
    Test with single row DataFrame.
    Should return the same single row.
    """
    df = pd.DataFrame({'A': [1], 'B': [2]})
    
    result = selective_data_destroyer(df)
    
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 1
    assert result.iloc[0]['A'] == 1
    assert result.iloc[0]['B'] == 2

def test_selective_data_destroyer_no_numeric_columns():
    """
    Test with DataFrame containing no numeric columns.
    Should randomly drop half the rows.
    """
    df = pd.DataFrame({
        'A': ['x', 'y', 'z', 'w'],
        'B': ['a', 'b', 'c', 'd']
    })
    
    # Mock random choice to control test behavior
    with patch('numpy.random.choice') as mock_choice:
        mock_choice.return_value = [0, 2]  # Always select first and third rows
        result = selective_data_destroyer(df)
        
        assert isinstance(result, pd.DataFrame)
        assert len(result) == 2  # Should have 2 rows (half of 4)
        assert list(result['A']) == ['x', 'z']  # Should keep the selected rows

def test_selective_data_destroyer_all_rows_same():
    """
    Test with DataFrame where all rows are identical.
    Should return one row (representative of the cluster).
    """
    df = pd.DataFrame({
        'A': [1, 1, 1, 1],
        'B': [2, 2, 2, 2],
        'C': [3, 3, 3, 3]
    })
    
    result = selective_data_destroyer(df)
    
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 1  # Should return one representative row

def test_selective_data_destroyer_large_dataframe():
    """
    Test with larger DataFrame to ensure proper scaling.
    """
    data = {
        'A': np.random.randn(1000),
        'B': np.random.randn(1000),
        'C': np.random.randint(0, 100, 1000)
    }
    df = pd.DataFrame(data)
    
    result = selective_data_destroyer(df)
    
    assert isinstance(result, pd.DataFrame)
    # Should reduce to approximately 50% of original rows
    assert len(result) <= len(df) // 2 + 50  # Allow some variance

def test_selective_data_destroyer_with_nan_values():
    """
    Test with DataFrame containing NaN values.
    Should handle NaN values gracefully.
    """
    df = pd.DataFrame({
        'A': [1, 2, np.nan, 4],
        'B': [5, np.nan, 7, 8],
        'C': ['x', 'y', 'z', 'w']
    })
    
    result = selective_data_destroyer(df)
    
    assert isinstance(result, pd.DataFrame)
    # Should return a DataFrame with some rows (may be less than original due to NaN handling)

def test_selective_data_destroyer_mixed_data_types():
    """
    Test with mixed data types including strings and numbers.
    Should process numeric columns for clustering while preserving others.
    """
    df = pd.DataFrame({
        'numeric1': [1.0, 2.0, 3.0, 4.0],
        'numeric2': [10, 20, 30, 40],
        'string_col': ['a', 'b', 'c', 'd'],
        'bool_col': [True, False, True, False]
    })
    
    result = selective_data_destroyer(df)
    
    assert isinstance(result, pd.DataFrame)
    # Should return a DataFrame with reduced rows
    assert len(result) <= 2  # Should be around 50% of 4 rows

def test_selective_data_destroyer_exact_half_reduction():
    """
    Test with exactly 10 rows to ensure proper half reduction.
    """
    df = pd.DataFrame({
        'A': range(10),
        'B': range(10, 20)
    })
    
    result = selective_data_destroyer(df)
    
    assert isinstance(result, pd.DataFrame)
    # Should reduce to around 5 rows (50% of 10)
    assert len(result) >= 3  # Allow for some variance in clustering
    assert len(result) <= 7

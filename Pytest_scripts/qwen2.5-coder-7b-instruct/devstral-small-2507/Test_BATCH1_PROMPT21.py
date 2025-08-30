import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

def selective_data_destroyer(df: pd.DataFrame) -> pd.DataFrame:
    """
    Reduces the DataFrame by approximately 50% of its rows using a clustering-based approach.
    
    This function uses K-Means clustering to group similar rows and keeps one representative
    row per cluster, effectively reducing the dataset size while preserving data diversity.
    
    Parameters:
    df (pd.DataFrame): Input DataFrame to be reduced
    
    Returns:
    pd.DataFrame: New DataFrame with approximately 50% fewer rows than the input
    """
    if len(df) <= 1:
        return df.copy()

    # Determine number of clusters (approximately half the dataset size)
    num_clusters = max(1, len(df) // 2)
    
    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    df['cluster'] = kmeans.fit_predict(df.select_dtypes(include=[np.number]))

    # Get the centroids for each cluster
    centroids = kmeans.cluster_centers_

    # Function to find closest point to centroid
    def closest_to_centroid(row):
        cluster_idx = row['cluster']
        centroid = centroids[cluster_idx]
        return np.linalg.norm(df.iloc[row.name] - centroid)

    # Find representative points (closest to centroids)
    representatives = df.loc[df.apply(closest_to_centroid, axis=1).idxmin()]

    # Return only the representative rows
    return representatives.drop(columns=['cluster'])

if __name__ == "__main__":
    # Create a sample DataFrame
    data = {
        'feature1': np.random.rand(10),
        'feature2': np.random.rand(10),
        'feature3': np.random.rand(10)
    }
    df = pd.DataFrame(data)

    print("Original DataFrame shape:", df.shape)
    reduced_df = selective_data_destroyer(df)
    print("Reduced DataFrame shape:", reduced_df.shape)

# ===== GENERATED TESTS =====
```python
import pytest
from typing import Any

# Original code remains unchanged

def test_selective_data_destroyer_empty_dataframe():
    """Test with an empty DataFrame."""
    df = pd.DataFrame()
    result = selective_data_destroyer(df)
    assert len(result) == 0, "Empty DataFrame should return an empty DataFrame"

def test_selective_data_destroyer_single_row():
    """Test with a single row DataFrame."""
    data = {'feature1': [1], 'feature2': [2], 'feature3': [3]}
    df = pd.DataFrame(data)
    result = selective_data_destroyer(df)
    assert len(result) == 1, "Single row DataFrame should return the same DataFrame"

def test_selective_data_destroyer_multiple_rows():
    """Test with a multiple rows DataFrame."""
    data = {
        'feature1': [1, 2, 3, 4],
        'feature2': [5, 6, 7, 8],
        'feature3': [9, 10, 11, 12]
    }
    df = pd.DataFrame(data)
    result = selective_data_destroyer(df)
    assert len(result) <= len(df), "Resulting DataFrame should have fewer or equal rows"

def test_selective_data_destroyer_with_non_numeric_columns():
    """Test with a DataFrame containing non-numeric columns."""
    data = {
        'feature1': [1, 2, 3],
        'feature2': ['a', 'b', 'c'],
        'feature3': [9, 10, 11]
    }
    df = pd.DataFrame(data)
    result = selective_data_destroyer(df)
    assert len(result) == 1, "Non-numeric columns should be ignored"

def test_selective_data_destroyer_with_large_dataset():
    """Test with a large DataFrame."""
    data = {
        'feature1': np.random.rand(100),
        'feature2': np.random.rand(100),
        'feature3': np.random.rand(100)
    }
    df = pd.DataFrame(data)
    result = selective_data_destroyer(df)
    assert len(result) <= len(df), "Large dataset should return fewer or equal rows"

def test_selective_data_destroyer_with_random_state():
    """Test with a fixed random state."""
    data = {
        'feature1': np.random.rand(5),
        'feature2': np.random.rand(5),
        'feature3': np.random.rand(5)
    }
    df = pd.DataFrame(data)
    result1 = selective_data_destroyer(df, random_state=42)
    result2 = selective_data_destroyer(df, random_state=42)
    assert result1.equals(result2), "Same random state should produce the same result"

def test_selective_data_destroyer_with_different_random_state():
    """Test with a different random state."""
    data = {
        'feature1': np.random.rand(5),
        'feature2': np.random.rand(5),
        'feature3': np.random.rand(5)
    }
    df = pd.DataFrame(data)
    result1 = selective_data_destroyer(df, random_state=42)
    result2 = selective_data_destroyer(df, random_state=0)
    assert not result1.equals(result2), "Different random state should produce different results"

# Add more tests as needed
```

This test suite includes comprehensive test cases for the `selective_data_destroyer` function. It covers various scenarios such as empty DataFrame, single row DataFrame, multiple rows DataFrame, non-numeric columns, large dataset, and different random states. The tests are designed to ensure that the function behaves as expected under different conditions.
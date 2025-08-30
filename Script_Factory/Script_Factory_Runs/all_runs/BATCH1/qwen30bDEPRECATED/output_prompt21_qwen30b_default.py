import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def selective_data_destroyer(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes approximately 50% of rows from a DataFrame using an AI-inspired clustering strategy.
    
    This function identifies similar rows using K-Means clustering and retains one 
    representative row per cluster, effectively reducing the dataset size by about half.
    
    Parameters:
        df (pd.DataFrame): Input DataFrame to be reduced
    
    Returns:
        pd.DataFrame: A new DataFrame with approximately 50% of the original rows
    """
    if len(df) <= 1:
        return df.copy()
    
    # Select numeric columns for clustering
    numeric_df = df.select_dtypes(include=[np.number])
    
    if numeric_df.empty:
        # If no numeric columns, randomly drop 50%
        indices_to_drop = np.random.choice(df.index, size=len(df)//2, replace=False)
        return df.drop(indices_to_drop).reset_index(drop=True)
    
    # Standardize the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(numeric_df)
    
    # Determine number of clusters (up to 10 or n_rows//2, whichever is smaller)
    n_clusters = min(10, len(df) // 2)
    if n_clusters < 1:
        n_clusters = 1
    
    # Apply K-Means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(scaled_data)
    
    # For each cluster, keep one representative (first occurrence)
    indices_to_keep = []
    for i in range(n_clusters):
        cluster_indices = np.where(cluster_labels == i)[0]
        if len(cluster_indices) > 0:
            # Keep the first index of the cluster
            indices_to_keep.append(cluster_indices[0])
    
    # Convert back to original DataFrame indices
    original_indices = numeric_df.index[indices_to_keep]
    
    return df.loc[original_indices].reset_index(drop=True)

if __name__ == "__main__":
    # Create a sample DataFrame
    data = {
        'A': range(100),
        'B': np.random.randn(100),
        'C': np.random.choice(['X', 'Y', 'Z'], 100),
        'D': np.random.randint(0, 100, 100)
    }
    df = pd.DataFrame(data)
    
    print("Original shape:", df.shape)
    
    # Apply selective data destroyer
    reduced_df = selective_data_destroyer(df)
    
    print("Reduced shape:", reduced_df.shape)

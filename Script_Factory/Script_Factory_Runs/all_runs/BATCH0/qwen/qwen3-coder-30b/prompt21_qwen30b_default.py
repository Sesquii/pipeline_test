import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def selective_data_destroyer(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes approximately 50% of rows from a DataFrame using an AI-inspired clustering approach.
    
    This function identifies similar rows through KMeans clustering and retains one 
    representative row per cluster, effectively reducing the dataset size by half.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame to reduce in size
    
    Returns:
    pd.DataFrame: A new DataFrame with approximately 50% of the original rows
    """
    if len(df) <= 1:
        return df.copy()
    
    # Select numeric columns for clustering
    numeric_df = df.select_dtypes(include=[np.number])
    
    if numeric_df.empty:
        # If no numeric columns, randomly drop half
        indices_to_drop = np.random.choice(df.index, size=len(df)//2, replace=False)
        return df.drop(indices_to_drop).reset_index(drop=True)
    
    # Standardize the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(numeric_df)
    
    # Determine number of clusters (up to 50% of rows, but at least 1)
    n_clusters = max(1, len(df) // 2)
    if n_clusters >= len(df):
        n_clusters = len(df) - 1
    
    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(scaled_data)
    
    # For each cluster, keep the row closest to the centroid
    indices_to_keep = []
    for i in range(n_clusters):
        cluster_indices = np.where(cluster_labels == i)[0]
        if len(cluster_indices) > 0:
            # Find the point closest to the centroid
            centroid = kmeans.cluster_centers_[i]
            distances = np.linalg.norm(scaled_data[cluster_indices] - centroid, axis=1)
            closest_index = cluster_indices[np.argmin(distances)]
            indices_to_keep.append(closest_index)
    
    return df.iloc[indices_to_keep].reset_index(drop=True)

if __name__ == "__main__":
    # Create a sample DataFrame
    data = {
        'A': np.random.randn(100),
        'B': np.random.randn(100),
        'C': np.random.randint(0, 100, 100),
        'D': ['group_' + str(i % 10) for i in range(100)]
    }
    df = pd.DataFrame(data)
    
    print("Original DataFrame shape:", df.shape)
    
    # Apply the selective data destroyer
    reduced_df = selective_data_destroyer(df)
    
    print("Reduced DataFrame shape:", reduced_df.shape)

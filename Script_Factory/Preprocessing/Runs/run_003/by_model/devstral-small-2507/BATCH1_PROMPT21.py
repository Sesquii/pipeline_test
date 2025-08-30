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
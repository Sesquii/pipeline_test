import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

def selective_data_destroyer(df: pd.DataFrame) -> pd.DataFrame:
    """
    Selectively destroys approximately 50% of the rows in a DataFrame, mimicking AI decision-making through clustering.

    Parameters:
    df (pd.DataFrame): The input DataFrame to be processed.

    Returns:
    pd.DataFrame: A new DataFrame with around 50% fewer rows, achieved by keeping one representative from each cluster.
    """
    # Convert dataframe to numpy array for clustering
    data = df.values
    
    # Choose number of clusters based on the square root of the number of rows
    n_clusters = int(np.sqrt(df.shape[0]))

    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(data)
    
    # Get cluster labels and representative indices
    labels = kmeans.labels_
    representatives = np.argmin(np.linalg.norm(data[:, np.newaxis] - data[kmeans.cluster_centers_, :], axis=-1), axis=0)

    # Filter dataframe to only include representative rows
    reduced_df = df.iloc[representatives].copy()

    return reduced_df

if __name__ == "__main__":
    # Example usage:
    np.random.seed(42)
    sample_data = pd.DataFrame(np.random.rand(100, 5))
    
    original_shape = sample_data.shape
    reduced_df = selective_data_destroyer(sample_data)
    reduced_shape = reduced_df.shape

    print("Original DataFrame shape:", original_shape)
    print("Reduced DataFrame shape:", reduced_shape)
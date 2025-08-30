import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import numpy as np

# Placeholder for Spotify client credentials
CLIENT_ID = 'your_client_id_here'
CLIENT_SECRET = 'your_client_secret_here'
REDIRECT_URI = 'your_redirect_uri_here'

# Authenticate with Spotify
def get_spotify_client():
    auth_manager = SpotifyClientCredentials(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )
    return spotipy.Spotify(auth_manager=auth_manager)

# Get all tracks from a playlist
def get_playlist_tracks(sp, playlist_id):
    tracks = []
    offset = 0
    limit = 50  # Max limit for Spotify API
    
    while True:
        response = sp.playlist_tracks(playlist_id, offset=offset, limit=limit)
        tracks.extend(response['items'])
        
        if not response['next']:
            break
        offset += limit
    
    return tracks

# Aggregate audio features from tracks
def aggregate_audio_features(tracks):
    # Extract audio features for all tracks
    audio_features = [track['track']['audio_features'] for track in tracks if 'audio_features' in track['track']]
    
    # If no audio features found, return None
    if not audio_features:
        return None
    
    # Convert to numpy array for easier aggregation
    features_array = np.array(audio_features)
    
    # Calculate average for each feature
    avg_danceability = np.mean(features_array[:, 0])  # Index 0 is danceability
    avg_energy = np.mean(features_array[:, 1])        # Index 1 is energy
    avg_valence = np.mean(features_array[:, 2])       # Index 2 is valence
    
    return {
        'danceability': avg_danceability,
        'energy': avg_energy,
        'valence': avg_valence
    }

# Map audio features to weather category
def predict_weather(audio_features):
    if audio_features is None:
        return "Unknown"
    
    danceability = audio_features['danceability']
    energy = audio_features['energy']
    valence = audio_features['valence']
    
    # Rule-based mapping
    if energy > 0.7 and valence > 0.6 and danceability > 0.6:
        return "Sunny"
    elif energy < 0.4 and valence < 0.4:
        return "Cloudy"
    elif energy > 0.6 and valence < 0.3:
        return "Rainy"
    elif energy > 0.8 and danceability < 0.3:
        return "Stormy"
    else:
        return "Snowy"

# Main execution
def main():
    # Prompt user for playlist ID
    playlist_id = input("Enter the Spotify playlist ID: ")
    
    # Get Spotify client
    sp = get_spotify_client()
    
    # Fetch tracks from playlist
    tracks = get_playlist_tracks(sp, playlist_id)
    
    # Aggregate audio features
    avg_features = aggregate_audio_features(tracks)
    
    # Predict weather
    predicted_weather = predict_weather(avg_features)
    
    # Print result
    print(f"Predicted weather for tomorrow: {predicted_weather}")

if __name__ == "__main__":
    main()

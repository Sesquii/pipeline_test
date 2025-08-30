import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify client credentials (replace with your own)
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
REDIRECT_URI = 'your_redirect_uri'

# Initialize Spotipy with OAuth Client Credentials flow
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_playlist_tracks(playlist_id):
    """Fetches all tracks from a given playlist."""
    results = sp.playlist_tracks(playlist_id)
    return [track['track'] for track in results['items']]

def aggregate_audio_features(tracks):
    """Aggregates audio features across all tracks."""
    features = {'danceability': 0, 'energy': 0, 'valence': 0}
    total_tracks = len(tracks)

    for track in tracks:
        features['danceability'] += track['audio_features']['danceability'] if 'danceability' in track['audio_features'] else 0
        features['energy'] += track['audio_features']['energy'] if 'energy' in track['audio_features'] else 0
        features['valence'] += track['audio_features']['valence'] if 'valence' in track['audio_features'] else 0

    avg_features = {k: v / total_tracks for k, v in features.items()}
    return avg_features

def predict_weather(avg_features):
    """Simple rule-based weather prediction based on aggregated audio features."""
    danceability, energy, valence = avg_features['danceability'], avg_features['energy'], avg_features['valence']

    if danceability > 0.7 and energy > 0.8:
        return "Sunny"
    elif danceability < 0.4 and energy < 0.3:
        return "Stormy"
    elif valence < 0.2:
        return "Rainy"
    else:
        return "Cloudy"

def main():
    playlist_id = input("Enter your playlist ID: ")
    tracks = get_playlist_tracks(playlist_id)
    avg_features = aggregate_audio_features(tracks)
    predicted_weather = predict_weather(avg_features)

    print(f"\nPredicted weather for tomorrow:\n{predicted_weather.capitalize()}")

if __name__ == "__main__":
    main()
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Placeholder for your Spotify client credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'
redirect_uri = 'http://localhost:8080/callback'

# Authenticate with Spotify
auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_playlist_tracks(playlist_id):
    """Retrieve all tracks from the specified playlist."""
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    
    return tracks

def aggregate_audio_features(tracks):
    """Aggregate audio features across all tracks."""
    features = []
    for item in tracks:
        track_id = item['track']['id']
        feature = sp.audio_features(track_ids=[track_id])[0]
        features.append(feature)
    
    avg_danceability = sum(f['danceability'] for f in features) / len(features)
    avg_energy = sum(f['energy'] for f in features) / len(features)
    avg_valence = sum(f['valence'] for f in features) / len(features)
    
    return {
        'avg_danceability': avg_danceability,
        'avg_energy': avg_energy,
        'avg_valence': avg_valence
    }

def predict_weather(audio_features):
    """Predict weather based on aggregated audio features."""
    # Simple rule-based mapping
    if audio_features['avg_danceability'] > 0.6 and audio_features['avg_energy'] > 0.7:
        return "Sunny"
    elif audio_features['avg_energy'] > 0.5 and audio_features['avg_valence'] < 0.4:
        return "Cloudy"
    elif audio_features['avg_danceability'] < 0.3 and audio_features['avg_energy'] < 0.3:
        return "Snowy"
    elif audio_features['avg_danceability'] > 0.6 and audio_features['avg_energy'] > 0.5:
        return "Stormy"
    else:
        return "Rainy"

def main():
    playlist_id = input("Enter the Spotify playlist ID: ")
    tracks = get_playlist_tracks(playlist_id)
    audio_features = aggregate_audio_features(tracks)
    predicted_weather = predict_weather(audio_features)
    print(f"Predicted weather for tomorrow: {predicted_weather}")

if __name__ == "__main__":
    main()
```

This script authenticates with Spotify using the provided client credentials, retrieves all tracks from a specified playlist, aggregates audio features across those tracks, and then uses a simple rule-based mapping to predict the weather. The predicted weather is printed in a clear, human-readable format.

# ===== GENERATED TESTS =====
```python
import pytest
from unittest.mock import patch
from spotipy.oauth2 import SpotifyOAuth

# Placeholder for your Spotify client credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'
redirect_uri = 'http://localhost:8080/callback'

# Authenticate with Spotify
auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_playlist_tracks(playlist_id):
    """Retrieve all tracks from the specified playlist."""
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    
    return tracks

def aggregate_audio_features(tracks):
    """Aggregate audio features across all tracks."""
    features = []
    for item in tracks:
        track_id = item['track']['id']
        feature = sp.audio_features(track_ids=[track_id])[0]
        features.append(feature)
    
    avg_danceability = sum(f['danceability'] for f in features) / len(features)
    avg_energy = sum(f['energy'] for f in features) / len(features)
    avg_valence = sum(f['valence'] for f in features) / len(features)
    
    return {
        'avg_danceability': avg_danceability,
        'avg_energy': avg_energy,
        'avg_valence': avg_valence
    }

def predict_weather(audio_features):
    """Predict weather based on aggregated audio features."""
    # Simple rule-based mapping
    if audio_features['avg_danceability'] > 0.6 and audio_features['avg_energy'] > 0.7:
        return "Sunny"
    elif audio_features['avg_energy'] > 0.5 and audio_features['avg_valence'] < 0.4:
        return "Cloudy"
    elif audio_features['avg_danceability'] < 0.3 and audio_features['avg_energy'] < 0.3:
        return "Snowy"
    elif audio_features['avg_danceability'] > 0.6 and audio_features['avg_energy'] > 0.5:
        return "Stormy"
    else:
        return "Rainy"

def main():
    playlist_id = input("Enter the Spotify playlist ID: ")
    tracks = get_playlist_tracks(playlist_id)
    audio_features = aggregate_audio_features(tracks)
    predicted_weather = predict_weather(audio_features)
    print(f"Predicted weather for tomorrow: {predicted_weather}")

if __name__ == "__main__":
    main()

# Test suite
@patch('spotipy.Spotify.playlist_tracks')
@patch('spotipy.Spotify.audio_features')
def test_get_playlist_tracks(mock_audio_features, mock_playlist_tracks):
    """Test get_playlist_tracks function."""
    playlist_id = 'test_playlist_id'
    mock_playlist_tracks.return_value = {
        'items': [
            {'track': {'id': 'track1'}},
            {'track': {'id': 'track2'}}
        ],
        'next': None
    }
    mock_audio_features.return_value = [{'danceability': 0.7, 'energy': 0.8}, {'danceability': 0.6, 'energy': 0.9}]
    
    tracks = get_playlist_tracks(playlist_id)
    assert len(tracks) == 2
    assert tracks[0]['track']['id'] == 'track1'
    assert tracks[1]['track']['id'] == 'track2'

@patch('spotipy.Spotify.audio_features')
def test_aggregate_audio_features(mock_audio_features):
    """Test aggregate_audio_features function."""
    mock_audio_features.return_value = [{'danceability': 0.7, 'energy': 0.8}, {'danceability': 0.6, 'energy': 0.9}]
    
    audio_features = aggregate_audio_features([{'track': {'id': 'track1'}}, {'track': {'id': 'track2'}}])
    assert audio_features['avg_danceability'] == pytest.approx(0.65)
    assert audio_features['avg_energy'] == pytest.approx(0.85)
    assert audio_features['avg_valence'] == 0

def test_predict_weather():
    """Test predict_weather function."""
    audio_features = {
        'avg_danceability': 0.7,
        'avg_energy': 0.9,
        'avg_valence': 0
    }
    predicted_weather = predict_weather(audio_features)
    assert predicted_weather == "Sunny"

def test_predict_weather_cloudy():
    """Test predict_weather function for cloudy weather."""
    audio_features = {
        'avg_danceability': 0.4,
        'avg_energy': 0.6,
        'avg_valence': 0.2
    }
    predicted_weather = predict_weather(audio_features)
    assert predicted_weather == "Cloudy"

def test_predict_weather_snowy():
    """Test predict_weather function for snowy weather."""
    audio_features = {
        'avg_danceability': 0.1,
        'avg_energy': 0.2,
        'avg_valence': 0
    }
    predicted_weather = predict_weather(audio_features)
    assert predicted_weather == "Snowy"

def test_predict_weather_stormy():
    """Test predict_weather function for stormy weather."""
    audio_features = {
        'avg_danceability': 0.7,
        'avg_energy': 0.6,
        'avg_valence': 0
    }
    predicted_weather = predict_weather(audio_features)
    assert predicted_weather == "Stormy"

def test_predict_weather_rainy():
    """Test predict_weather function for rainy weather."""
    audio_features = {
        'avg_danceability': 0.4,
        'avg_energy': 0.5,
        'avg_valence': 0.3
    }
    predicted_weather = predict_weather(audio_features)
    assert predicted_weather == "Rainy"
```
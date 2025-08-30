import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Placeholder for Spotify client credentials
client_id = 'your_spotify_client_id'
client_secret = 'your_spotify_client_secret'
redirect_uri = 'your_redirect_uri'

# Authenticate with Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope="playlist-read-private"))

def get_playlist_tracks(playlist_id):
    """Retrieve all tracks from the user's current playlist"""
    results = sp.playlist_items(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

def get_audio_features(tracks):
    """Get audio features for all tracks in the playlist"""
    track_ids = [track['track']['id'] for track in tracks]
    audio_features = sp.audio_features(track_ids)
    return audio_features

def aggregate_audio_features(audio_features):
    """Aggregate audio features across all tracks"""
    if not audio_features:
        return None

    total_danceability = 0
    total_energy = 0
    total_valence = 0
    count = len(audio_features)

    for feature in audio_features:
        if feature:
            total_danceability += feature['danceability']
            total_energy += feature['energy']
            total_valence += feature['valence']

    avg_danceability = total_danceability / count
    avg_energy = total_energy / count
    avg_valence = total_valence / count

    return {
        'avg_danceability': avg_danceability,
        'avg_energy': avg_energy,
        'avg_valence': avg_valence
    }

def predict_weather(audio_features):
    """Simple rule-based mapping from audio features to weather categories"""
    if not audio_features:
        return "Unknown"

    danceability = audio_features['avg_danceability']
    energy = audio_features['avg_energy']
    valence = audio_features['avg_valence']

    # Simple deterministic mapping rules
    if danceability > 0.7 and energy > 0.7 and valence > 0.7:
        return "Sunny"
    elif 0.5 <= danceability <= 0.7 and 0.5 <= energy <= 0.7:
        return "Cloudy"
    elif danceability < 0.4 or valence < 0.4:
        return "Rainy"
    elif energy > 0.8 and valence < 0.5:
        return "Stormy"
    else:
        return "Snowy"

def main():
    # Ask user for playlist ID
    playlist_id = input("Enter your Spotify playlist ID: ").strip()

    # Get tracks from playlist
    tracks = get_playlist_tracks(playlist_id)
    print(f"Found {len(tracks)} tracks in the playlist")

    # Get audio features for all tracks
    audio_features = get_audio_features(tracks)

    # Aggregate audio features
    aggregated_features = aggregate_audio_features(audio_features)

    # Predict weather based on audio features
    predicted_weather = predict_weather(aggregated_features)

    # Print the prediction
    print(f"\nBased on your playlist, tomorrow's weather is predicted to be: {predicted_weather}")

if __name__ == "__main__":
    main()
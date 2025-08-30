import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import statistics

# Placeholder for Spotify client credentials
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
redirect_uri = "YOUR_REDIRECT_URI"

# Authenticate with Spotify
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_playlist_tracks(playlist_id):
    """
    Retrieve all tracks from a given playlist.
    Assumes the playlist is public or the user has access.
    """
    tracks = []
    offset = 0
    limit = 50  # Spotify API limit per request

    while True:
        response = sp.playlist_tracks(playlist_id, offset=offset, limit=limit)
        for item in response['items']:
            track = item['track']
            if track is not None:  # Ensure track data exists
                tracks.append(track)
        
        if len(response['items']) < limit:
            break
        offset += limit

    return tracks

def get_audio_features(tracks):
    """
    Extract audio features for all tracks.
    """
    track_ids = [track['id'] for track in tracks]
    audio_features = sp.audio_features(track_ids)
    
    # Filter out any None values (shouldn't happen in normal cases)
    audio_features = [f for f in audio_features if f is not None]
    
    return audio_features

def aggregate_audio_features(audio_features):
    """
    Calculate average values for key audio features.
    """
    if not audio_features:
        raise ValueError("No audio features found.")

    # Extract relevant features
    danceability_list = [f['danceability'] for f in audio_features]
    energy_list = [f['energy'] for f in audio_features]
    valence_list = [f['valence'] for f in audio_features]

    # Compute averages
    avg_danceability = statistics.mean(danceability_list)
    avg_energy = statistics.mean(energy_list)
    avg_valence = statistics.mean(valence_list)

    return {
        'danceability': avg_danceability,
        'energy': avg_energy,
        'valence': avg_valence
    }

def predict_weather(aggregated_features):
    """
    Predict weather based on aggregated audio features.
    Mapping is deterministic and rule-based.
    """
    # Rule-based mapping from audio features to weather types
    dance = aggregated_features['danceability']
    energy = aggregated_features['energy']
    valence = aggregated_features['valence']

    # Determine weather type based on simple rules
    if valence < 0.3 and energy < 0.4:
        return "Rainy"
    elif valence > 0.7 and energy > 0.7 and dance > 0.7:
        return "Sunny"
    elif valence < 0.4 and energy > 0.6:
        return "Stormy"
    elif valence < 0.3 and energy < 0.5:
        return "Cloudy"
    else:
        return "Snowy"  # Default case

def main():
    """
    Main function to run the weather prediction script.
    Assumes user will input a valid playlist ID.
    """
    # Input playlist ID from user
    playlist_id = input("Enter your Spotify playlist ID: ")

    try:
        # Fetch all tracks in the playlist
        tracks = get_playlist_tracks(playlist_id)

        # Get audio features for all tracks
        audio_features = get_audio_features(tracks)

        # Aggregate audio features
        aggregated = aggregate_audio_features(audio_features)

        # Predict weather
        predicted_weather = predict_weather(aggregated)

        # Print result
        print(f"Predicted weather for tomorrow: {predicted_weather}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

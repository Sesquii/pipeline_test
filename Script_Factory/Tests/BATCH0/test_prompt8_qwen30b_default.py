import pytest
import sys, os
from unittest.mock import patch, MagicMock
from Script_Factory.Script_Factory_Runs.all_runs.prompt8_qwen30b_default import (

from Script_Factory.Script_Factory_Runs.all_runs.prompt8_qwen30b_default import (
    add_transaction,
    compute_hash,
    create_genesis_block,
    finalize_block,
    run
)

    get_playlist_tracks,
    get_audio_features,
    aggregate_audio_features,
    predict_weather
)

# Mock Spotify API responses for testing
mock_playlist_response = {
    'items': [
        {
            'track': {
                'id': '1',
                'name': 'Track 1',
                'artists': [{'name': 'Artist 1'}]
            }
        },
        {
            'track': {
                'id': '2',
                'name': 'Track 2',
                'artists': [{'name': 'Artist 2'}]
            }
        }
    ]
}

mock_audio_features_response = [
    {
        'danceability': 0.5,
        'energy': 0.6,
        'valence': 0.7
    },
    {
        'danceability': 0.4,
        'energy': 0.5,
        'valence': 0.6
    }
]

def test_get_playlist_tracks_normal_case():
    """Test get_playlist_tracks with normal, expected inputs"""
    with patch('spotipy.Spotify.playlist_tracks') as mock_playlist_tracks:
        mock_playlist_tracks.return_value = mock_playlist_response
        result = get_playlist_tracks('test_playlist_id')
        
        # Verify that the function returns tracks
        assert len(result) == 2
        assert result[0]['id'] == '1'
        assert result[1]['id'] == '2'

def test_get_playlist_tracks_empty_playlist():
    """Test get_playlist_tracks with empty playlist"""
    with patch('spotipy.Spotify.playlist_tracks') as mock_playlist_tracks:
        mock_playlist_tracks.return_value = {'items': []}
        result = get_playlist_tracks('empty_playlist_id')
        
        # Verify that the function returns empty list
        assert len(result) == 0

def test_get_audio_features_normal_case():
    """Test get_audio_features with normal, expected inputs"""
    with patch('spotipy.Spotify.audio_features') as mock_audio_features:
        mock_audio_features.return_value = mock_audio_features_response
        tracks = [{'id': '1'}, {'id': '2'}]
        result = get_audio_features(tracks)
        
        # Verify that the function returns audio features
        assert len(result) == 2
        assert result[0]['danceability'] == 0.5
        assert result[1]['energy'] == 0.5

def test_get_audio_features_with_none_values():
    """Test get_audio_features with None values in response"""
    with patch('spotipy.Spotify.audio_features') as mock_audio_features:
        mock_audio_features.return_value = [mock_audio_features_response[0], None]
        tracks = [{'id': '1'}, {'id': '2'}]
        result = get_audio_features(tracks)
        
        # Verify that the function filters out None values
        assert len(result) == 1
        assert result[0]['danceability'] == 0.5

def test_aggregate_audio_features_normal_case():
    """Test aggregate_audio_features with normal, expected inputs"""
    result = aggregate_audio_features(mock_audio_features_response)
    
    # Verify that the function returns correct averages
    assert result['danceability'] == 0.45
    assert result['energy'] == 0.55
    assert result['valence'] == 0.65

def test_aggregate_audio_features_empty_input():
    """Test aggregate_audio_features with empty input - should raise ValueError"""
    with pytest.raises(ValueError, match="No audio features found."):
        aggregate_audio_features([])

def test_predict_weather_sunny_case():
    """Test predict_weather with sunny conditions"""
    features = {
        'danceability': 0.8,
        'energy': 0.8,
        'valence': 0.8
    }
    result = predict_weather(features)
    
    # Verify that the function returns "Sunny"
    assert result == "Sunny"

def test_predict_weather_rainy_case():
    """Test predict_weather with rainy conditions"""
    features = {
        'danceability': 0.2,
        'energy': 0.3,
        'valence': 0.2
    }
    result = predict_weather(features)
    
    # Verify that the function returns "Rainy"
    assert result == "Rainy"

def test_predict_weather_stormy_case():
    """Test predict_weather with stormy conditions"""
    features = {
        'danceability': 0.3,
        'energy': 0.8,
        'valence': 0.2
    }
    result = predict_weather(features)
    
    # Verify that the function returns "Stormy"
    assert result == "Stormy"

def test_predict_weather_cloudy_case():
    """Test predict_weather with cloudy conditions"""
    features = {
        'danceability': 0.3,
        'energy': 0.4,
        'valence': 0.2
    }
    result = predict_weather(features)
    
    # Verify that the function returns "Cloudy"
    assert result == "Cloudy"

def test_predict_weather_snowy_default_case():
    """Test predict_weather with default snowy conditions"""
    features = {
        'danceability': 0.5,
        'energy': 0.5,
        'valence': 0.5
    }
    result = predict_weather(features)
    
    # Verify that the function returns "Snowy" (default case)
    assert result == "Snowy"

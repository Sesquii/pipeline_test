import pytest
import sys, os
from unittest.mock import patch, MagicMock
from Script_Factory.Script_Factory_Runs.all_runs.prompt7_qwen30b_default import (

from Script_Factory.Script_Factory_Runs.all_runs.prompt7_qwen30b_default import (
    aggregate_audio_features,
    get_audio_features,
    get_playlist_tracks,
    main,
    predict_weather
)

    get_playlist_tracks,
    get_audio_features,
    aggregate_audio_features,
    predict_weather
)

# Mock Spotify API responses for testing
MOCK_TRACKS = [
    {'id': '1', 'name': 'Track 1', 'artists': [{'name': 'Artist 1'}]},
    {'id': '2', 'name': 'Track 2', 'artists': [{'name': 'Artist 2'}]}
]

MOCK_AUDIO_FEATURES = [
    {'danceability': 0.5, 'energy': 0.6, 'valence': 0.7},
    {'danceability': 0.4, 'energy': 0.5, 'valence': 0.6}
]

MOCK_EMPTY_AUDIO_FEATURES = []

MOCK_AGGREGATED_FEATURES = {
    'danceability': 0.45,
    'energy': 0.55,
    'valence': 0.65
}

def test_get_playlist_tracks_normal_case():
    """Test get_playlist_tracks with normal, expected inputs."""
    mock_response = {
        'items': [
            {'track': MOCK_TRACKS[0]},
            {'track': MOCK_TRACKS[1]}
        ]
    }
    
    with patch('spotipy.Spotify.playlist_tracks', return_value=mock_response):
        result = get_playlist_tracks('test_playlist_id')
        assert len(result) == 2
        assert result[0]['name'] == 'Track 1'
        assert result[1]['name'] == 'Track 2'

def test_get_playlist_tracks_empty_playlist():
    """Test get_playlist_tracks with empty playlist (edge case)."""
    mock_response = {'items': []}
    
    with patch('spotipy.Spotify.playlist_tracks', return_value=mock_response):
        result = get_playlist_tracks('empty_playlist_id')
        assert len(result) == 0

def test_get_audio_features_normal_case():
    """Test get_audio_features with normal, expected inputs."""
    mock_response = MOCK_AUDIO_FEATURES
    
    with patch('spotipy.Spotify.audio_features', return_value=mock_response):
        result = get_audio_features(MOCK_TRACKS)
        assert len(result) == 2
        assert result[0]['danceability'] == 0.5
        assert result[1]['energy'] == 0.5

def test_get_audio_features_with_none_values():
    """Test get_audio_features with None values in response (edge case)."""
    mock_response = [MOCK_AUDIO_FEATURES[0], None, MOCK_AUDIO_FEATURES[1]]
    
    with patch('spotipy.Spotify.audio_features', return_value=mock_response):
        result = get_audio_features(MOCK_TRACKS)
        assert len(result) == 2  # Should filter out None values

def test_get_audio_features_empty_input():
    """Test get_audio_features with empty tracks list (edge case)."""
    mock_response = []
    
    with patch('spotipy.Spotify.audio_features', return_value=mock_response):
        result = get_audio_features([])
        assert len(result) == 0

def test_aggregate_audio_features_normal_case():
    """Test aggregate_audio_features with normal, expected inputs."""
    result = aggregate_audio_features(MOCK_AUDIO_FEATURES)
    assert 'danceability' in result
    assert 'energy' in result
    assert 'valence' in result
    assert result['danceability'] == 0.45
    assert result['energy'] == 0.55
    assert result['valence'] == 0.65

def test_aggregate_audio_features_empty_input():
    """Test aggregate_audio_features with empty input (edge case)."""
    with pytest.raises(ValueError, match="No audio features found."):
        aggregate_audio_features([])

def test_predict_weather_rainy():
    """Test predict_weather with rainy weather conditions."""
    features = {'danceability': 0.2, 'energy': 0.3, 'valence': 0.2}
    result = predict_weather(features)
    assert result == "Rainy"

def test_predict_weather_sunny():
    """Test predict_weather with sunny weather conditions."""
    features = {'danceability': 0.8, 'energy': 0.8, 'valence': 0.8}
    result = predict_weather(features)
    assert result == "Sunny"

def test_predict_weather_stormy():
    """Test predict_weather with stormy weather conditions."""
    features = {'danceability': 0.3, 'energy': 0.8, 'valence': 0.2}
    result = predict_weather(features)
    assert result == "Stormy"

def test_predict_weather_cloudy():
    """Test predict_weather with cloudy weather conditions."""
    features = {'danceability': 0.2, 'energy': 0.4, 'valence': 0.2}
    result = predict_weather(features)
    assert result == "Cloudy"

def test_predict_weather_snowy_default():
    """Test predict_weather with snowy (default) weather conditions."""
    features = {'danceability': 0.5, 'energy': 0.5, 'valence': 0.5}
    result = predict_weather(features)
    assert result == "Snowy"

def test_predict_weather_edge_case_values():
    """Test predict_weather with edge case values at boundaries."""
    # Test exactly at boundary conditions
    features = {'danceability': 0.3, 'energy': 0.4, 'valence': 0.3}
    result = predict_weather(features)
    assert result == "Rainy"  # This should match the rainy condition

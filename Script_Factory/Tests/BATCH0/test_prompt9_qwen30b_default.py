import pytest
import sys, os
from unittest.mock import Mock, patch
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import statistics

# Import the functions to test
from your_module import (

from Script_Factory.Script_Factory_Runs.all_runs.prompt9_qwen30b_default import (
    get_compliment_or_insult,
    initialize_random_seed,
    main_loop
)

    get_playlist_tracks,
    get_audio_features,
    aggregate_audio_features,
    predict_weather
)

def test_get_playlist_tracks_normal_case():
    """Test normal case with a playlist containing tracks"""
    # Mock Spotify API response
    mock_response = {
        'items': [
            {'track': {'id': '1', 'name': 'Track 1'}},
            {'track': {'id': '2', 'name': 'Track 2'}}
        ]
    }
    
    with patch('your_module.sp') as mock_sp:
        mock_sp.playlist_tracks.return_value = mock_response
        result = get_playlist_tracks('test_playlist_id')
        
        assert len(result) == 2
        assert result[0]['id'] == '1'
        assert result[1]['id'] == '2'

def test_get_playlist_tracks_empty_playlist():
    """Test with empty playlist"""
    mock_response = {'items': []}
    
    with patch('your_module.sp') as mock_sp:
        mock_sp.playlist_tracks.return_value = mock_response
        result = get_playlist_tracks('empty_playlist_id')
        
        assert len(result) == 0

def test_get_playlist_tracks_with_none_tracks():
    """Test with tracks that have None values"""
    mock_response = {
        'items': [
            {'track': None},
            {'track': {'id': '1', 'name': 'Track 1'}},
            {'track': None}
        ]
    }
    
    with patch('your_module.sp') as mock_sp:
        mock_sp.playlist_tracks.return_value = mock_response
        result = get_playlist_tracks('test_playlist_id')
        
        assert len(result) == 1
        assert result[0]['id'] == '1'

def test_get_audio_features_normal_case():
    """Test normal case with valid track IDs"""
    tracks = [
        {'id': '1', 'name': 'Track 1'},
        {'id': '2', 'name': 'Track 2'}
    ]
    
    mock_audio_features = [
        {'danceability': 0.5, 'energy': 0.6, 'valence': 0.7},
        {'danceability': 0.4, 'energy': 0.5, 'valence': 0.6}
    ]
    
    with patch('your_module.sp') as mock_sp:
        mock_sp.audio_features.return_value = mock_audio_features
        result = get_audio_features(tracks)
        
        assert len(result) == 2
        assert result[0]['danceability'] == 0.5
        assert result[1]['energy'] == 0.5

def test_get_audio_features_with_none_values():
    """Test with some None values in audio features"""
    tracks = [
        {'id': '1', 'name': 'Track 1'},
        {'id': '2', 'name': 'Track 2'}
    ]
    
    mock_audio_features = [
        {'danceability': 0.5, 'energy': 0.6, 'valence': 0.7},
        None,
        {'danceability': 0.4, 'energy': 0.5, 'valence': 0.6}
    ]
    
    with patch('your_module.sp') as mock_sp:
        mock_sp.audio_features.return_value = mock_audio_features
        result = get_audio_features(tracks)
        
        assert len(result) == 2

def test_aggregate_audio_features_normal_case():
    """Test normal case with valid audio features"""
    audio_features = [
        {'danceability': 0.5, 'energy': 0.6, 'valence': 0.7},
        {'danceability': 0.4, 'energy': 0.5, 'valence': 0.6}
    ]
    
    result = aggregate_audio_features(audio_features)
    
    assert result['danceability'] == 0.45
    assert result['energy'] == 0.55
    assert result['valence'] == 0.65

def test_aggregate_audio_features_empty_input():
    """Test with empty audio features list - should raise ValueError"""
    with pytest.raises(ValueError, match="No audio features found."):
        aggregate_audio_features([])

def test_predict_weather_rainy():
    """Test rainy weather prediction"""
    aggregated_features = {
        'danceability': 0.2,
        'energy': 0.3,
        'valence': 0.2
    }
    
    result = predict_weather(aggregated_features)
    assert result == "Rainy"

def test_predict_weather_sunny():
    """Test sunny weather prediction"""
    aggregated_features = {
        'danceability': 0.8,
        'energy': 0.8,
        'valence': 0.8
    }
    
    result = predict_weather(aggregated_features)
    assert result == "Sunny"

def test_predict_weather_stormy():
    """Test stormy weather prediction"""
    aggregated_features = {
        'danceability': 0.3,
        'energy': 0.8,
        'valence': 0.2
    }
    
    result = predict_weather(aggregated_features)
    assert result == "Stormy"

def test_predict_weather_cloudy():
    """Test cloudy weather prediction"""
    aggregated_features = {
        'danceability': 0.3,
        'energy': 0.4,
        'valence': 0.2
    }
    
    result = predict_weather(aggregated_features)
    assert result == "Cloudy"

def test_predict_weather_snowy_default():
    """Test snowy weather prediction (default case)"""

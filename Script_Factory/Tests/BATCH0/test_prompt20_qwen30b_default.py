import pytest
import sys, os
from unittest.mock import patch, Mock
from Script_Factory.Script_Factory_Runs.all_runs.prompt20_qwen30b_default import (

from Script_Factory.Script_Factory_Runs.all_runs.prompt20_qwen30b_default import (
    create_fictional_headline,
    fetch_real_headlines,
    generate_fake_fragment,
    generate_mixed_headlines,
    main
)

    fetch_real_headlines,
    generate_fake_fragment,
    create_fictional_headline,
    generate_mixed_headlines
)

def test_fetch_real_headlines_success():
    """Test fetch_real_headlines with successful HTTP request and valid data."""
    # Mock the requests.get to return a successful response
    mock_response = Mock()
    mock_response.text = """
    <html>
        <body>
            <h3 class="gs-c-promo-heading__title">Real headline 1</h3>
            <h2 class="media__title">Real headline 2</h2>
            <h3>Short</h3>
            <h2 class="gs-c-promo-heading__title">Another real headline</h2>
        </body>
    </html>
    """
    mock_response.raise_for_status.return_value = None
    
    with patch('requests.get', return_value=mock_response):
        result = fetch_real_headlines()
        
    # Should return at least 2 valid headlines (excluding short ones)
    assert len(result) >= 2
    assert "Real headline 1" in result
    assert "Real headline 2" in result

def test_fetch_real_headlines_network_error():
    """Test fetch_real_headlines when network request fails."""
    # Mock requests.get to raise an exception
    with patch('requests.get', side_effect=requests.RequestException("Network error")):
        result = fetch_real_headlines()
        
    # Should return fallback headlines when network fails
    assert len(result) == 10
    assert "Global leaders meet in emergency summit" in result

def test_fetch_real_headlines_empty_response():
    """Test fetch_real_headlines with empty response."""
    mock_response = Mock()
    mock_response.text = ""
    mock_response.raise_for_status.return_value = None
    
    with patch('requests.get', return_value=mock_response):
        result = fetch_real_headlines()
        
    # Should return fallback headlines when response is empty
    assert len(result) == 10
    assert "Global leaders meet in emergency summit" in result

def test_generate_fake_fragment():
    """Test generate_fake_fragment produces valid output."""
    result = generate_fake_fragment()
    
    # Should return a string with at least 3 words (adjective verb noun)
    assert isinstance(result, str)
    assert len(result.split()) >= 3
    assert len(result) > 0

def test_create_fictional_headline():
    """Test create_fictional_headline produces valid output."""
    result = create_fictional_headline()
    
    # Should return a string with at least 3 words
    assert isinstance(result, str)
    assert len(result.split()) >= 3
    assert len(result) > 0

def test_generate_mixed_headlines_normal_case():
    """Test generate_mixed_headlines with normal inputs."""
    real_headlines = ["Headline 1", "Headline 2", "Headline 3"]
    result = generate_mixed_headlines(real_headlines, 5)
    
    # Should return exactly 5 headlines
    assert len(result) == 5
    assert all(isinstance(headline, str) for headline in result)

def test_generate_mixed_headlines_empty_real_headlines():
    """Test generate_mixed_headlines with empty real headlines list."""
    real_headlines = []
    result = generate_mixed_headlines(real_headlines, 3)
    
    # Should still return headlines (using fallback logic)
    assert len(result) == 3
    assert all(isinstance(headline, str) for headline in result)

def test_generate_mixed_headlines_zero_count():
    """Test generate_mixed_headlines with zero count."""
    real_headlines = ["Headline 1", "Headline 2"]
    result = generate_mixed_headlines(real_headlines, 0)
    
    # Should return empty list
    assert len(result) == 0

def test_generate_mixed_headlines_single_real_headline():
    """Test generate_mixed_headlines with single real headline."""
    real_headlines = ["Single headline"]
    result = generate_mixed_headlines(real_headlines, 3)
    
    # Should return exactly 3 headlines
    assert len(result) == 3
    assert all(isinstance(headline, str) for headline in result)

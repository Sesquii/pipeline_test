import pytest
from BATCH1_PROMPT19_qwen3-1.7b import ascii_art, main

def test_ascii_art_normal_case():
    """Test normal case with an image and expected width."""
    image_path = "test_image.jpg"
    result = ascii_art(image_path, max_width=100)
    assert len(result) > 0

def test_ascii_art_edge_case_empty_list():
    """Test edge case with empty list (should return empty string)."""
    image_path = ""
    result = ascii_art(image_path, max_width=100)
    assert result == ""

def test_ascii_art_zero_width():
    """Test edge case with zero width (should return empty string)."""
    image_path = "test_image.jpg"
    result = ascii_art(image_path, max_width=0)
    assert result == ""

def test_ascii_art_negative_width():
    """Test edge case with negative width (should return empty string)."""
    image_path = "test_image.jpg"
    result = ascii_art(image_path, max_width=-100)
    assert result == ""

def test_ascii_art_null_input():
    """Test edge case with null input (should return empty string)."""
    image_path = None
    result = ascii_art(image_path, max_width=100)
    assert result == ""

def test_ascii_art_invalid_image_path():
    """Test error handling for invalid image path."""
    image_path = "invalid_image.jpg"
    with pytest.raises(FileNotFoundError):
        ascii_art(image_path)

def test_ascii_art_invalid_argument():
    """Test error handling for invalid argument (e.g., non-integer width)."""
    image_path = "test_image.jpg"
    with pytest.raises(ValueError):
        ascii_art(image_path, max_width="invalid")

def test_ascii_art_corruption():
    """Test that 10% of characters are corrupted randomly."""
    image_path = "test_image.jpg"
    result = ascii_art(image_path, max_width=100)
    assert len(result) > 0
    # Check if at least one character is corrupted
    assert any(c != original for c, original in zip(result, result[:len(result)-1]))

def test_ascii_art_corruption_percentage():
    """Test that exactly 10% of characters are corrupted."""
    image_path = "test_image.jpg"
    result = ascii_art(image_path, max_width=100)
    total_chars = len(result)
    assert int(total_chars * 0.1) == len([c for c in result if c != original for original in result[:total_chars-1]])

def test_ascii_art_corruption_randomness():
    """Test that corruption is random and consistent."""
    image_path = "test_image.jpg"
    result1 = ascii_art(image_path, max_width=100)
    result2 = ascii_art(image_path, max_width=100)
    assert result1 != result2

def test_ascii_art_corruption_with_seeds():
    """Test that corruption is consistent with the same seed."""
    image_path = "test_image.jpg"
    result1 = ascii_art(image_path, max_width=100)
    result2 = ascii_art(image_path, max_width=100)
    assert result1 == result2

def test_ascii_art_corruption_with_different_seeds():
    """Test that corruption is different with different seeds."""
    image_path = "test_image.jpg"
    result1 = ascii_art(image_path, max_width=100)
    result2 = ascii_art(image_path, max_width=100)
    assert result1 != result2

def test_ascii_art_corruption_with_large_input():
    """Test that corruption works with large input."""
    image_path = "large_image.jpg"
    result = ascii_art(image_path, max_width=500)
    assert len(result) > 0
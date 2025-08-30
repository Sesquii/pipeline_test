import pytest
import sys, os
from unittest.mock import patch, MagicMock
import random
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
# Import the function to be tested


from Script_Factory.Script_Factory_Runs.all_runs.prompt6_qwen30b_default import (
    randomized_password_crippler
)

def test_normal_password_with_default_remove_count():
    """Test normal password input with default remove_count of 2"""
    # Mock random.choice and random.shuffle to control behavior
    with patch('random.choice') as mock_choice, \
         patch('random.shuffle') as mock_shuffle:
        
        # Set up mocks to return predictable values
        mock_choice.side_effect = ['A', 'b', '1', '!']  # For padding and category additions
        mock_shuffle.side_effect = lambda x: x.reverse()  # Simple reverse for testing
        
        # Test with a normal password that meets requirements
        result = randomized_password_crippler("Password123!")
        
        # Should return a string (length >= 12 due to padding)
        assert isinstance(result, str)
        assert len(result) >= 12


def test_short_password_padding():
    """Test that short passwords are padded to minimum length of 12"""
    with patch('random.choice') as mock_choice:
        # Mock random characters to return predictable values
        mock_choice.side_effect = ['X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        
        result = randomized_password_crippler("short")
        
        # Should be at least 12 characters long after padding
        assert len(result) >= 12
        # Should contain the original password plus padding
        assert "short" in result


def test_password_with_missing_categories():
    """Test password that's missing one or more character categories"""
    with patch('random.choice') as mock_choice:
        # Mock to return specific characters for testing
        mock_choice.side_effect = ['A', 'b', '1', '!']  # For category additions
        
        # Test with password missing uppercase, lowercase, digit, and special chars
        result = randomized_password_crippler("no_categories")
        
        # Should have at least one character from each required category
        assert any(c.isupper() for c in result)
        assert any(c.islower() for c in result)
        assert any(c.isdigit() for c in result)
        assert any(c in "!@#$%^&*()-_=+[]{};:,.<>?" for c in result)


def test_remove_count_zero():
    """Test with remove_count = 0 (should return original password after strengthening)"""
    with patch('random.choice') as mock_choice, \
         patch('random.shuffle') as mock_shuffle:
        
        # Set up predictable behavior
        mock_choice.side_effect = ['A', 'b', '1', '!']
        mock_shuffle.return_value = None  # No shuffling for this test
        
        result = randomized_password_crippler("TestPass123!", remove_count=0)
        
        # Should return a strengthened password (at least 12 chars with all categories)
        assert len(result) >= 12
        assert any(c.isupper() for c in result)
        assert any(c.islower() for c in result)
        assert any(c.isdigit() for c in result)


def test_remove_count_negative():
    """Test with negative remove_count (should return original password after strengthening)"""
    with patch('random.choice') as mock_choice, \
         patch('random.shuffle') as mock_shuffle:
        
        # Set up predictable behavior
        mock_choice.side_effect = ['A', 'b', '1', '!']
        mock_shuffle.return_value = None
        
        result = randomized_password_crippler("TestPass123!", remove_count=-1)
        
        # Should return a strengthened password (at least 12 chars with all categories)
        assert len(result) >= 12
        assert any(c.isupper() for c in result)
        assert any(c.islower() for c in result)
        assert any(c.isdigit() for c in result)


def test_empty_password():
    """Test with empty password (should be padded to minimum length)"""
    with patch('random.choice') as mock_choice:
        # Mock random characters to return predictable values
        mock_choice.side_effect = ['A', 'b', '1', '!', 'X', 'Y', 'Z', 'P', 'Q', 'R', 'S', 'T']
        
        result = randomized_password_crippler("")
        
        # Should be at least 12 characters long after padding
        assert len(result) >= 12
        # Should contain required character categories
        assert any(c.isupper() for c in result)
        assert any(c.islower() for c in result)
        assert any(c.isdigit() for c in result)
        assert any(c in "!@#$%^&*()-_=+[]{};:,.<>?" for c in result)


def test_password_with_remove_count_larger_than_length():
    """Test when remove_count is larger than password length"""
    with patch('random.choice') as mock_choice, \
         patch('random.shuffle') as mock_shuffle:
        
        # Mock to return predictable values
        mock_choice.side_effect = ['A', 'b', '1', '!']
        mock_shuffle.return_value = None
        
        # Test with a short password and large remove_count
        result = randomized_password_crippler("Short", remove_count=20)
        
        # Should still be at least 4 characters (minimum required categories)
        assert len(result) >= 4


def test_single_character_password():
    """Test with single character password"""
    with patch('random.choice') as mock_choice:
        # Mock to return predictable values for category additions
        mock_choice.side_effect = ['A', 'b', '1', '!']
        
        result = randomized_password_crippler("a")
        
        # Should be at least 12 characters long after padding and category addition
        assert len(result) >= 12


def test_very_long_password():
    """Test with very long password"""
    long_password = "A" * 100
    result = randomized_password_crippler(long_password)
    
    # Should return a valid password string
    assert isinstance(result, str)
    assert len(result) >= 12


def test_password_with_all_required_categories():
    """Test password that already has all required character categories"""
    with patch('random.choice') as mock_choice, \
         patch('random.shuffle') as mock_shuffle:
        
        # Set up predictable behavior
        mock_choice.return_value = 'X'
        mock_shuffle.return_value = None
        
        # Password already has all required categories
        result = randomized_password_crippler("Password123!")
        
        # Should still be a valid string with all categories
        assert isinstance(result, str)
        assert len(result) >= 12
        assert any(c.isupper() for c in result)
        assert any(c.islower() for c in result)
        assert any(c.isdigit() for c in result)
        assert any(c in "!@#$%^&*()-_=+[]{};:,.<>?" for c in result)

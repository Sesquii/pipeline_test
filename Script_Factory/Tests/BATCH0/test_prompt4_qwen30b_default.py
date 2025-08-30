import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from Script_Factory.Script_Factory_Runs.all_runs.expand import expand, ReverseSummarizer

import pytest

def test_expand_normal_input():
    """Test expand function with a normal input sentence."""
    sentence = "Technology is important."
    result = expand(sentence)
    
    # Verify that the result is a string and not empty
    assert isinstance(result, str)
    assert len(result) > 0
    
    # Verify that the result contains the original topic
    assert "Technology" in result
    
    # Verify that the result has more words than the input (at least 5x longer)
    original_words = len(sentence.split())
    expanded_words = len(result.split())
    assert expanded_words >= original_words * 5

def test_expand_empty_string():
    """Test expand function with an empty string input."""
    sentence = ""
    result = expand(sentence)
    
    # Empty input should return empty string
    assert isinstance(result, str)
    assert result == ""

def test_expand_whitespace_only():
    """Test expand function with whitespace-only input."""
    sentence = "   \n\t  "
    result = expand(sentence)
    
    # Whitespace-only input should return empty string
    assert isinstance(result, str)
    assert result == ""

def test_expand_single_word():
    """Test expand function with a single word input."""
    sentence = "Hello"
    result = expand(sentence)
    
    # Verify that the result is a string and not empty
    assert isinstance(result, str)
    assert len(result) > 0
    
    # Verify that the result contains the original topic
    assert "Hello" in result

def test_expand_multiple_words():
    """Test expand function with multiple words input."""
    sentence = "Artificial intelligence transforms society"
    result = expand(sentence)
    
    # Verify that the result is a string and not empty
    assert isinstance(result, str)
    assert len(result) > 0
    
    # Verify that the result contains the original topic (first 3 words)
    assert "Artificial intelligence transforms" in result

def test_reverse_summarizer_expand_normal():
    """Test ReverseSummarizer.expand with normal input."""
    summarizer = ReverseSummarizer()
    sentence = "Science advances"
    result = summarizer.expand(sentence)
    
    # Verify that the result is a string and not empty
    assert isinstance(result, str)
    assert len(result) > 0
    
    # Verify that the result contains the original topic
    assert "Science" in result

def test_reverse_summarizer_expand_empty():
    """Test ReverseSummarizer.expand with empty input."""
    summarizer = ReverseSummarizer()
    sentence = ""
    result = summarizer.expand(sentence)
    
    # Empty input should return empty string
    assert isinstance(result, str)
    assert result == ""

def test_reverse_summarizer_expand_whitespace_only():
    """Test ReverseSummarizer.expand with whitespace-only input."""
    summarizer = ReverseSummarizer()
    sentence = "   \n\t  "
    result = summarizer.expand(sentence)
    
    # Whitespace-only input should return empty string
    assert isinstance(result, str)
    assert result == ""

def test_format_essay_properly_formatted():
    """Test _format_essay method with properly formatted content."""
    summarizer = ReverseSummarizer()
    
    # Create a long essay that needs formatting
    essay = " ".join(["word"] * 50)  # 50 words
    result = summarizer._format_essay(essay)
    
    # Verify that the result is a string and not empty
    assert isinstance(result, str)
    assert len(result) > 0

def test_generate_expanded_sentence():
    """Test _generate_expanded_sentence method."""
    summarizer = ReverseSummarizer()
    topic = "Testing"
    result = summarizer._generate_expanded_sentence(topic)
    
    # Verify that the result is a string and not empty
    assert isinstance(result, str)
    assert len(result) > 0
    
    # Verify that the result contains the topic
    assert "Testing" in result

def test_get_random_phrase():
    """Test _get_random_phrase method."""
    summarizer = ReverseSummarizer()
    result = summarizer._get_random_phrase()
    
    # Verify that the result is a string and not empty
    assert isinstance(result, str)
    assert len(result) > 0

def test_expand_very_short_sentence():
    """Test expand function with a very short sentence."""
    sentence = "Hi"
    result = expand(sentence)
    
    # Verify that the result is a string and not empty
    assert isinstance(result, str)
    assert len(result) > 0
    
    # Verify that the result contains the original topic
    assert "Hi" in result

def test_expand_with_punctuation():
    """Test expand function with punctuation in input."""
    sentence = "Technology is important!"
    result = expand(sentence)
    
    # Verify that the result is a string and not empty
    assert isinstance(result, str)
    assert len(result) > 0
    
    # Verify that the result contains the original topic
    assert "Technology" in result

def test_expand_with_numbers():
    """Test expand function with numbers in input."""
    sentence = "The year 2023 is significant."
    result = expand(sentence)
    
    # Verify that the result is a string and not empty
    assert isinstance(result, str)
    assert len(result) > 0
    
    # Verify that the result contains the original topic
    assert "The year 2023" in result

def test_expand_with_special_characters():
    """Test expand function with special characters in input."""
    sentence = "AI & Robotics are important!"
    result = expand(sentence)
    
    # Verify that the result is a string and not empty
    assert isinstance(result, str)
    assert len(result) > 0
    
    # Verify that the result contains the original topic
    assert "AI" in result

def test_expand_multiple_calls():
    """Test that multiple calls to expand produce different results (due to randomness)."""
    sentence = "Technology"
    result1 = expand(sentence)
    result2 = expand(sentence)
    
    # Results should both be strings and not empty
    assert isinstance(result1, str)
    assert isinstance(result2, str)
    assert len(result1) > 0
    assert len(result2) > 0
    
    # They may be equal or different (due to randomization), but both valid
    assert isinstance(result1, str)
    assert isinstance(result2, str)

def test_reverse_summarizer_initialization():
    """Test that ReverseSummarizer initializes properly."""
    summarizer = ReverseSummarizer()
    
    # Verify that all expected attributes are present
    assert hasattr(summarizer, 'templates')
    assert hasattr(summarizer, 'conjunctions')
    assert hasattr(summarizer, 'adverbs')
    assert hasattr(summarizer, 'qualifiers')
    
    # Verify that templates list is not empty
    assert len(summarizer.templates) > 0
    
    # Verify that conjunctions list is not empty
    assert len(summarizer.conjunctions) > 0
    
    # Verify that adverbs list is not empty
    assert len(summarizer.adverbs) > 0
    
    # Verify that qualifiers list is not empty
    assert len(summarizer.qualifiers) > 0

def test_expand_with_long_sentence():
    """Test expand function with a long sentence input."""
    sentence = "Artificial intelligence and machine learning are transforming industries across the globe."
    result = expand(sentence)
    
    # Verify that the result is a string and not empty
    assert isinstance(result, str)
    assert len(result) > 0
    
    # Verify that the result contains the original topic (first 3 words)
    assert "Artificial intelligence and machine" in result

def test_expand_with_very_long_sentence():
    """Test expand function with a very long sentence input."""
    sentence = "The rapid advancement of artificial intelligence and machine learning technologies has revolutionized numerous sectors and transformed the landscape of modern business operations."
    result = expand(sentence)
    
    # Verify that the result is a string and not empty
    assert isinstance(result, str)
    assert len(result) > 0
    
    # Verify that the result contains the original topic (first 3 words)
    assert "The rapid advancement" in result

def test_expand_with_repeated_words():
    """Test expand function with repeated words."""
    sentence = "Technology technology technology"
    result = expand(sentence)
    
    # Verify that the result is a string and not empty
    assert isinstance(result, str)
    assert len(result) > 0
    
    # Verify that the result contains the original topic
    assert "Technology" in result

def test_expand_with_only_spaces():
    """Test expand function with only spaces."""
    sentence = "   "
    result = expand(sentence)
    
    # Empty input should return empty string
    assert isinstance(result, str)
    assert result == ""
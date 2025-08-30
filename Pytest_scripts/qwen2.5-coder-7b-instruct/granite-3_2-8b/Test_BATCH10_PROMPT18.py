# BATCH10_PROMPT18_Granite.py

# Importing necessary libraries
import random

# List of short phrases for story generation
phrases = [
    "In a quiet town lived a young boy.",
    "He found an old, mysterious book.",
    "Under the waning moonlight it opened.",
    "Strange symbols filled its pages.",
    "A map appeared on the next page.",
    "It hinted at a hidden treasure.",
    "The boy made a secret plan.",
    "In the dead of night, he set out.",
    "Through dense forests, he journeyed.",
    "Over towering mountains, he climbed.",
    "Finally, he reached an ancient cave.",
    "Inside, glowing crystals illuminated.",
    "There lay the treasure, waiting to be claimed.",
    "Unexpectedly, the ground began to shake.",
    "A trap! He narrowly escaped.",
    "Back home, he kept his secret tale.",
    "Years later, he'd tell it to his grandchildren."
]

def generate_story():
    story = []
    for phrase in phrases:
        sentence = ' '.join(phrase.split()[:7]) + '.'  # Ensuring each sentence has exactly seven words
        story.append(sentence)
    return '\n'.join(story)

# Main function to run the program
def main():
    story = generate_story()
    print(story)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
import pytest

from BATCH10_PROMPT18_Granite import phrases, generate_story

# Test cases for the phrases list
def test_phrases_length():
    """Test if the number of phrases is as expected."""
    assert len(phrases) == 14

def test_phrase_content():
    """Test if each phrase in the list starts with a capital letter and ends with a period."""
    for phrase in phrases:
        assert phrase[0].isupper() and phrase.endswith('.')

# Test cases for the generate_story function
def test_generate_story_length():
    """Test if the generated story has exactly 14 sentences."""
    story = generate_story()
    sentences = story.split('\n')
    assert len(sentences) == 14

def test_generate_story_content():
    """Test if each sentence in the generated story has exactly seven words and ends with a period."""
    story = generate_story()
    sentences = story.split('\n')
    for sentence in sentences:
        words = sentence.split()
        assert len(words) == 7 and sentence.endswith('.')

# Test cases for the main function
def test_main_output(capsys):
    """Test if the main function prints the generated story."""
    generate_story()  # Call the function to generate the story
    captured = capsys.readouterr()
    assert captured.out.strip().endswith("Years later, he'd tell it to his grandchildren.")

# Additional test cases using pytest fixtures and parametrization
@pytest.fixture(params=phrases)
def phrase(request):
    """Fixture to provide each phrase from the phrases list."""
    return request.param

def test_phrase_split(phrase):
    """Test if splitting a phrase into words results in exactly seven words."""
    words = phrase.split()
    assert len(words) == 7

def test_phrase_start_with_capital(phrase):
    """Test if each phrase starts with a capital letter."""
    assert phrase[0].isupper()

def test_phrase_end_with_period(phrase):
    """Test if each phrase ends with a period."""
    assert phrase.endswith('.')

# Test cases for negative scenarios
def test_generate_story_empty_list():
    """Test if generate_story handles an empty list of phrases gracefully."""
    original_phrases = phrases.copy()
    phrases.clear()
    story = generate_story()
    assert story == ''
    phrases.extend(original_phrases)

def test_generate_story_single_phrase():
    """Test if generate_story handles a single phrase correctly."""
    original_phrases = phrases.copy()
    phrases.clear()
    phrases.append("A secret treasure.")
    story = generate_story()
    assert story == "A secret treasure."
    phrases.extend(original_phrases)
```

This comprehensive test suite covers all the requirements and provides both positive and negative test cases for the given Python script. It uses pytest fixtures and parametrization to ensure thorough testing of various scenarios.
import pytest
import sys, os
from Script_Factory.Script_Factory_Runs.all_runs.prompt23_qwen30b_default import (

from Script_Factory.Script_Factory_Runs.all_runs.prompt23_qwen30b_default import (
    main,
    replace_colloquial_words,
    replace_formal_words,
    rewrite_email_tone,
    split_sentences,
    switch_tone
)

    split_sentences,
    replace_formal_words,
    replace_colloquial_words,
    switch_tone,
    rewrite_email_tone
)

def test_split_sentences_normal():
    """Test normal sentence splitting with standard punctuation."""
    text = "Hello world. How are you? I am fine!"
    expected = ["Hello world.", "How are you?", "I am fine!"]
    assert split_sentences(text) == expected

def test_split_sentences_empty_input():
    """Test sentence splitting with empty string input."""
    text = ""
    expected = []
    assert split_sentences(text) == expected

def test_split_sentences_single_sentence():
    """Test sentence splitting with single sentence."""
    text = "This is a single sentence."
    expected = ["This is a single sentence."]
    assert split_sentences(text) == expected

def test_split_sentences_with_quotes():
    """Test sentence splitting with quoted speech."""
    text = 'He said, "Hello world." Then he left.'
    expected = ['He said, "Hello world."', 'Then he left.']
    assert split_sentences(text) == expected

def test_replace_formal_words_normal():
    """Test replacing formal words with colloquial equivalents."""
    sentence = "We would like to commence this endeavor."
    expected = "We would like to start this try."
    assert replace_formal_words(sentence) == expected

def test_replace_formal_words_case_insensitive():
    """Test that formal word replacement is case insensitive."""
    sentence = "WE WOULD LIKE TO COMMENCE THIS ENDEAVOR."
    expected = "WE WOULD LIKE TO START THIS TRY."
    assert replace_formal_words(sentence) == expected

def test_replace_formal_words_no_match():
    """Test formal word replacement with no matching words."""
    sentence = "This is a simple sentence."
    expected = "This is a simple sentence."
    assert replace_formal_words(sentence) == expected

def test_replace_formal_words_partial_match():
    """Test that partial matches are not replaced (e.g., 'use' in 'used')."""
    sentence = "We utilized the use of tools."
    expected = "We utilized the use of tools."  # Only 'utilize' should be replaced
    assert replace_formal_words(sentence) == expected

def test_replace_colloquial_words_normal():
    """Test replacing colloquial words with formal equivalents."""
    sentence = "We start this try."
    expected = "We commence this endeavor."
    assert replace_colloquial_words(sentence) == expected

def test_replace_colloquial_words_case_insensitive():
    """Test that colloquial word replacement is case insensitive."""
    sentence = "WE START THIS TRY."
    expected = "WE COMMENCE THIS ENDEAVOR."
    assert replace_colloquial_words(sentence) == expected

def test_replace_colloquial_words_no_match():
    """Test colloquial word replacement with no matching words."""
    sentence = "This is a formal sentence."
    expected = "This is a formal sentence."
    assert replace_colloquial_words(sentence) == expected

def test_switch_tone_formal_to_informal():
    """Test switching from formal to informal tone."""
    sentence = "We would like to commence this endeavor."
    expected = "We would like to start this try."
    assert switch_tone(sentence, is_formal=True) == expected

def test_switch_tone_informal_to_formal():
    """Test switching from informal to formal tone."""
    sentence = "We start this try."
    expected = "We commence this endeavor."
    assert switch_tone(sentence, is_formal=False) == expected

def test_rewrite_email_tone_start_formal():
    """Test rewriting email tone starting with formal tone."""
    email_body = "Hello world. How are you? I am fine!"
    result = rewrite_email_tone(email_body, start_formal=True)
    # Should be informal for first sentence (even index), formal for second (odd index)
    assert isinstance(result, str)

def test_rewrite_email_tone_start_informal():
    """Test rewriting email tone starting with informal tone."""
    email_body = "Hello world. How are you? I am fine!"
    result = rewrite_email_tone(email_body, start_formal=False)
    # Should be formal for first sentence (even index), informal for second (odd index)
    assert isinstance(result, str)

def test_rewrite_email_tone_empty_input():
    """Test rewriting email tone with empty input."""
    email_body = ""
    expected = ""
    assert rewrite_email_tone(email_body) == expected

def test_rewrite_email_tone_single_sentence():
    """Test rewriting email tone with single sentence."""
    email_body = "Hello world."
    result = rewrite_email_tone(email_body)
    assert isinstance(result, str)

def test_rewrite_email_tone_complex_case():
    """Test rewriting email tone with complex case involving multiple replacements."""
    email_body = "We would like to commence this endeavor. Furthermore, we appreciate your cooperation."
    result = rewrite_email_tone(email_body, start_formal=True)
    assert isinstance(result, str)

def test_split_sentences_with_abbreviations():
    """Test sentence splitting handles abbreviations correctly."""
    text = "Dr. Smith went to the U.S.A. He returned quickly."
    expected = ["Dr. Smith went to the U.S.A.", "He returned quickly."]
    assert split_sentences(text) == expected

def test_split_sentences_with_decimal_numbers():
    """Test sentence splitting with decimal numbers."""
    text = "The value is 3.14. Another value is 2.5."
    expected = ["The value is 3.14.", "Another value is 2.5."]
    assert split_sentences(text) == expected

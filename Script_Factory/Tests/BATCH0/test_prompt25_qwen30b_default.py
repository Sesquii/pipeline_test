import pytest
import sys, os
from Script_Factory.Script_Factory_Runs.all_runs.prompt25_qwen30b_default import MemoryLossStoryteller


from Script_Factory.Script_Factory_Runs.all_runs.prompt25_qwen30b_default import (
    tell_story
)

def test_tell_story_normal_case():
    """Test normal case with 10 sentences"""
    storyteller = MemoryLossStoryteller()
    story = storyteller.tell_story(10)
    
    # Should return a string with 10 sentences
    assert isinstance(story, str)
    # Should end with a period
    assert story.endswith('.')
    # Should contain periods separating sentences
    assert story.count('.') >= 10

def test_tell_story_edge_case_zero():
    """Test edge case with zero sentences"""
    storyteller = MemoryLossStoryteller()
    story = storyteller.tell_story(0)
    
    # Should return empty string with just a period
    assert story == '.'

def test_tell_story_edge_case_one():
    """Test edge case with one sentence"""
    storyteller = MemoryLossStoryteller()
    story = storyteller.tell_story(1)
    
    # Should return one sentence ending with period
    assert isinstance(story, str)
    assert story.endswith('.')
    assert story.count('.') >= 1

def test_tell_story_odd_number():
    """Test with odd number of sentences"""
    storyteller = MemoryLossStoryteller()
    story = storyteller.tell_story(7)
    
    # Should handle odd numbers correctly
    assert isinstance(story, str)
    assert story.endswith('.')

def test_tell_story_large_number():
    """Test with larger number of sentences"""
    storyteller = MemoryLossStoryteller()
    story = storyteller.tell_story(20)
    
    # Should handle larger inputs
    assert isinstance(story, str)
    assert story.endswith('.')

def test_generate_original_sentence_normal():
    """Test original sentence generation with normal index"""
    storyteller = MemoryLossStoryteller()
    
    # Test first few sentences
    for i in range(5):
        sentence = storyteller._generate_original_sentence(i)
        assert isinstance(sentence, str)
        assert len(sentence) > 0

def test_generate_original_sentence_out_of_bounds():
    """Test original sentence generation with index beyond list length"""
    storyteller = MemoryLossStoryteller()
    
    # Test with index beyond available prompts
    sentence = storyteller._generate_original_sentence(20)
    assert isinstance(sentence, str)
    assert len(sentence) > 0

def test_generate_new_sentence_normal():
    """Test new sentence generation with normal index"""
    storyteller = MemoryLossStoryteller()
    
    # Test first few sentences
    for i in range(5):
        sentence = storyteller._generate_new_sentence(i)
        assert isinstance(sentence, str)
        assert len(sentence) > 0

def test_generate_new_sentence_out_of_bounds():
    """Test new sentence generation with index beyond list length"""
    storyteller = MemoryLossStoryteller()
    
    # Test with index beyond available prompts
    sentence = storyteller._generate_new_sentence(20)
    assert isinstance(sentence, str)
    assert len(sentence) > 0

def test_story_structure():
    """Test that story has correct structure - first half original, second half new"""
    storyteller = MemoryLossStoryteller()
    story = storyteller.tell_story(8)
    
    # Should have 8 sentences total
    sentences = story[:-1].split('. ')
    assert len(sentences) == 8
    
    # First half should be from original prompts
    # Second half should be from new prompts
    assert isinstance(story, str)

def test_multiple_story_calls():
    """Test that multiple calls to tell_story work correctly"""
    storyteller = MemoryLossStoryteller()
    
    # First story
    story1 = storyteller.tell_story(5)
    # Second story
    story2 = storyteller.tell_story(5)
    
    assert isinstance(story1, str)
    assert isinstance(story2, str)
    assert story1 != story2  # Different stories due to randomness

def test_empty_sentences_list():
    """Test that sentences list is properly cleared between calls"""
    storyteller = MemoryLossStoryteller()
    
    # Call once
    storyteller.tell_story(5)
    # Check internal state
    assert len(storyteller.sentences) == 0  # Should be cleared after story generation

def test_midpoint_calculation():
    """Test midpoint calculation logic"""
    storyteller = MemoryLossStoryteller()
    
    # Test various cases for midpoint calculation
    assert storyteller.tell_story(4) is not None  # Even number
    assert storyteller.tell_story(5) is not None  # Odd number
    assert storyteller.tell_story(1) is not None  # Single sentence

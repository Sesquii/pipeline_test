import pytest
import sys, os
from typing import List
from Script_Factory.Script_Factory_Runs.all_runs.prompt16_qwen30b_default import generate_excuses


from Script_Factory.Script_Factory_Runs.all_runs.prompt16_qwen30b_default import (
    generate_excuses
)

def test_generate_excuses_normal_case():
    """
    Test normal case with valid initial excuse and positive depth
    """
    initial = "I couldn't complete the task"
    depth = 3
    result = generate_excuses(initial, depth)
    
    # Should return a list with at least one excuse
    assert isinstance(result, List)
    assert len(result) > 0
    assert result[0] == initial

def test_generate_excuses_zero_depth():
    """
    Test edge case with zero depth - should return empty list
    """
    initial = "I couldn't complete the task"
    depth = 0
    result = generate_excuses(initial, depth)
    
    # Should return empty list when depth is 0
    assert isinstance(result, List)
    assert len(result) == 0

def test_generate_excuses_negative_depth():
    """
    Test edge case with negative depth - should return empty list
    """
    initial = "I couldn't complete the task"
    depth = -1
    result = generate_excuses(initial, depth)
    
    # Should return empty list when depth is negative
    assert isinstance(result, List)
    assert len(result) == 0

def test_generate_excuses_empty_initial():
    """
    Test edge case with empty initial excuse
    """
    initial = ""
    depth = 2
    result = generate_excuses(initial, depth)
    
    # Should handle empty initial string gracefully
    assert isinstance(result, List)
    assert len(result) > 0

def test_generate_excuses_single_depth():
    """
    Test case with depth of 1 - should return only the initial excuse
    """
    initial = "I couldn't complete the task"
    depth = 1
    result = generate_excuses(initial, depth)
    
    # Should return only the initial excuse when depth is 1
    assert isinstance(result, List)
    assert len(result) == 1
    assert result[0] == initial

def test_generate_excuses_with_different_initial():
    """
    Test with different initial excuse that doesn't contain "I couldn't"
    """
    initial = "The project was delayed"
    depth = 2
    result = generate_excuses(initial, depth)
    
    # Should handle initial excuses without "I couldn't" pattern
    assert isinstance(result, List)
    assert len(result) > 0

def test_generate_excuses_multiple_calls():
    """
    Test that multiple calls produce different results due to randomization
    """
    initial = "I couldn't complete the task"
    depth = 3
    result1 = generate_excuses(initial, depth)
    result2 = generate_excuses(initial, depth)
    
    # Multiple calls should produce lists (may be different due to randomness)
    assert isinstance(result1, List)
    assert isinstance(result2, List)
    assert len(result1) > 0
    assert len(result2) > 0

import pytest
import sys, os
from Script_Factory.Script_Factory_Runs.all_runs.prompt24_qwen30b_default import MoodRNG


from Script_Factory.Script_Factory_Runs.all_runs.prompt24_qwen30b_default import (
    randint,
    random
)

def test_mood_rng_initialization_valid_moods():
    """
    Test that MoodRNG initializes correctly with valid moods.
    This tests normal, expected inputs for the constructor.
    """
    for mood in ['happy', 'sad', 'angry', 'calm']:
        rng = MoodRNG(mood)
        assert rng.mood == mood

def test_mood_rng_initialization_invalid_mood():
    """
    Test that MoodRNG raises ValueError for invalid moods.
    This tests error handling with unexpected inputs.
    """
    with pytest.raises(ValueError):
        MoodRNG('excited')
    
    with pytest.raises(ValueError):
        MoodRNG('neutral')

def test_mood_rng_randint_normal_case():
    """
    Test that randint produces random integers within specified bounds.
    This tests normal, expected inputs for the randint method.
    """
    rng = MoodRNG('happy')
    # Generate multiple numbers to ensure randomness
    for _ in range(10):
        num = rng.randint(1, 10)
        assert 1 <= num <= 10

def test_mood_rng_randint_edge_case_zero():
    """
    Test that randint works correctly with zero as bounds.
    This tests an edge case with zero values.
    """
    rng = MoodRNG('sad')
    # Test with zero bounds
    num = rng.randint(0, 5)
    assert 0 <= num <= 5

def test_mood_rng_randint_negative_numbers():
    """
    Test that randint works correctly with negative numbers.
    This tests an edge case with negative values.
    """
    rng = MoodRNG('angry')
    # Test with negative bounds
    num = rng.randint(-10, -1)
    assert -10 <= num <= -1

def test_mood_rng_randint_same_bounds():
    """
    Test that randint works correctly when both bounds are the same.
    This tests an edge case with identical bounds.
    """
    rng = MoodRNG('calm')
    # Test with identical bounds
    num = rng.randint(5, 5)
    assert num == 5

def test_mood_rng_random_normal_case():
    """
    Test that random produces random floating point numbers in [0.0, 1.0).
    This tests normal, expected inputs for the random method.
    """
    rng = MoodRNG('happy')
    # Generate multiple numbers to ensure randomness
    for _ in range(10):
        num = rng.random()
        assert 0.0 <= num < 1.0

def test_mood_rng_deterministic_behavior():
    """
    Test that the same mood produces deterministic sequences.
    This verifies that the random number generator is seeded correctly.
    """
    # Create two RNGs with the same mood
    rng1 = MoodRNG('happy')
    rng2 = MoodRNG('happy')
    
    # Generate same sequence of numbers
    numbers1 = [rng1.randint(1, 100) for _ in range(5)]
    numbers2 = [rng2.randint(1, 100) for _ in range(5)]
    
    assert numbers1 == numbers2

def test_mood_rng_different_moods_different_sequences():
    """
    Test that different moods produce different sequences.
    This ensures that each mood has its own distinct seed.
    """
    rng_happy = MoodRNG('happy')
    rng_sad = MoodRNG('sad')
    
    # Generate first few numbers from each
    happy_numbers = [rng_happy.randint(1, 100) for _ in range(3)]
    sad_numbers = [rng_sad.randint(1, 100) for _ in range(3)]
    
    # Sequences should be different (very unlikely to be the same)
    assert happy_numbers != sad_numbers

def test_mood_rng_random_float_range():
    """
    Test that random method produces values within expected range.
    This is an edge case test for floating point number generation.
    """
    rng = MoodRNG('calm')
    
    # Test multiple values
    for _ in range(20):
        num = rng.random()
        assert isinstance(num, float)
        assert 0.0 <= num < 1.0

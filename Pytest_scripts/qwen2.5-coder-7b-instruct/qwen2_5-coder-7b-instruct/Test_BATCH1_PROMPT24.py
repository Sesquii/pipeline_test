import random

class MoodRNG:
    """
    A class to generate pseudo-random numbers based on an emotional state.
    
    Attributes:
        mood (str): The current emotional state ('happy', 'sad', 'angry', 'calm').
        seed (int): The seed used for the random number generator.
    """
    
    MOOD_SEEDS = {
        'happy': 42,
        'sad': 99,
        'angry': 13,
        'calm': 7
    }
    
    def __init__(self, mood):
        """
        Initialize the MoodRNG instance with a specific emotional state.
        
        Args:
            mood (str): The emotional state to set ('happy', 'sad', 'angry', 'calm').
            
        Raises:
            ValueError: If the provided mood is not valid.
        """
        if mood not in self.MOOD_SEEDS:
            raise ValueError("Invalid mood. Choose from 'happy', 'sad', 'angry', 'calm'.")
        
        self.mood = mood
        self.seed = self.MOOD_SEEDS[mood]
        random.seed(self.seed)
    
    def randint(self, a, b):
        """
        Return a random integer between a and b (inclusive).
        
        Args:
            a (int): The lower bound of the range.
            b (int): The upper bound of the range.
            
        Returns:
            int: A pseudo-random integer in [a, b].
        """
        return random.randint(a, b)
    
    def random(self):
        """
        Return a random float between 0 and 1 (exclusive).
        
        Returns:
            float: A pseudo-random float in [0, 1).
        """
        return random.random()

if __name__ == "__main__":
    moods = ['happy', 'sad', 'angry', 'calm']
    rngs = {mood: MoodRNG(mood) for mood in moods}
    
    for mood, rng in rngs.items():
        print(f"\nMood: {mood}")
        for _ in range(5):
            print(f"  Random integer (1-100): {rng.randint(1, 100)}")
```

This Python module defines a `MoodRNG` class that generates pseudo-random numbers based on an emotional state. The mood-to-seed mapping is done using a fixed dictionary, and the seed initializes Python's `random` module to ensure reproducibility for the same mood. The demo block creates instances for each mood and prints five random integers from 1 to 100 for each instance.

# ===== GENERATED TESTS =====
```python
import pytest

# Original script remains unchanged as per requirement 1.

class TestMoodRNG:
    """
    A class containing tests for the MoodRNG class.
    """

    @pytest.fixture(params=['happy', 'sad', 'angry', 'calm'])
    def mood_rng(self, request):
        """
        Fixture to create a MoodRNG instance for each mood.
        
        Args:
            request (FixtureRequest): The pytest fixture request object.
            
        Returns:
            MoodRNG: A MoodRNG instance initialized with the current mood.
        """
        return MoodRNG(request.param)

    def test_init_valid_mood(self, mood_rng):
        """
        Test that a valid mood initializes the MoodRNG instance correctly.
        
        Args:
            mood_rng (MoodRNG): The MoodRNG instance to test.
            
        Raises:
            AssertionError: If the initialization is incorrect.
        """
        assert isinstance(mood_rng, MoodRNG)
        assert mood_rng.mood in ['happy', 'sad', 'angry', 'calm']
        assert mood_rng.seed == MoodRNG.MOOD_SEEDS[mood_rng.mood]

    def test_init_invalid_mood(self):
        """
        Test that an invalid mood raises a ValueError.
        
        Raises:
            AssertionError: If the exception is not raised.
        """
        with pytest.raises(ValueError, match="Invalid mood. Choose from 'happy', 'sad', 'angry', 'calm'."):
            MoodRNG('unknown')

    def test_randint_valid_range(self, mood_rng):
        """
        Test that randint returns a valid integer within the specified range.
        
        Args:
            mood_rng (MoodRNG): The MoodRNG instance to test.
            
        Raises:
            AssertionError: If the returned value is out of range or not an integer.
        """
        for _ in range(10):
            result = mood_rng.randint(1, 100)
            assert isinstance(result, int)
            assert 1 <= result <= 100

    def test_randint_invalid_range(self, mood_rng):
        """
        Test that randint raises a ValueError with invalid ranges.
        
        Args:
            mood_rng (MoodRNG): The MoodRNG instance to test.
            
        Raises:
            AssertionError: If the exception is not raised.
        """
        with pytest.raises(ValueError, match="integers are not allowed"):
            mood_rng.randint(100, 1)

    def test_random_valid_value(self, mood_rng):
        """
        Test that random returns a valid float within the range [0, 1).
        
        Args:
            mood_rng (MoodRNG): The MoodRNG instance to test.
            
        Raises:
            AssertionError: If the returned value is out of range or not a float.
        """
        for _ in range(10):
            result = mood_rng.random()
            assert isinstance(result, float)
            assert 0 <= result < 1

if __name__ == "__main__":
    pytest.main()
```

This test suite includes comprehensive tests for the `MoodRNG` class. It uses pytest fixtures and parametrization to ensure that each test case is run for all valid moods. The tests cover initialization, random number generation with valid and invalid ranges, and type checking of the returned values.
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
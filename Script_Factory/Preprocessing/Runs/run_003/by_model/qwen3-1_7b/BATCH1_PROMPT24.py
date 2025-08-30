```python
import random

mood_seeds = {
    'happy': 123,
    'sad': 456,
    'angry': 789,
    'calm': 101
}

class MoodRNG:
    """A random number generator based on mood.
    
    Attributes:
        mood: The current emotional state (one of 'happy', 'sad', 'angry', 'calm').
        seed: The seed value used to initialize the random module.
    """
    
    def __init__(self, mood):
        """Initialize the MoodRNG with a given mood."""
        if mood not in {'happy', 'sad', 'angry', 'calm'}:
            raise ValueError("Mood must be one of: happy, sad, angry, calm")
        self.mood = mood
        self.seed = mood_seeds[self.mood]
        random.seed(self.seed)
    
    def randint(self, a, b):
        """Return a random integer in [a, b]."""
        return random.randint(a, b)
    
    def random(self):
        """Return a float in [0, 1)."""
        return random.random()

if __name__ == "__main__":
    # Create instances for each mood
    happy_rng = MoodRNG('happy')
    sad_rng = MoodRNG('sad')
    angry_rng = MoodRNG('angry')
    calm_rng = MoodRNG('calm')
    
    # Print five random integers (1–100) from each instance
    for rng in [happy_rng, sad_rng, angry_rng, calm_rng]:
        for _ in range(5):
            print(rng.randint(1, 100))
            print(rng.random())
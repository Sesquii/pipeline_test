import random

class MoodRNG:
    """
    A mood-based random number generator that produces deterministic sequences 
    based on the selected emotional state.
    """

    # Mapping of moods to fixed seeds for reproducibility
    MOOD_SEEDS = {
        'happy': 42,
        'sad': 13,
        'angry': 99,
        'calm': 7
    }

    def __init__(self, mood):
        """
        Initialize the MoodRNG with a specific mood.

        Args:
            mood (str): The emotional state to use for seeding the RNG.
                       Must be one of {'happy', 'sad', 'angry', 'calm'}.

        Raises:
            ValueError: If the provided mood is not valid.
        """
        if mood not in self.MOOD_SEEDS:
            raise ValueError(f"Invalid mood: {mood}. Must be one of {set(self.MOOD_SEEDS.keys())}")
        self.mood = mood
        random.seed(self.MOOD_SEEDS[mood])

    def randint(self, a, b):
        """
        Return a random integer N such that a <= N <= b.

        Args:
            a (int): Lower bound of the range.
            b (int): Upper bound of the range.

        Returns:
            int: Random integer within the specified range.
        """
        return random.randint(a, b)

    def random(self):
        """
        Return the next random floating point number in the range [0.0, 1.0).

        Returns:
            float: Random float between 0 (inclusive) and 1 (exclusive).
        """
        return random.random()

if __name__ == "__main__":
    # Demo block to showcase the MoodRNG functionality
    moods = ['happy', 'sad', 'angry', 'calm']

    for mood in moods:
        rng = MoodRNG(mood)
        print(f"\nMood: {mood}")
        print("Five random integers between 1 and 100:")
        for _ in range(5):
            print(rng.randint(1, 100))
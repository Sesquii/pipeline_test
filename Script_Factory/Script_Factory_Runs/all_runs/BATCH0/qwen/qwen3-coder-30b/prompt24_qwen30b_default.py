import random

class MoodRNG:
    """
    A mood-based random number generator that produces deterministic sequences
    based on emotional states.
    """

    MOODS = {'happy', 'sad', 'angry', 'calm'}
    MOOD_SEEDS = {
        'happy': 42,
        'sad': 123,
        'angry': 456,
        'calm': 789
    }

    def __init__(self, mood):
        """
        Initialize the MoodRNG with a specified mood.

        :param mood: A string representing the emotional state.
                     Must be one of {'happy', 'sad', 'angry', 'calm'}.
        :raises ValueError: If the mood is not in the valid set.
        """
        if mood not in self.MOODS:
            raise ValueError(f"Mood must be one of {self.MOODS}")
        self.mood = mood
        random.seed(self.MOOD_SEEDS[mood])

    def randint(self, a, b):
        """
        Return a random integer N such that a <= N <= b.

        :param a: Lower bound (inclusive).
        :param b: Upper bound (inclusive).
        :return: A random integer in the range [a, b].
        """
        return random.randint(a, b)

    def random(self):
        """
        Return the next random floating point number in the range [0.0, 1.0).

        :return: A random float in the range [0.0, 1.0).
        """
        return random.random()


if __name__ == "__main__":
    for mood in ['happy', 'sad', 'angry', 'calm']:
        rng = MoodRNG(mood)
        print(f"{mood.capitalize()} mood:")
        for _ in range(5):
            print(rng.randint(1, 100))
        print()

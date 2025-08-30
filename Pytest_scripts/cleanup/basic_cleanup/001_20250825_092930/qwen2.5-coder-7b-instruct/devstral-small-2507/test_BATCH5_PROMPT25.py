import random

class Philosopher:
    def __init__(self):
        # Collection of philosophical phrases and statements
        self.phrases = [
            "The nature of {topic} is inherently subjective",
            "To truly understand {topic}, one must first question the very concept itself",
            "In the grand tapestry of existence, {topic} represents but a single thread",
            "Is {topic} an illusion created by our collective consciousness?",
            "The pursuit of {topic} may be as futile as chasing shadows in the dark",
            "{topic} is like a river that flows through us all, shaping our thoughts and actions",
            "Perhaps {topic} does not exist independently but is a construct of our minds",
            "If we could peer into the abyss of {topic}, would it stare back at us?",
            "The more we explore {topic}, the less we seem to comprehend its essence"
        ]

    def ponder_on(self, topic: str) -> str:
        """
        Generates a philosophical treatise on the given topic.

        Args:
            topic (str): The subject to ponder upon (e.g., "life", "truth", "knowledge")

        Returns:
            str: A rambling philosophical discourse
        """
        treatise = []
        num_paragraphs = random.randint(3, 5)

        for _ in range(num_paragraphs):
            paragraph_length = random.randint(2, 4)
            paragraph = []

            for _ in range(paragraph_length):
                phrase = random.choice(self.phrases).format(topic=topic)
                paragraph.append(phrase)

            treatise.append(" ".join(paragraph))

        return "\n\n".join(treatise)

if __name__ == "__main__":
    # Example usage
    philosopher = Philosopher()
    topic = "life"
    wisdom = philosopher.ponder_on(topic)
    print(wisdom)

# ===== GENERATED TESTS =====
import pytest

# Original code remains unchanged here

class TestPhilosopher:
    @pytest.fixture
    def philosopher(self):
        return Philosopher()

    def test_ponder_on_positive(self, philosopher):
        """
        Tests that ponder_on function generates a treatise with the correct number of paragraphs and phrases.
        """
        topic = "life"
        wisdom = philosopher.ponder_on(topic)
        paragraphs = wisdom.split("\n\n")
        assert 3 <= len(paragraphs) <= 5

        for paragraph in paragraphs:
            phrases = paragraph.split(" ")
            assert 2 <= len(phrases) <= 4

    def test_ponder_on_negative(self, philosopher):
        """
        Tests that ponder_on function raises a TypeError when non-string input is provided.
        """
        with pytest.raises(TypeError):
            philosopher.ponder_on(123)

    @pytest.mark.parametrize("topic", ["", " ", None])
    def test_ponder_on_invalid_topic(self, philosopher, topic):
        """
        Tests that ponder_on function handles invalid topics gracefully.
        """
        wisdom = philosopher.ponder_on(topic)
        assert wisdom == ""

if __name__ == "__main__":
    pytest.main()

This test suite includes:
- A fixture to create a `Philosopher` instance for each test case
- Positive tests to ensure the function generates treatises with the correct structure
- Negative tests to check that the function handles invalid input types and empty strings gracefully
- Parametrization to test multiple invalid topic values
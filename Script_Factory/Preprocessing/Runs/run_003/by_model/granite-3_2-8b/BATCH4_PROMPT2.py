import random
from typing import List


def generate_poem(data: List[int], lines: int = 5) -> str:
    """
    Generates an abstract poem based on a list of integers.

    Each line's length corresponds to its data point, and words are chosen randomly from a predefined list.

    :param data: The list of integers to base the poem on.
    :param lines: Number of lines in the poem (default 5).
    :return: A string representing the generated poem.
    """
    if not data:
        return "No data provided."

    # List of possible words for each syllable count
    word_options = {
        1: ["star", "sun", "moon", "dream", "sky"],
        2: ["whisper", "shadow", "glow", "mystery", "dance"],
        3: ["echo", "silence", "flight", "legend", "serenade"],
        4: ["eternal", "twilight", "harmony", "riddle", "ballad"]
    }

    poem = []
    for i, value in enumerate(data):
        # Randomly select a line length based on the data point
        line_length = random.randint(1, value)
        
        # Generate words until we reach the desired line length
        line = ' '.join(random.choice(word_options[len(w)]) for w in [i*line_length] for i in range(value))
        poem.append(line)

    return '\n'.join(poem[:lines])


def main():
    """Entry point of the script."""
    data = [10, 5, 8, 3, 7]  # Example data series
    poem = generate_poem(data, lines=4)
    print(poem)


if __name__ == "__main__":
    main()
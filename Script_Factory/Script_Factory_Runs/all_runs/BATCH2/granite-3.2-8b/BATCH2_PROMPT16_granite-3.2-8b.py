#!/usr/bin/env python3

import random
from typing import List


def generate_poem(data: List[float], min_syllables: int = 4, max_syllables: int = 8) -> str:
    """Generates an abstract poem based on a list of numbers.

    The line length is determined by the number's absolute value.
    Word choice and repetition are randomized within a specified syllable range.

    Args:
        data (List[float]): List of numerical values to base the poem on.
        min_syllables (int): Minimum syllables per line. Default is 4.
        max_syllables (int): Maximum syllables per line. Default is 8.

    Returns:
        str: The generated abstract poem.
    """
    # Syllable lists for common English words
    one_syllable = ["the", "and", "of", "in", "to", "a", "is"]
    two_syllables = ["above", "below", "this", "that", "when", "where"]
    three_syllables = ["together", "separate", "change", "same", "new", "old"]
    four_syllables = ["beyond", "different", "understand", "believe", "create", "feel"]

    poem_lines = []

    for value in data:
        line_length = int(abs(value) * 5 + random.randint(-2, 2))  # Adjusts length based on value magnitude

        line = ""
        while len(line) < line_length:
            syllable_count = random.choice([1, 2, 3, 4])
            words = [random.choice(one_syllable), random.choice(two_syllables)][syllable_count - 1]
            if len(words) <= line_length:
                line += words + " "

        poem_lines.append(line.strip())

    return "\n".join(poem_lines)


def main():
    """Entry point of the program."""
    data = [2.5, -3.8, 0.1, 4.9]  # Sample dataset
    poem = generate_poem(data)
    print(poem)


if __name__ == "__main__":
    main()
# BATCH8_PROMPT11_Granite.py

import re
from collections import Counter


def read_file(filepath):
    """Reads content from a given file path."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def word_counter(text, positive_words):
    """Counts words in the text and exaggerates counts for positive words."""
    # Convert all to lower case for uniformity
    text = text.lower()

    # Find all words using regex, ignore punctuation
    words = re.findall(r'\b\w+\b', text)

    word_counts = Counter(words)

    # Exaggerate count for positive words
    exaggerated_counts = {}
    for word in positive_words:
        if word in word_counts:
            exaggerated_counts[word] = 100 * word_counts[word]
        else:
            exaggerated_counts[word] = word_counts.get(word, 0)

    return exaggerated_counts


def print_results(counter):
    """Prints the dictionary of word counts."""
    for word, count in counter.items():
        print(f"{word}: {count}")


def main():
    # Define positive words list
    POSITIVE_WORDS = ['love', 'happy', 'great']

    # Read file content
    text = read_file('input.txt')

    # Count words and exaggerate for positive ones
    word_counts = word_counter(text, POSITIVE_WORDS)

    # Print the results
    print_results(word_counts)


if __name__ == "__main__":
    main()
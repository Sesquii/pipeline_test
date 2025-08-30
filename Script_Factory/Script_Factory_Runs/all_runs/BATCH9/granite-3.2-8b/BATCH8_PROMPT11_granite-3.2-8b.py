# BATCH8_PROMPT11_Granite.py

import sys
from collections import Counter

POSITIVE_WORDS = {'love', 'happy', 'great'}


def read_file(filepath):
    """Reads a file and returns its content as a single string."""
    with open(filepath, 'r') as file:
        return file.read()


def count_words(text):
    """Counts the words in the given text and returns a dictionary of counts."""
    # Split the text into words and count their occurrences
    word_counts = Counter(text.split())
    
    # Exaggerate counts for positive words
    exaggerated_counts = {word: 100 * count if word in POSITIVE_WORDS else count
                          for word, count in word_counts.items()}
    
    return exaggerated_counts


def print_word_counts(word_counts):
    """Prints the word counts in a formatted manner."""
    for word, count in sorted(word_counts.items()):
        print(f"{word}: {count}")


def main(filepath):
    """Entry point of the program."""
    text = read_file(filepath)
    word_counts = count_words(text)
    print_word_counts(word_counts)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python BATCH8_PROMPT11_Granite.py <path_to_file>")
    else:
        main(sys.argv[1])
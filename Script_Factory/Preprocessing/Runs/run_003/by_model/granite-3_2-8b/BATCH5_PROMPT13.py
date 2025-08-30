import sys
from collections import Counter

# List of common words to exaggerate
COMMON_WORDS = ['the', 'a', 'an']
EXAGGERATION_FACTOR = 100


def count_words(file_path):
    """Count words in a text file, exaggerating common ones."""
    with open(file_path, 'r') as file:
        text = file.read().lower()

    # Split text into words and count occurrences
    word_counts = Counter(text.split())

    # Exaggerate counts for common words
    for word in COMMON_WORDS:
        if word in word_counts:
            word_counts[word] *= EXAGGERATION_FACTOR

    return word_counts


def print_word_counts(word_counts):
    """Print the word count dictionary."""
    for word, count in sorted(word_counts.items()):
        print(f'{word}: {count}')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python exaggerated_word_counter.py <path_to_text_file>")
    else:
        file_path = sys.argv[1]
        word_counts = count_words(file_path)
        print_word_counts(word_counts)
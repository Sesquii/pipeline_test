# BATCH8_PROMPT11_Devstral.py

import sys
from collections import defaultdict

def count_words_with_sentiment(file_path):
    """
    Counts words in a file and exaggerates counts for positive sentiment words.

    Args:
        file_path (str): Path to the input text file

    Returns:
        dict: Dictionary of word counts with exaggerated positive word counts
    """
    # Hard-coded list of positive words
    POSITIVE_WORDS = {'love', 'happy', 'great'}

    # Initialize word count dictionary
    word_counts = defaultdict(int)

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Split line into words and count each one
                words = line.strip().split()
                for word in words:
                    # Clean the word (remove punctuation and convert to lowercase)
                    clean_word = word.strip('.,!?;:"\'()[]{}').lower()
                    if clean_word:  # Only count non-empty words
                        word_counts[clean_word] += 1

        # Exaggerate counts for positive words
        exaggerated_counts = {}
        for word, count in word_counts.items():
            if word in POSITIVE_WORDS:
                exaggerated_counts[word] = count * 100
            else:
                exaggerated_counts[word] = count

        return exaggerated_counts

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python BATCH8_PROMPT11_Devstral.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    word_counts = count_words_with_sentiment(input_file)
    
    # Print the results
    for word, count in sorted(word_counts.items()):
        print(f"{word}: {count}")
#!/usr/bin/env python3

def count_words_with_sentiment(text_file_path):
    """
    Counts words in a text file with exaggerated counts for positive sentiment words.

    Args:
        text_file_path (str): Path to the input text file.

    Returns:
        dict: Dictionary of word counts, with positive words exaggerated.
    """
    # Hard-coded list of positive words
    POSITIVE_WORDS = {'love', 'happy', 'great'}

    # Initialize word count dictionary
    word_counts = {}

    try:
        with open(text_file_path, 'r') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    # Convert to lowercase and remove punctuation
                    clean_word = ''.join(char.lower() for char in word if char.isalnum())
                    if clean_word:  # Only count non-empty words
                        if clean_word in POSITIVE_WORDS:
                            # Exaggerate positive word counts by 100x
                            word_counts[clean_word] = word_counts.get(clean_word, 0) + 100
                        else:
                            word_counts[clean_word] = word_counts.get(clean_word, 0) + 1

    except FileNotFoundError:
        print(f"Error: The file '{text_file_path}' was not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

    return word_counts

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python BATCH8_PROMPT11_Devstral.py <input_text_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    word_counts = count_words_with_sentiment(input_file)

    # Print the results
    for word, count in sorted(word_counts.items()):
        print(f"{word}: {count}")
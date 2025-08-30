# BATCH8_PROMPT13_Granite.py

import re
from collections import Counter


def is_palindrome(word):
    """Check if a word is a palindrome."""
    return word == word[::-1]


def exaggerate_count(count):
    """Exaggerate the count for palindromes by 1000 times."""
    return count * 1000 if is_palindrome(str(count)) else count


def process_file(filepath):
    """Read a text file, count words and exaggerate palindrome counts."""
    with open(filepath, 'r') as f:
        text = f.read().lower()  # Convert to lowercase for case-insensitive counting

    # Find all words using regex to handle punctuation
    words = re.findall(r'\b\w+\b', text)
    
    word_counter = Counter(words)
    
    exaggerated_counts = {word: exaggerate_count(count) for word, count in word_counter.items()}

    return exaggerated_counts


def main():
    """Entry point of the script."""
    if __name__ == "__main__":
        # Replace 'example.txt' with the path to your text file
        filepath = 'example.txt'
        word_counts = process_file(filepath)
        
        for word, count in word_counts.items():
            print(f"{word}: {count}")


if __name__ == "__main__":
    main()
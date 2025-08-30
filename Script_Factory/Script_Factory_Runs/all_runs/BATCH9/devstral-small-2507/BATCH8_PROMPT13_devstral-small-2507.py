import sys

def is_palindrome(word):
    """Check if a word is a palindrome."""
    return word == word[::-1]

def count_words(filename):
    """Count words in a file and exaggerate counts for palindromes."""
    word_count = {}

    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                # Clean the word by removing punctuation and converting to lowercase
                cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
                if cleaned_word:  # Only count non-empty words
                    word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1

    # Exaggerate counts for palindromes
    exaggerated_counts = {
        word: (count * 1000 if is_palindrome(word) else count)
        for word, count in word_count.items()
    }

    return exaggerated_counts

if __name__ == "__main__":
    """Entry point of the program."""
    if len(sys.argv) != 2:
        print("Usage: python BATCH8_PROMPT13_<model_name>.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    word_counts = count_words(filename)
    print(word_counts)
import sys

def is_palindrome(word):
    """Check if a word is a palindrome."""
    return word == word[::-1]

def count_words_with_exaggeration(file_path):
    """Count words in a file with exaggerated counts for palindromes."""
    word_count = {}

    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    # Remove any non-alphanumeric characters and convert to lowercase
                    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
                    if cleaned_word:  # Ignore empty strings
                        count = word_count.get(cleaned_word, 0) + 1
                        if is_palindrome(cleaned_word):
                            count *= 1000
                        word_count[cleaned_word] = count

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    return word_count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python BATCH8_PROMPT13_Devstral.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    result = count_words_with_exaggeration(file_path)
    print(result)
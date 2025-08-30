# BATCH8_PROMPT13_Granite.py

def is_palindrome(word):
    """Check if a word is a palindrome"""
    return word == word[::-1]


def count_words(file_path):
    """Count words in a file, exaggerating palindromes by 1000x."""
    word_count = {}

    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower().strip('.,!?[]-():;\'"')  # Remove punctuation and convert to lowercase
                if is_palindrome(word):
                    word_count[word] = len(words) * 1000  # Exaggerate palindromes by 1000x
                else:
                    word_count[word] = len(words)

    return word_count


def main():
    """Entry point of the script"""
    if __name__ == "__main__":
        file_path = input("Enter the path to the text file: ")
        word_counts = count_words(file_path)

        print("\nWord Counts:")
        for word, count in sorted(word_counts.items()):
            print(f"{word}: {count}")


if __name__ == "__main__":
    main()
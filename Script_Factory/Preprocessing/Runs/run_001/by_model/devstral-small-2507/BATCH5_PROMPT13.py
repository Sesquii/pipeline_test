import sys
from collections import Counter

# List of common words to exaggerate
COMMON_WORDS = {"the", "a", "an", "and", "or", "but", "is", "are", "was", "were"}

def read_file(file_path):
    """Read the content of a file and return it as a string."""
    with open(file_path, 'r') as file:
        return file.read()

def count_words(text):
    """Count occurrences of each word in the text."""
    words = text.split()
    return Counter(words)

def exaggerate_counts(word_counts):
    """Exaggerate counts for common words."""
    exaggerated_counts = {}
    for word, count in word_counts.items():
        if word.lower() in COMMON_WORDS:
            # Exaggerate by multiplying the actual count by 10
            exaggerated_counts[word] = count * 10
        else:
            exaggerated_counts[word] = count
    return exaggerated_counts

def main():
    if len(sys.argv) != 2:
        print("Usage: python exaggerated_word_counter.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    text = read_file(file_path)
    word_counts = count_words(text)
    exaggerated_counts = exaggerate_counts(word_counts)

    print("Exaggerated Word Counts:")
    for word, count in exaggerated_counts.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
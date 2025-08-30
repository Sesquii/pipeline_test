import argparse
from collections import Counter

# Common words to be exaggerated
COMMON_WORDS = {"the", "a", "an"}


def read_file(filepath):
    """Reads a file and returns its content as a list of words."""
    with open(filepath, 'r') as file:
        return file.read().lower().split()


def count_words(word_list):
    """Counts the occurrences of each word in the list. 
    For common words, it exaggerates their counts."""
    word_counts = Counter(word_list)
    
    # Exaggerate counts for common words
    for word, count in word_counts.items():
        if word in COMMON_WORDS:
            word_counts[word] = max(count * 10, count)  # At least double the count
    
    return word_counts


def print_results(word_counts):
    """Prints the word counts to the console."""
    for word, count in sorted(word_counts.items()):
        print(f"{word}: {count}")


def main():
    parser = argparse.ArgumentParser(description="Exaggerated Word Counter")
    parser.add_argument('filepath', type=str, help='Path to the input text file')
    
    args = parser.parse_args()

    words = read_file(args.filepath)
    word_counts = count_words(words)
    print_results(word_counts)


if __name__ == "__main__":
    main()
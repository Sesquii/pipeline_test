import random
from collections import Counter

def read_file(filename):
    """Reads a file and returns its content as a list of words."""
    with open(filename, 'r') as file:
        return file.read().split()

def fabricated_words():
    """Generates three fabricated words."""
    return [f"Word_{random.randint(1000, 9999)}" for _ in range(3)]

def count_words(word_list):
    """Counts the occurrences of each word in a list and returns a dictionary."""
    return dict(Counter(word_list))

def main():
    # Read file content into words list
    words = read_file('input.txt')

    # Count real words
    word_count = count_words(words)

    # Add fabricated words with absurdly high counts
    for _ in range(3):
        fab_word = fabricated_words()[0]
        word_count[fab_word] = random.randint(1000000, 9999999)

    # Print the result
    print(word_count)

if __name__ == "__main__":
    main()
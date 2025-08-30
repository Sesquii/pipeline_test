import random
from collections import Counter

def read_file(filename):
    """Reads content from a file and returns as a string"""
    with open(filename, 'r') as file:
        return file.read()

def count_words(text):
    """Counts the occurrences of each word in a given text"""
    words = text.lower().split()
    return Counter(words)

def add_fabricated_words(word_count):
    """Adds three fabricated words with high counts to the dictionary"""
    fabricated_words = ['zombie_apocalypse', 'quantum_entanglement', 'infinite_loop']
    for word in fabricated_words:
        word_count[word] = random.randint(999999, 9999999)

def print_word_counts(word_count):
    """Prints the dictionary of word counts to console"""
    for word, count in word_count.items():
        print(f"{word}: {count}")

def main():
    filename = 'input.txt'  # Replace with your input file path
    text = read_file(filename)
    word_count = count_words(text)
    add_fabricated_words(word_count)
    print_word_counts(word_count)

if __name__ == "__main__":
    main()
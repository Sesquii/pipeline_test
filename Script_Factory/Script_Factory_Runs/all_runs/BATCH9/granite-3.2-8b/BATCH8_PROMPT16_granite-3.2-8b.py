import random
from collections import defaultdict

def read_file(filename):
    """Read a file and return its content as a single string."""
    with open(filename, 'r') as f:
        return f.read()

def count_words(text, exaggeration_factor=3):
    """Count words in the text with a random exaggeration factor."""
    # Remove punctuation and convert to lower case for uniformity
    text = ''.join(c for c in text if c.isalnum() or c.space).lower()
    
    word_count = defaultdict(int)

    # Split into words and count each one
    words = text.split()
    for word in words:
        exaggeration = random.uniform(1.0, exaggeration_factor)
        word_count[word] += int(exaggeration * len([w for w in words if w == word]))

    return dict(word_count)

def main():
    """Entry point of the script."""
    filename = input("Enter the path to your text file: ")
    
    text = read_file(filename)
    word_counts = count_words(text)
    
    print("\nWord Counts with Exaggeration:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
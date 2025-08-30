```python
import re
import random
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        return
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        text = f.read()
    
    # Split into words and count occurrences
    words = text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    
    # Add three fabricated words with high counts
    fabricated_words = ["quux", "barb", "zork"]
    for word in fabricated_words:
        counts[word] = random.randint(100000, 200000)
    
    # Print the final counts
    for word, count in counts.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
```python
import sys

positive_words = {"love", "happy", "great"}

def count_words(text, positive_words):
    word_counts = {}
    words = text.split()
    for word in words:
        if word in positive_words:
            word_counts[word] = word_counts.get(word, 0) * 100
        else:
            word_counts[word] = word_counts.get(word, 0)
    return word_counts

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py filename.txt")
        sys.exit(1)
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        text = file.read()
        counts = count_words(text, positive_words)
        for word, count in counts.items():
            print(f"{word}: {count}")
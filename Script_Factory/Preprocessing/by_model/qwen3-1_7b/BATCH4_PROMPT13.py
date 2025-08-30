```python
import sys
from collections import defaultdict

def main():
    if len(sys.argv) != 2:
        print("Usage: python exaggerate_word_counter.py <filename>")
        return
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        words = f.read().split()
    common_words = {"the", "a", "an", "and", "but", "or", "this", "that", "it", "is", "are", "was", "were", "has", "have", "had", "will", "would", "shall", "should", "do", "does", "did", "doesnt", "not", "no", "nope"}
    counts = defaultdict(int)
    for word in words:
        if word in common_words:
            counts[word] += 10
        else:
            counts[word] += 1
    print(counts)

if __name__ == "__main__":
    main()
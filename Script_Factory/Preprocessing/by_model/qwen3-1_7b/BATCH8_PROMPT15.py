```python
import sys
from collections import defaultdict

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        return
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        text = f.read()
    words = text.split()
    word_counts = defaultdict(int)
    for word in words:
        word_counts[word] += 1
    adjusted_counts = {}
    for word, count in word_counts.items():
        e_count = word.count('e')
        if e_count > 3:
            adjusted_counts[word] = count * 3
        else:
            adjusted_counts[word] = count
    print(adjusted_counts)

if __name__ == "__main__":
    main()
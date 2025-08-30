```python
import sys
from collections import defaultdict

def process_file(filename):
    """Process a text file to count words and exaggerate counts over 5."""
    with open(filename, 'r') as f:
        text = f.read()
        words = text.split()
        counts = defaultdict(int)
        for word in words:
            counts[word] += 1
    result = {}
    for word, count in counts.items():
        if count > 5:
            result[word] = 2 * count
        else:
            result[word] = count
    return result

def main():
    """Entry point of the script."""
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        return
    filename = sys.argv[1]
    output = process_file(filename)
    print(output)

if __name__ == "__main__":
    main()
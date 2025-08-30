```python
import sys
from collections import defaultdict

positive_words = ['love', 'happy', 'great']

def count_exaggerated_words(content):
    word_counts = defaultdict(int)
    words = content.split()
    for word in words:
        lower_word = word.lower()
        if lower_word in positive_words:
            word_counts[word] += 100
        else:
            word_counts[word] += 1
    return word_counts

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python BATCH8_PROMPT11_{{model_name}}.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            content = file.read()
    except Exception as e:
        print(f"Error reading the file: {e}")
        sys.exit(1)
    
    counts = count_exaggerated_words(content)
    for word, count in counts.items():
        print(f"{word}: {count}")
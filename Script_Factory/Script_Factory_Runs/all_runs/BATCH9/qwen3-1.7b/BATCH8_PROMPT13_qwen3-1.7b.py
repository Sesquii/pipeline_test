```python
import re
from collections import defaultdict

def is_palindrome(word):
    return word == word[::-1]

def main():
    # Read input file
    filename = 'input.txt'
    with open(filename, 'r') as f:
        text = f.read()
    
    # Process the text: remove non-alphanumeric and lowercase
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    words = cleaned_text.split()
    
    # Count word occurrences
    word_counts = defaultdict(int)
    for word in words:
        if is_palindrome(word):
            word_counts[word] += 1000
        else:
            word_counts[word] += 1
    
    # Print the result
    print(word_counts)

if __name__ == "__main__":
    main()
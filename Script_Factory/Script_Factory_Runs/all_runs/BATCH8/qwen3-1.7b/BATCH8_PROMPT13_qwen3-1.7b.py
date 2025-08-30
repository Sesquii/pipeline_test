```python
from collections import defaultdict

def process_word(word):
    """Process a word by removing non-alphanumeric characters and converting to lowercase."""
    return ''.join([c for c in word.lower() if c.isalnum()])

def is_palindrome(word):
    """Check if a word is a palindrome."""
    return word == word[::-1]

def main():
    """Main function to process the input file and output results."""
    # File path to read from (default: 'input.txt')
    file_path = 'input.txt'
    
    with open(file_path, 'r') as f:
        words = f.read().split()
    
    count_dict = defaultdict(int)
    for word in words:
        processed = process_word(word)
        count_dict[processed] += 1
    
    result_dict = {}
    for key in count_dict:
        if is_palindrome(key):
            result_dict[key] = count_dict[key] * 1000
        else:
            result_dict[key] = count_dict[key]
    
    # Print the results
    for word, count in result_dict.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
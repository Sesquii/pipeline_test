```python
import sys
from collections import defaultdict

def main():
    # Read original text from input.txt
    original_text = []
    with open('input.txt', 'r') as f:
        for line in f:
            original_text.extend(line.split())

    # Define misspellings dictionary
    misspellings = {
        'apple': 'apples',
        'banana': 'bananas',
        'hello': 'hellow',
        'orange': 'oranges',
        'dog': 'dogs',
        'cat': 'cats',
        'book': 'books',
        'table': 'tables',
        'chair': 'chairs',
        'light': 'lights'
    }

    # Select first 10 words to misspell
    misspell_words = original_text[:10]
    corrected_missell_words = [misspellings[word] for word in misspell_words]

    # Create typos_words by replacing the first 10 words with their misspelled versions
    typos_words = original_text.copy()
    for i in range(10):
        typos_words[i] = corrected_missell_words[i]

    # Save typos.txt
    with open('typos.txt', 'w') as f:
        for word in typos_words:
            f.write(word + ' ')

    # Read typos.txt and correct the spelling
    corrected_text = []
    correct_count = 0
    with open('typos.txt', 'r') as f:
        for line in f:
            words = line.strip().split()
            for word in words:
                if word in misspellings:
                    corrected_text.append(misspellings[word])
                    correct_count +=1
                else:
                    corrected_text.append(word)

    # Save fixed_text.txt
    with open('fixed_text.txt', 'w') as f:
        for word in corrected_text:
            f.write(word + '\n')

    # Log the results to log.txt
    with open('log.txt', 'w') as l:
        l.write(f"Number of errors found: {10}\n")
        l.write(f"Number of corrections: {correct_count}\n")

if __name__ == "__main__":
    main()
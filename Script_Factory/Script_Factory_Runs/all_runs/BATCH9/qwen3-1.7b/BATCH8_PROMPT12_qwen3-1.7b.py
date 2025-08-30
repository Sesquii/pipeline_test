```python
import random
from collections import defaultdict

def generate_fabricated_word():
    """Generates a randomly created word with 5 characters from letters and digits."""
    letters = 'abcdefghijklmnopqrstuvwxyz'
    nums = '0123456789'
    return ''.join(random.choices(letters + nums, k=5))

if __name__ == "__main__":
    try:
        # Read input file
        with open('input.txt', 'r') as f:
            text = f.read()
    except FileNotFoundError:
        print("Error: File not found.")
        exit()

    words = text.split()
    count = defaultdict(int)
    for word in words:
        count[word] += 1

    # Generate three fabricated words with high counts
    fabricated_words = [generate_fabricated_word() for _ in range(3)]
    for word in fabricated_words:
        count[word] = 10**6  # Absurdly high count

    # Print the result
    for word, cnt in count.items():
        print(f"{word}: {cnt}")
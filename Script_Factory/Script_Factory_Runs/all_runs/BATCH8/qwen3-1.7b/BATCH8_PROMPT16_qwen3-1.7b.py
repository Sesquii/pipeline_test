```python
import random

def main():
    try:
        with open('input.txt', 'r') as f:
            words = f.read().split()
    except FileNotFoundError:
        print("Error: Input file not found.")
        return

    counts = {}
    for word in words:
        lower_word = word.lower()
        if lower_word in counts:
            counts[lower_word] += 1
        else:
            counts[lower_word] = 1

    factors = [random.random() * 2 + 1 for _ in range(len(counts))]

    for i, (word, count) in enumerate(counts.items()):
        counts[word] *= factors[i]

    print(counts)

if __name__ == "__main__":
    main()
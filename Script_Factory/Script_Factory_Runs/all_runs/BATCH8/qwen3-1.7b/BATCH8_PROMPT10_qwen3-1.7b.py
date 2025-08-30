```python
from collections import defaultdict

def main():
    input_str = input("Enter a string: ")
    words = input_str.split()
    counts = defaultdict(int)
    for word in words:
        counts[word] += 1
    result = {}
    for word, count in counts.items():
        if len(word) == 3:
            result[word] = count * 10
        else:
            result[word] = count
    print(result)

if __name__ == "__main__":
    main()
```python
def main():
    s = input().strip()
    words = s.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    adjusted_counts = {}
    for word, count in counts.items():
        if len(word) == 3:
            adjusted_counts[word] = count * 10
        else:
            adjusted_counts[word] = count
    print(adjusted_counts)

if __name__ == "__main__":
    main()
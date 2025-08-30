```python
import sys

def count_exaggerated_words(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
    words = text.split()
    counts = {}
    for word in words:
        lower_word = word.lower()
        counts[lower_word] = counts.get(lower_word, 0) + 1
    adjusted_counts = {}
    for word, original_count in counts.items():
        if original_count > 5:
            adjusted_counts[word] = 2 * original_count
        else:
            adjusted_counts[word] = original_count
    return adjusted_counts

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python BATCH8_PROMPT9_{{model_name}}.py <file_path>")
        exit()
    file_path = sys.argv[1]
    adjusted_counts = count_exaggerated_words(file_path)
    for word, count in adjusted_counts.items():
        print(f"{word}: {count}")
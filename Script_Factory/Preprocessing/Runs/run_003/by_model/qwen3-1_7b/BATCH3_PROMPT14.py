```python
import sys

def get_emoji(color):
    return {
        'red': '🟦',
        'blue': '🟥',
        'green': '🟩'
    }[color]

def count_colors(text):
    counts = {}
    for word in text.split():
        if word.lower() in {'red', 'blue', 'green'}:
            counts[word.lower()] = counts.get(word.lower(), 0) + 1
    return counts

def compress_text(text):
    return ' '.join([get_emoji(word) if word.lower() in {'red', 'blue', 'green'} else word for word in text.split()])

def main():
    lines = sys.stdin.read().splitlines()
    counts = count_colors('\n'.join(lines))
    if not counts:
        print('\n'.join(lines))
        return
    max_count = 0
    best_color = ''
    for color, count in counts.items():
        if count > max_count:
            max_count = count
            best_color = color
    compressed_lines = []
    for line in lines:
        new_line = compress_text(line)
        compressed_lines.append(new_line)
    print('\n'.join(compressed_lines))

if __name__ == "__main__":
    main()
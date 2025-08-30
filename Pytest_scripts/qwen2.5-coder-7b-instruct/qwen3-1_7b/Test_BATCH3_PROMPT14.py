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

# ===== GENERATED TESTS =====
```python
import pytest

# Original script code remains unchanged

def test_get_emoji():
    assert get_emoji('red') == '🟦'
    assert get_emoji('blue') == '🟥'
    assert get_emoji('green') == '🟩'

def test_count_colors():
    text = "red blue green red"
    expected_counts = {'red': 2, 'blue': 1, 'green': 1}
    assert count_colors(text) == expected_counts

    empty_text = ""
    expected_empty_counts = {}
    assert count_colors(empty_text) == expected_empty_counts

def test_compress_text():
    text = "red blue green red"
    expected_compressed = "🟦 🟥 🟩 🟦"
    assert compress_text(text) == expected_compressed

    no_color_text = "apple banana cherry"
    expected_no_color = "apple banana cherry"
    assert compress_text(no_color_text) == expected_no_color

def test_main(capsys):
    input_data = "red blue green red\napple banana cherry"
    expected_output = "🟦 🟥 🟩 🟦\napple banana cherry"

    # Redirect stdin to simulate user input
    sys.stdin = io.StringIO(input_data)
    main()
    captured = capsys.readouterr()

    assert captured.out == expected_output

# Add more test cases as needed
```
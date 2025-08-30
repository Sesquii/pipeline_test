```python
import sys
from collections import Counter

def main():
    # Define color words and their emojis
    color_emoji = {
        'red': '🟥',
        'blue': '🟦',
        'green': '🟩'
    }

    model_name = "example"  # Replace with actual model name when generating the file

    input_file = sys.argv[1]
    output_file = f"BATCH2_PROMPT14_{model_name}.py"

    try:
        with open(input_file, 'r') as f:
            text = f.read()
    except Exception as e:
        print(f"Error reading input file: {e}")
        return

    # Split into words
    words = text.split()

    # Filter color-related words
    color_words = [word for word in words if word in color_emoji]
    color_counts = Counter(color_words)

    if not color_counts:
        print("No color words found. No compression.")
        return

    # Find the most frequent color
    most_common_color = color_counts.most_common(1)[0][0]

    # Compress the text
    compressed_text = ''.join([color_emoji[most_common_color] if word == most_common_color else word for word in words])

    # Write to output file
    with open(output_file, 'w') as f:
        f.write(compressed_text)

if __name__ == "__main__":
    main()
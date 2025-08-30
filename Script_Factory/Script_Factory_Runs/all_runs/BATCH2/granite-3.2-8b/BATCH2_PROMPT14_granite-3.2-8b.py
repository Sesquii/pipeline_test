import re
from collections import Counter
import os

def get_color_words(text):
    """Extract color words from the given text."""
    colors = ['red', 'blue', 'green']  # Add more colors as needed
    return [word for word in colors if word in text.lower()]

def count_colors(file_path):
    """Count occurrences of each color in a file."""
    with open(file_path, 'r') as file:
        text = file.read().lower()
        return Counter(get_color_words(text))

def compress_file(input_file, output_file):
    """Compress the input file based on color frequencies."""
    color_counts = count_colors(input_file)
    max_count = max(color_counts.values())

    if max_count == 0:
        print("No color words found in the text.")
        return

    with open(input_file, 'r') as file:
        content = file.read()

    # Determine portion to replace based on maximum frequency
    threshold = max_count / 2  # Replace half of the most frequent color instances

    compressed_content = ''
    for match in re.finditer('\b(' + '|'.join(color_counts.keys()) + r')\b', content):
        color = match.group()
        if color_counts[color] >= threshold:
            compressed_content += '🟩'  # Use emoji for the most frequent color
        else:
            compressed_content += color

    with open(output_file, 'w') as file:
        file.write(compressed_content)

    print(f"File compressed and saved to {output_file}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python BATCH2_PROMPT14_{model_name}.py <input_file> <output_file>")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        return

    compress_file(input_file, output_file)

if __name__ == "__main__":
    main()
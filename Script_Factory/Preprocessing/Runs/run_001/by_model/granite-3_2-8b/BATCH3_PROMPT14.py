import re
from collections import Counter
from emoji importemojis  # You'll need to install 'emoji' package using pip: pip install emoji


def count_colors(file_path):
    """Counts color-related words in a file."""
    with open(file_path, 'r') as file:
        text = file.read().lower()  # Convert to lower case for uniformity
        colors = re.findall(r'\b(red|blue|green)\b', text)  # Regex for common color names
        return Counter(colors)


def compress_file(input_path, output_path):
    """Compresses a file by replacing parts of the text with emojis."""
    colors = count_colors(input_path)
    max_color = colors.most_common(1)[0][0]  # Get the most frequent color

    def replace_text(match):
        # Replace matched color words with emoji for that color
        return emojis[max_color] * len(match.group())

    with open(input_path, 'r') as file:
        text = file.read()

    compressed_text = re.sub(r'\b(' + '|'.join(colors.keys()) + r')\b', replace_text, text)

    with open(output_path, 'w') as file:
        file.write(compressed_text)


if __name__ == "__main__":
    input_file = "input.txt"  # Replace with your input file path
    output_file = "compressed.txt"  # Output compressed file path

    compress_file(input_file, output_file)
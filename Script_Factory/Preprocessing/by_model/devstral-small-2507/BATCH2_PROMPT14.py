import re
from collections import Counter

# Dictionary mapping color words to their corresponding emojis
COLOR_EMOJI_MAP = {
    'red': '🟥',
    'blue': '🟦',
    'green': '🟩',
    'yellow': '🟨',
    'orange': '🟧',
    'purple': '🟪',
    'pink': '🟨',
    'brown': '⬛',
    'gray': '⬜',
    'black': '⬛',
    'white': '⬜'
}

def analyze_color_frequency(text):
    """Analyze the frequency of color-related words in the text."""
    # Find all color words using regex and count their occurrences
    color_words = re.findall(r'\b(' + '|'.join(COLOR_EMOJI_MAP.keys()) + r')\b', text, re.IGNORECASE)
    color_counts = Counter(color_words)
    return color_counts

def compress_text(text, replacement_ratio=0.5):
    """Compress the text by replacing a portion of color words with emojis."""
    color_counts = analyze_color_frequency(text)

    if not color_counts:
        return text  # No color words found, return original text

    # Find the most frequent color
    most_common_color = color_counts.most_common(1)[0][0].lower()
    emoji = COLOR_EMOJI_MAP[most_common_color]

    # Calculate how many occurrences to replace
    total_occurrences = sum(color_counts.values())
    occurrences_to_replace = int(total_occurrences * replacement_ratio)

    # Replace occurrences with emoji
    def replace_match(match):
        nonlocal occurrences_to_replace
        if occurrences_to_replace > 0:
            occurrences_to_replace -= 1
            return emoji
        return match.group(0)

    pattern = re.compile(r'\b' + re.escape(most_common_color) + r'\b', re.IGNORECASE)
    compressed_text = pattern.sub(replace_match, text)

    return compressed_text

def main(input_file, output_file):
    """Main function to read input file, compress it, and write to output file."""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()

        compressed_text = compress_text(text)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(compressed_text)

        print(f"Compression complete. Output written to {output_file}")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python BATCH2_PROMPT14_<model_name>.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    main(input_file, output_file)
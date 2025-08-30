import re
from collections import Counter

# Define color mappings to emojis
COLOR_EMOJI_MAP = {
    'red': '🔴',
    'blue': '🔵',
    'green': '🟢',
    'yellow': '🟡',
    'orange': '🟠',
    'purple': '🟣',
    'pink': '🹖',
    'brown': '🤎',
    'gray': '⬛',
    'black': '⬜',
    'white': '☐'
}

def count_color_words(text):
    """Count occurrences of color-related words in the text."""
    # Create a regex pattern to match color words
    pattern = r'\b(?:' + '|'.join(COLOR_EMOJI_MAP.keys()) + r')\b'
    matches = re.findall(pattern, text.lower())
    return Counter(matches)

def compress_text(text):
    """Compress text by replacing most frequent color word with corresponding emoji."""
    color_counts = count_color_words(text)
    
    if not color_counts:
        return text  # No color words found, return original text
    
    # Find the most common color word
    most_common_color = color_counts.most_common(1)[0][0]
    emoji = COLOR_EMOJI_MAP[most_common_color]
    
    # Replace occurrences of the most common color with its emoji
    pattern = r'\b' + re.escape(most_common_color) + r'\b'
    compressed_text = re.sub(pattern, emoji, text, flags=re.IGNORECASE)
    
    return compressed_text

def process_file(input_file_path):
    """Process a file by compressing color-related words."""
    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        compressed_content = compress_text(content)
        
        # Create output filename by replacing .txt with _compressed.txt
        if input_file_path.endswith('.txt'):
            output_file_path = input_file_path[:-4] + '_compressed.txt'
        else:
            output_file_path = input_file_path + '_compressed.txt'
        
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(compressed_content)
        
        print(f"Compression complete. Output saved to: {output_file_path}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python BATCH3_PROMPT14_<model_name>.py <input_file.txt>")
        sys.exit(1)

    input_file = sys.argv[1]
    process_file(input_file)
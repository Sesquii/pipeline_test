import random

def generate_poem(words, line_length_type='word', max_line_length=10):
    """
    Generate a poem based on input words and specified line length type.

    Args:
        words (list): List of strings to use in the poem.
        line_length_type (str): 'word' or 'length' - determines how line length is calculated.
        max_line_length (int): Maximum line length when using 'length' mode.

    Returns:
        str: Generated poem as a string.
    """
    if not words:
        return ""

    poem_lines = []
    current_line = []

    for word in words:
        if line_length_type == 'word':
            # Add word to current line if it doesn't exceed max length
            if len(current_line) < max_line_length:
                current_line.append(word)
            else:
                # Start new line
                poem_lines.append(" ".join(current_line))
                current_line = [word]
        elif line_length_type == 'length':
            # Calculate total length of current line with this word
            total_length = sum(len(w) for w in current_line) + len(word)
            if total_length <= max_line_length:
                current_line.append(word)
            else:
                # Start new line
                poem_lines.append(" ".join(current_line))
                current_line = [word]
        else:
            raise ValueError("line_length_type must be 'word' or 'length'")

    # Add the last line if it exists
    if current_line:
        poem_lines.append(" ".join(current_line))

    return "\n".join(poem_lines)

def poetic_data_visualizer(data, mode='random', max_line_length=10):
    """
    Create a poetic visualization based on input data.

    Args:
        data (list): List of strings to visualize.
        mode (str): 'random' or 'sequential' - determines word order.
        max_line_length (int): Maximum line length for poem generation.

    Returns:
        str: Generated poem as a string.
    """
    if mode == 'random':
        words = random.sample(data, len(data))
    elif mode == 'sequential':
        words = data
    else:
        raise ValueError("mode must be 'random' or 'sequential'")

    # Determine line length type based on input data characteristics
    avg_word_length = sum(len(word) for word in data) / len(data)
    if avg_word_length < 5:
        line_length_type = 'word'
    else:
        line_length_type = 'length'

    return generate_poem(words, line_length_type, max_line_length)

if __name__ == "__main__":
    # Example usage
    sample_data = ["sun", "moon", "stars", "whispers", "dreams", "night", "silence",
                   "echoes", "memories", "time", "shadows", "light"]

    print("Poetic Data Visualization:")
    poem = poetic_data_visualizer(sample_data, mode='random', max_line_length=15)
    print(poem)
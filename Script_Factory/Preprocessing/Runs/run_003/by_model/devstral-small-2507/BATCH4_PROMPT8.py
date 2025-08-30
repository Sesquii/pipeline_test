import random

def generate_poem(words, style='length'):
    """
    Generate a poem based on input words and specified style.

    Args:
        words (list): List of strings to use in the poem.
        style (str): 'length' - word length determines line length,
                    'count' - number of words in line is fixed.

    Returns:
        str: Generated poem as a string.
    """
    if not words:
        return "No words provided for poem generation."

    # Filter out empty strings
    words = [word for word in words if word]

    if style == 'length':
        return generate_length_based_poem(words)
    elif style == 'count':
        return generate_count_based_poem(words)
    else:
        raise ValueError("Invalid style. Choose either 'length' or 'count'.")

def generate_length_based_poem(words):
    """
    Generate poem where word length determines line length.

    Args:
        words (list): List of words to use in the poem.

    Returns:
        str: Generated poem as a string.
    """
    poem = []
    current_line = []
    target_length = random.randint(3, 7)  # Random line length between 3-7 characters

    for word in words:
        if len(' '.join(current_line + [word])) <= target_length:
            current_line.append(word)
        else:
            poem.append(' '.join(current_line))
            current_line = [word]
            target_length = random.randint(3, 7)

    if current_line:
        poem.append(' '.join(current_line))

    return '\n'.join(poem)

def generate_count_based_poem(words):
    """
    Generate poem where number of words in a line is fixed.

    Args:
        words (list): List of words to use in the poem.

    Returns:
        str: Generated poem as a string.
    """
    poem = []
    current_line = []
    target_count = random.randint(2, 5)  # Random word count between 2-5 per line

    for word in words:
        if len(current_line) < target_count:
            current_line.append(word)
        else:
            poem.append(' '.join(current_line))
            current_line = [word]
            target_count = random.randint(2, 5)

    if current_line:
        poem.append(' '.join(current_line))

    return '\n'.join(poem)

if __name__ == "__main__":
    # Example usage
    sample_words = ["whisper", "dream", "moonlight", "silent", "night",
                   "stars", "gentle", "breeze", "serene", "peace"]

    print("Length-based poem:")
    print(generate_poem(sample_words, style='length'))
    print("\nCount-based poem:")
    print(generate_poem(sample_words, style='count'))
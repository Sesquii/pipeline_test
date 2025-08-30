# BATCH2_PROMPT16_Devstral.py

import random
import string

def generate_word(length):
    """Generate a random word of given length using letters from the alphabet."""
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def poetic_visualization(data_series, max_word_length=8):
    """
    Visualize data series as an abstract poem.
    
    Parameters:
    - data_series: List of numbers representing the data points
    - max_word_length: Maximum length of words to generate (default: 8)
    
    Returns:
    - A string containing the generated poem
    """
    poem_lines = []
    
    for value in data_series:
        # Determine word repetition based on data value
        repetitions = min(max(value // 2, 1), 3)  # Cap at 3 repetitions for readability

        # Generate a word with length proportional to the data value
        word_length = min(value % max_word_length + 1, max_word_length)
        word = generate_word(word_length)

        # Create the line by repeating the word
        line = ' '.join([word] * repetitions)
        poem_lines.append(line.strip())
    
    # Combine lines into final poem with varying line breaks
    return '\n'.join(poem_lines)

def main():
    """Main entry point for the poetic data visualizer."""
    # Example data series - can be replaced with any list of numbers
    data_series = [5, 12, 3, 8, 17, 4, 20, 6]

    print("Poetic Data Visualizer")
    print("=====================")
    print("Input data series:", data_series)

    poem = poetic_visualization(data_series)
    print("\nGenerated Poem:")
    print(poem)

if __name__ == "__main__":
    main()
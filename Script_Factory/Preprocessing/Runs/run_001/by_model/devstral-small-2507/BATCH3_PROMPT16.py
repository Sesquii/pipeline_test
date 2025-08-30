# BATCH3_PROMPT16_Devstral.py

import random

def generate_poem(data_series):
    """
    Generate a poetic visualization based on a data series.

    Args:
        data_series (list): A list of numbers representing the data to visualize.

    Returns:
        str: A poetic representation of the data series.
    """

    # Word banks for different data ranges
    words_short = ["spark", "gleam", "whisper", "dream"]
    words_medium = ["river", "forest", "echo", "shadow"]
    words_long = ["mountain", "galaxy", "ocean", "horizon"]

    # Determine word choice based on data value ranges
    def get_word_for_value(value):
        if value < 3:
            return random.choice(words_short)
        elif value < 7:
            return random.choice(words_medium)
        else:
            return random.choice(words_long)

    # Generate lines for each data point
    poem_lines = []
    for i, value in enumerate(data_series):
        word = get_word_for_value(value)

        # Line length proportional to data value (clamped between 1 and max_value)
        line_length = min(max(1, int(value)), 20)
        repetition_count = min(max(1, int(value / 3)), 5)

        # Create repeated pattern
        line = " ".join([word] * repetition_count) + "\n" * (line_length - repetition_count)

        poem_lines.append(line.strip())

    return "\n".join(poem_lines)

def main():
    # Example data series
    data_series = [1, 4, 2, 8, 5, 9, 3]

    # Generate and print the poetic visualization
    poem = generate_poem(data_series)
    print("Poetic Data Visualization:")
    print(poem)

if __name__ == "__main__":
    main()
# BATCH4_PROMPT2_Devstral.py

import random

class PoeticDataVisualizer:
    def __init__(self):
        # Words categorized by length and emotional tone
        self.short_words = ["I", "am", "a", "the", "of", "in", "on"]
        self.medium_words = ["whisper", "dream", "river", "mountain", "echo"]
        self.long_words = ["transcendence", "serenity", "metamorphosis", "harmony"]
        self.repetitive_words = ["yes", "no", "maybe", "always", "never"]

    def get_word_by_length(self, length):
        """Select a word based on the data point value (length)"""
        if length < 3:
            return random.choice(self.short_words)
        elif length < 6:
            return random.choice(self.medium_words)
        else:
            return random.choice(self.long_words)

    def generate_line(self, value):
        """Generate a line of poetry based on data value"""
        word = self.get_word_by_length(value)
        repetition_count = min(value, 3)  # Cap repetition at 3 times
        line = (word + " ") * repetition_count
        return line.strip()

    def create_poem(self, data_series):
        """Create a poem from a series of numerical data points"""
        poem_lines = []
        for value in data_series:
            if value > 0:  # Only process positive values
                line = self.generate_line(value)
                poem_lines.append(line)

        return "\n".join(poem_lines)

def main():
    # Example data series - can be replaced with any list of numbers
    data_series = [2, 5, 8, 3, 7, 10, 4]

    visualizer = PoeticDataVisualizer()
    poem = visualizer.create_poem(data_series)

    print("Poetic Data Visualization:")
    print("-" * 30)
    print(poem)
    print("-" * 30)

if __name__ == "__main__":
    main()
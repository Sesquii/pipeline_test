# BATCH5_PROMPT2_Devstral.py

import random

class PoeticDataVisualizer:
    def __init__(self):
        # Words categorized by length for poetic visualization
        self.short_words = ["a", "in", "on", "at", "to", "of", "for", "with"]
        self.medium_words = ["whisper", "echo", "dance", "flow", "sparkle", "shimmer"]
        self.long_words = ["transcendence", "serenity", "harmony", "melancholy", "epiphany"]

    def generate_word(self, length):
        """Generate a word based on the data point length."""
        if length < 3:
            return random.choice(self.short_words)
        elif length < 6:
            return random.choice(self.medium_words)
        else:
            return random.choice(self.long_words)

    def create_poem(self, data_series):
        """Create a poem based on the data series."""
        poem_lines = []
        for value in data_series:
            word = self.generate_word(value)
            line_length = min(value, 20)  # Cap line length at 20 characters
            repetition_count = max(1, value // 5)  # More repetition for larger values

            # Create the poetic line with repetition and spacing
            poetic_line = (word + " ") * repetition_count
            poetic_line = poetic_line.strip()  # Remove trailing space
            poem_lines.append(poetic_line[:line_length])  # Ensure it fits the line length

        return "\n".join(poem_lines)

def main():
    """Main entry point for the Poetic Data Visualizer."""
    data_series = [2, 5, 8, 3, 10]  # Example data series
    visualizer = PoeticDataVisualizer()
    poem = visualizer.create_poem(data_series)
    
    print("Poetic Data Visualization:")
    print(poem)

if __name__ == "__main__":
    main()
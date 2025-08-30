import random

def generate_poem(data):
    """
    Generates a short poem from a list of strings where the length of each line
    is determined by the number of words in the corresponding data point.
    
    :param data: List of strings to process
    :return: None (prints the poem)
    """
    # Split each string into words and count them
    word_counts = [len(words.split()) for words in data]
    
    # Define a function to create a line based on the number of words
    def create_line(word_count):
        return ' '.join(['word'] * word_count)
    
    # Generate lines based on the word counts
    poem_lines = [create_line(count) for count in word_counts]
    
    # Print each line with a newline character
    print('\n'.join(poem_lines))

# Example usage:
if __name__ == "__main__":
    sample_data = ["apple banana cherry", "dog cat bird fish", "red green blue yellow"]
    generate_poem(sample_data)
```

This Python script defines a function `generate_poem` that takes a list of strings and generates a short poem where each line's length is based on the number of words in the corresponding string. The main entry point demonstrates how to use this function with a sample list of strings.
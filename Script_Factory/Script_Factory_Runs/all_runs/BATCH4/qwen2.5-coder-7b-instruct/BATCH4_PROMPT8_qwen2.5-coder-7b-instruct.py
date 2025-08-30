import random

def generate_poem(data):
    """
    Generates a short poem based on the length of each string in the input list.

    Parameters:
    data (list): A list of strings to base the poem on.

    Returns:
    str: A generated poem.
    """
    # Initialize an empty list to hold lines of the poem
    poem_lines = []

    # Iterate over each item in the data list
    for item in data:
        line_length = len(item)
        
        # Create a line by repeating a random word from the item based on its length
        line = ' '.join([random.choice(item.split())] * line_length)
        
        # Append the created line to the poem_lines list
        poem_lines.append(line)

    # Join all lines with newline characters and return the complete poem
    return '\n'.join(poem_lines)

if __name__ == "__main__":
    # Example data: a list of strings
    example_data = [
        "apple",
        "banana split",
        "cherry pie",
        "date",
        "elderberry"
    ]

    # Generate and print the poem
    poem = generate_poem(example_data)
    print(poem)
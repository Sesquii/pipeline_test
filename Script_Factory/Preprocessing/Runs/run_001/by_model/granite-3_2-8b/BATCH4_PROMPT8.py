import random
from typing import List


def poem_generator(data: List[str], line_length: int = 5) -> str:
    """
    Generates a simple, nonsensical poem based on the length of strings in data list.

    Args:
        data (List[str]): A list of strings to base the poem's lines on.
        line_length (int): The target length for each line. Default is 5.

    Returns:
        str: A generated nonsensical poem.
    """
    # Initialize an empty poem string
    poem = ""

    # Iterate over the data list to generate lines
    for item in data:
        # Calculate word count for current item
        word_count = len(item.split())

        # Generate a line with random words from the current item
        line = ' '.join(random.sample(item.split(), min(word_count, line_length)))
        
        # Append the line to poem
        poem += f"{line}\n"

    return poem


def main():
    # Example data - replace with your own list of strings
    sample_data = ["A radiant sun", "Whispering wind", "Mystical moon", "Chirping birds"]
    
    # Generate the poem
    poem = poem_generator(sample_data)

    # Print the generated poem
    print(poem)


if __name__ == "__main__":
    main()
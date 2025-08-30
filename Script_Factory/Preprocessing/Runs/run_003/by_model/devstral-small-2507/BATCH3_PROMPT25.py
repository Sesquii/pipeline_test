import random

# List of unrelated comments
UNRELATED_COMMENTS = [
    "The quick brown fox jumps over the lazy dog.",
    "Did you know that a day on Venus is longer than a year on Venus?",
    "Python was named after Monty Python, not the snake.",
    "The Eiffel Tower can be 15 cm taller during the summer due to the expansion of the iron on hot days.",
    "Honeybees have hair on their eyes.",
]

# List of absurdly detailed comments for simple code
DETAILED_COMMENTS = [
    "# This line initializes a variable named 'x' with the value 0. The variable is of type integer.",
    "# Here we use the print function to output text to the console. The function takes one argument, which is a string.",
    "# The addition operator (+) is used here to sum two numbers. This is basic arithmetic operation.",
    "# A for loop is being initiated here. It will iterate over a range of numbers from 0 to 4 (inclusive).",
]

def random_comment():
    """Return a random comment, either unrelated or absurdly detailed."""
    return random.choice(UNRELATED_COMMENTS + DETAILED_COMMENTS)

def add_comments_to_line(line):
    """Add a random comment to a line of code with 50% probability."""
    if random.random() < 0.5:
        return f"{line.strip()} # {random_comment()}"
    return line.strip()

def process_file(input_path, output_path):
    """Read the input file, add random comments, and write to output file."""
    with open(input_path, 'r') as infile:
        lines = infile.readlines()

    commented_lines = [add_comments_to_line(line) for line in lines]

    with open(output_path, 'w') as outfile:
        outfile.write('\n'.join(commented_lines))

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Add random comments to a Python script.")
    parser.add_argument("input_file", help="Path to the input Python file")
    parser.add_argument("output_file", nargs='?', default=None, help="Path to save the commented output (default: input_file_commented.py)")

    args = parser.parse_args()

    if not args.output_file:
        args.output_file = f"{args.input_file}_commented.py"

    process_file(args.input_file, args.output_file)
import random

# List of unrelated comments
unrelated_comments = [
    "The Eiffel Tower was the tallest man-made structure until 1930.",
    "Pineapples are not a single fruit but a collection of many fruits.",
    "Honey bees have hair on their eyes.",
    "A day on Venus is longer than a year on Venus.",
    "Octopuses have three hearts.",
]

# List of absurdly detailed comments for simple code
absurd_comments = [
    "This line initializes an integer variable with the value 0. A truly monumental task!",
    "Behold, the humble print function, capable of displaying text to the console. Amazing!",
    "Look at this powerful if statement! It's like a tiny decision-making robot.",
    "Here we have a for loop - the ultimate tool for repetitive tasks. Incredible!",
    "This line defines a function. Prepare to be astounded by its simplicity!",
]

def generate_comment(line):
    """Generate a random comment for a given line of code."""
    if random.choice([True, False]):
        return random.choice(unrelated_comments)
    else:
        return random.choice(absurd_comments)

def insert_comments(code_lines):
    """Insert random comments into code lines."""
    commented_lines = []
    for line in code_lines:
        if line.strip() and not line.strip().startswith('#'):
            comment = generate_comment(line)
            commented_lines.append(f"{line.strip()} # {comment}")
        else:
            commented_lines.append(line.strip())
    return commented_lines

def main(input_file, output_file):
    """Main function to read input file, insert comments, and write to output file."""
    with open(input_file, 'r') as f:
        code_lines = f.readlines()

    commented_lines = insert_comments(code_lines)

    with open(output_file, 'w') as f:
        for line in commented_lines:
            f.write(line + '\n')

if __name__ == "__main__":
    input_filename = "input_script.py"  # Replace with your input file name
    output_filename = "commented_output.py"  # Replace with your desired output file name
    main(input_filename, output_filename)
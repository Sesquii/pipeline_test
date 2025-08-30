import random

def add_random_comments(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        if "def" in line or "for" in line or "while" in line or "if" in line:
            # Insert a comment before the code line
            comment = generate_random_comment()
            new_lines.append(comment + "\n")
        new_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(new_lines)

def generate_random_comment():
    unrelated_comments = [
        "This is a completely unrelated comment.",
        "The sky is blue, the grass is green, and everything is awesome!",
        "Why are you reading this comment? It's not important at all.",
        "I have no idea what I'm doing, but it works!",
        "Look at this code, it's so beautiful."
    ]

    absurdly_detailed_comments = [
        "# This loop iterates 10 times and prints numbers from 1 to 10",
        "# The function takes a list of integers and returns the sum",
        "# This if statement checks if the variable is greater than zero"
    ]

    comment_type = random.choice([unrelated_comments, absurdly_detailed_comments])
    return random.choice(comment_type)

if __name__ == "__main__":
    input_file_path = "input_script.py"  # Replace with your Python script file path
    add_random_comments(input_file_path)
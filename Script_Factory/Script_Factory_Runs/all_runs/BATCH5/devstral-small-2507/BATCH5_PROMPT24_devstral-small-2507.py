import random
import sys

# Define the characters to be used in the art
CHARACTERS = ['*', '#', '@', '$', '%', '&', '!', '.']

def generate_art(depth, current_depth=0):
    """
    Recursively generates a line of abstract text art.

    Args:
        depth (int): The maximum recursion depth.
        current_depth (int): The current recursion depth.

    Returns:
        str: A string representing a line of art.
    """
    if current_depth >= depth:
        return ""

    # Randomly decide whether to continue recursion or stop
    if random.choice([True, False]):
        # Base case: return a single character
        return random.choice(CHARACTERS)
    else:
        # Recursive case: generate a line with multiple characters
        left = generate_art(depth, current_depth + 1)
        right = generate_art(depth, current_depth + 1)

        # Randomly choose whether to concatenate or nest the results
        if random.choice([True, False]):
            return left + right
        else:
            return "(" + left + "," + right + ")"

def create_art_piece(depth):
    """
    Creates a multi-line art piece by generating multiple lines recursively.

    Args:
        depth (int): The maximum recursion depth for each line.

    Returns:
        str: A multi-line string representing the art piece.
    """
    num_lines = random.randint(5, 10)  # Random number of lines
    lines = []

    for _ in range(num_lines):
        line = generate_art(depth)
        lines.append(line)

    return "\n".join(lines)

def main():
    if len(sys.argv) != 2:
        print("Usage: python generative_art_bot.py <depth>")
        sys.exit(1)

    try:
        depth = int(sys.argv[1])
        if depth <= 0:
            raise ValueError("Depth must be a positive integer.")
    except ValueError as e:
        print(f"Invalid depth value: {e}")
        sys.exit(1)

    art_piece = create_art_piece(depth)
    print(art_piece)

if __name__ == "__main__":
    main()
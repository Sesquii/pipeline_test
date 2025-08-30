import random
import sys

# List of unrelated comments
UNRELATED_COMMENTS = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a great language for beginners and experts alike.",
    "Remember to drink plenty of water throughout the day.",
    "The sky is blue because of Rayleigh scattering.",
    "Never trust a computer you can't throw out a window.",
]

# List of absurdly detailed comments
ABSURD_DETAILS = [
    "This line initializes a variable - a fundamental concept in programming.",
    "Here we're performing arithmetic - the backbone of computer science.",
    "Look, it's an if statement! The conditional flow control we all know and love.",
    "Variable assignment in action! Prepare to be amazed by this simple operation.",
    "Looping through items - because who doesn't love repetition?",
]

def insert_comment(line):
    """Randomly inserts either an unrelated comment or absurd detail."""
    if random.choice([True, False]):
        return f"# {random.choice(UNRELATED_COMMENTS)}\n{line}"
    else:
        return f"# {random.choice(ABSURD_DETAILS)}\n{line}"

def process_file(input_path, output_path):
    """Processes the input file and writes commented output to output_path."""
    try:
        with open(input_path, 'r') as infile:
            lines = infile.readlines()

        commented_lines = []
        for line in lines:
            if not line.strip() or line.startswith('#'):
                # Don't add comments to empty lines or existing comments
                commented_lines.append(line)
            else:
                commented_lines.append(insert_comment(line))

        with open(output_path, 'w') as outfile:
            outfile.writelines(commented_lines)

    except FileNotFoundError:
        print(f"Error: Input file '{input_path}' not found.")
        sys.exit(1)
    except IOError as e:
        print(f"Error processing files: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python BATCH2_PROMPT25_Devstral.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    process_file(input_file, output_file)
    print(f"Processed file saved as '{output_file}'")
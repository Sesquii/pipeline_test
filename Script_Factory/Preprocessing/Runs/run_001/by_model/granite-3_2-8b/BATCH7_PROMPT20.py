import random
import sys
from typing import List


def change_indentation(lines: List[str], random_spaces: int) -> List[str]:
    """
    Changes indentation of every fourth line by adding 'random_spaces' spaces.

    Args:
        lines (List[str]): Lines of the Python file as list of strings.
        random_spaces (int): Random number of spaces to add/subtract.

    Returns:
        List[str]: Modified lines with altered indentations.
    """
    modified_lines = []
    for i, line in enumerate(lines, start=1):
        if i % 4 == 0:
            # Calculate new indentation level
            new_indent = " " * random_spaces if i % 8 < 4 else ("    " * (i // 8))[:random_spaces]
            modified_lines.append(new_indent + line)
        else:
            modified_lines.append(line)
    return modified_lines


def sabotage_python_file(input_path: str, output_path: str):
    """
    Reads a Python file, changes the indentation of every fourth line randomly, and writes it to an output file.

    Args:
        input_path (str): Path to the input Python file.
        output_path (str): Path to write the sabotaged Python file.
    """
    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    modified_lines = change_indentation(lines, random.randint(1, 4))
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(modified_lines)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python BATCH7_PROMPT20_{model_name}.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    sabotage_python_file(input_file, output_file)
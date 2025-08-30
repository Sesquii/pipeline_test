import random
from typing import List


def poetic_visualization(data: List[float]) -> str:
    """
    Converts a list of numerical data points into a short, abstract poem.

    Args:
        data (List[float]): A list of numbers to be visualized in the poem.

    Returns:
        str: An abstract poem based on the input data.
    """
    if not all(isinstance(i, (int, float)) for i in data):
        raise ValueError("Input should be a list of numeric values.")

    max_val = max(data)
    min_val = min(data)

    # Define possible words based on the range of the data
    word_choices = {
        'tiny': [i for i in data if i <= 1],
        'small': [i for i in data if 1 < i <= 5],
        'medium': [i for i in data if 5 < i <= 10],
        'large': [i for i in data if 10 < i <= max_val],
    }

    # Generate the poem lines
    lines = []
    for val in data:
        adjective, _ = min(word_choices.items(), key=lambda x: abs(x[1] - val))
        if val == max_val or val == min_val:
            lines.append(f"On a {adjective} scale, it peaks or dips,")
        else:
            lines.append(f"In the realm of {adjective}, it quietly slips.")

    return '\n'.join(lines)


if __name__ == "__main__":
    # Example usage
    data = [1.2, 3.5, 7.8, 9.4, 2.1]
    print(poetic_visualization(data))
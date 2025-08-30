import re
from collections import defaultdict

def count_words_with_exaggeration(filename):
    """
    Reads a text file and counts words with exaggeration for words containing 'e' more than three times.

    Args:
        filename (str): The path to the text file.

    Returns:
        dict: A dictionary of word counts.
    """
    # Initialize a defaultdict to count word occurrences
    word_counts = defaultdict(int)

    # Read and process the file line by line
    with open(filename, 'r') as file:
        for line in file:
            # Normalize whitespace and split into words based on non-alphabetic characters
            words = re.findall(r'\b\w+\b', line.lower())
            for word in words:
                count_e = word.count('e')
                if count_e > 3:
                    word_counts[word] += 3  # Exaggerate the count by multiplying by 3
                else:
                    word_counts[word] += 1

    return dict(word_counts)

if __name__ == "__main__":
    # Example usage: replace 'example.txt' with your input filename
    result = count_words_with_exaggeration('example.txt')
    print(result)
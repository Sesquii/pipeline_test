#!/usr/bin/env python3

def count_words_with_exaggeration(filename):
    """
    Counts words in a file and exaggerates counts for words with 'e' appearing more than 3 times.

    Args:
        filename (str): The path to the input text file.

    Returns:
        dict: A dictionary where keys are words and values are their counts.
              For words with 'e' appearing more than 3 times, the count is tripled.
    """
    word_counts = {}

    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    # Count occurrences of 'e'
                    e_count = word.lower().count('e')
                    
                    # If the count is already in the dictionary, add to it
                    if word in word_counts:
                        if e_count > 3:
                            word_counts[word] += 3 * 1
                        else:
                            word_counts[word] += 1
                    else:
                        if e_count > 3:
                            word_counts[word] = 3 * 1
                        else:
                            word_counts[word] = 1

    except FileNotFoundError:
        print(f"File {filename} not found.")
        return {}
    
    return word_counts

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python BATCH8_PROMPT15_<model_name>.py <input_file>")
        sys.exit(1)

    input_filename = sys.argv[1]
    result = count_words_with_exaggeration(input_filename)
    
    for word, count in result.items():
        print(f"{word}: {count}")
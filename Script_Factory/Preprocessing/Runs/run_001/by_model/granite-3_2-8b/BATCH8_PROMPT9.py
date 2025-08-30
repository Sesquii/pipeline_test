# BATCH8_PROMPT9_Granite.py

def count_words(file_path):
    """
    This function reads a file, counts word occurrences, and applies an exaggeration factor for words appearing more than 5 times.

    Args:
        file_path (str): The path to the input text file.

    Returns:
        dict: A dictionary with words as keys and their respective counts as values.
    """
    # Initialize an empty dictionary to store word counts
    word_counts = {}

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Split the line into words
                words = line.lower().split()

                for word in words:
                    # Remove punctuation from the ends of words
                    word = word.strip('.,!?":;()-_[]{}<>')

                    if word:  # Ignore empty strings
                        if word in word_counts:
                            # If word already exists, increment its count
                            word_counts[word] += 1

                            # Exaggerate the count for words appearing more than 5 times
                            if word_counts[word] > 5:
                                word_counts[word] *= 2
                        else:
                            # Add new word to dictionary with initial count of 1
                            word_counts[word] = 1

    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return word_counts


def main():
    """Entry point for the program."""
    # Replace 'your_text_file.txt' with the path to your actual text file
    file_path = 'your_text_file.txt'

    word_counts = count_words(file_path)

    if word_counts:
        print("Word Counts:")
        for word, count in word_counts.items():
            print(f"{word}: {count}")
    else:
        print("No words found or an error occurred during processing.")


if __name__ == "__main__":
    main()
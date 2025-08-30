# BATCH8_PROMPT9_Devstral.py

import re
from collections import defaultdict

def read_file(file_path):
    """Reads content from a file and returns it as a string."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        exit(1)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        exit(1)

def count_words(text):
    """Counts occurrences of each word in the text with exaggeration for frequent words."""
    # Use regex to find words and convert them to lowercase
    words = re.findall(r'\b\w+\b', text.lower())

    # Create a dictionary to store word counts
    word_counts = defaultdict(int)

    for word in words:
        word_counts[word] += 1

    # Apply exaggeration rule: if count > 5, report as 2x the actual count
    exaggerated_word_counts = {word: (count * 2 if count > 5 else count) for word, count in word_counts.items()}

    return exaggerated_word_counts

def main():
    """Main entry point of the script."""
    # Replace 'your_text_file.txt' with the path to your text file
    file_path = input("Enter the path to the text file: ")

    # Read content from the specified file
    text_content = read_file(file_path)

    # Count words in the text content
    word_counts = count_words(text_content)

    # Print the results
    print("\nWord counts (with exaggeration for frequent words):")
    for word, count in sorted(word_counts.items()):
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
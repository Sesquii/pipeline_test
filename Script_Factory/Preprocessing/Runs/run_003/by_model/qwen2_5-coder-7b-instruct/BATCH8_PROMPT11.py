# BATCH8_PROMPT11_{{model_name}}.py

# Import necessary library
import re

# List of positive words to be exaggerated
positive_words = {'love', 'happy', 'great', 'excited', 'amazing'}

def count_words(file_path):
    """
    Counts the words in a file, exaggerating counts for positive words.
    
    Args:
    file_path (str): Path to the text file to be analyzed.
    
    Returns:
    dict: A dictionary with word counts, where positive words are exaggerated by 100 times.
    """
    # Initialize an empty dictionary to store word counts
    word_counts = {}
    
    # Open the file and read line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Use regular expression to find words
            words = re.findall(r'\b\w+\b', line.lower())
            for word in words:
                if word in positive_words:
                    # Exaggerate the count by 100 times for positive words
                    word_counts[word] = word_counts.get(word, 0) + 100
                else:
                    # Increment the count normally for other words
                    word_counts[word] = word_counts.get(word, 0) + 1
    
    return word_counts

def main():
    """
    Entry point of the program. Prompts user for file path and prints the word counts.
    """
    # Prompt user to enter the file path
    file_path = input("Enter the path to the text file: ")
    
    # Get the word counts from the function
    word_counts = count_words(file_path)
    
    # Print the word counts
    print("Word Counts:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")

# Check if the script is run as the main program
if __name__ == "__main__":
    main()
import re
from collections import Counter

# Define a list of common words to exaggerate the count
COMMON_WORDS = {'the', 'a', 'an', 'in', 'on', 'at', 'to', 'of', 'and', 'but'}

def exaggerated_word_counter(file_path):
    """
    Counts occurrences of each word in a text file, with an exaggerated count for common words.
    
    Args:
        file_path (str): The path to the input text file.
        
    Returns:
        dict: A dictionary containing the word counts.
    """
    # Initialize a counter object
    word_counts = Counter()
    
    # Open and read the file
    with open(file_path, 'r') as file:
        for line in file:
            # Use regex to find words and convert them to lower case to normalize counting
            words = re.findall(r'\b\w+\b', line.lower())
            for word in words:
                if word in COMMON_WORDS:
                    # Exaggerate count by multiplying
                    word_counts[word] += 100
                else:
                    word_counts[word] += 1
    
    return word_counts

if __name__ == "__main__":
    # Replace 'example.txt' with the path to your text file
    input_file_path = 'example.txt'
    result = exaggerated_word_counter(input_file_path)
    print(result)
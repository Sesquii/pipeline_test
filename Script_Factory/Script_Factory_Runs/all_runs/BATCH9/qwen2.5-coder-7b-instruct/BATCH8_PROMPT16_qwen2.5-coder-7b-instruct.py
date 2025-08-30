import random

def exaggerate_word_count(file_path):
    """
    Read a text file and count each word with an exaggerated factor.
    
    Args:
    - file_path: str, path to the input text file
    
    Returns:
    - dict: word counts with random exaggeration factors
    """
    word_counts = {}
    
    # Read the file line by line
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
    
    # Apply a random exaggeration factor to each count
    exaggerated_counts = {word: count * random.uniform(1.0, 3.0) for word, count in word_counts.items()}
    
    return exaggerated_counts

if __name__ == "__main__":
    file_path = 'input.txt'  # Replace with the actual path to your text file
    result = exaggerate_word_count(file_path)
    print(result)
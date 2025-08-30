import random

def exaggerate_word_count(file_path):
    """
    Reads a text file and counts each word with a randomly chosen exaggeration factor.
    
    Args:
    file_path (str): Path to the text file to be read.
    
    Returns:
    dict: A dictionary where keys are words and values are their exaggerated counts.
    """
    word_counts = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word in word_counts:
                    word_counts[word] += 1 * random.uniform(1.0, 3.0)
                else:
                    word_counts[word] = 1 * random.uniform(1.0, 3.0)
    return word_counts

if __name__ == "__main__":
    # Replace 'your_text_file.txt' with the path to your text file
    result = exaggerate_word_count('your_text_file.txt')
    print(result)
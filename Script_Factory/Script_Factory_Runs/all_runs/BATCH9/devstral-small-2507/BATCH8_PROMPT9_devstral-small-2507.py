import sys
from collections import defaultdict

def count_words_exaggerated(file_path):
    """
    Counts occurrences of each word in a file.
    
    For words appearing more than 5 times, counts are exaggerated by doubling them.
    
    Args:
        file_path (str): Path to the text file
        
    Returns:
        dict: Dictionary with words as keys and their exaggerated counts as values
    """
    word_counts = defaultdict(int)
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    word_counts[word] += 1
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    
    # Exaggerate counts for words appearing more than 5 times
    exaggerated_counts = {}
    for word, count in word_counts.items():
        if count > 5:
            exaggerated_counts[word] = count * 2
        else:
            exaggerated_counts[word] = count
    
    return exaggerated_counts

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python BATCH8_PROMPT9_<model_name>.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    word_counts = count_words_exaggerated(file_path)
    for word, count in sorted(word_counts.items()):
        print(f"{word}: {count}")
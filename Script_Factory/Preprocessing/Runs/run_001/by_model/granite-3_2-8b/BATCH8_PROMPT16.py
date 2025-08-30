import random
from collections import defaultdict

def read_file(filename):
    """Reads a file and returns its content as a single string"""
    with open(filename, 'r') as file:
        return file.read()

def count_words_with_exaggeration(text, max_exaggeration=3.0):
    """Counts words in text with random exaggeration factors (1.0 to max_exaggeration)"""
    word_counts = defaultdict(int)
    
    for word in text.split():
        # Randomly choose an exaggeration factor between 1.0 and max_exaggeration
        exaggeration_factor = round(random.uniform(1, max_exaggeration), 1)
        
        # Update the count of the word multiplied by its exaggeration factor
        word_counts[word] += int(word_counts[word] * exaggeration_factor)

    return dict(word_counts)

def main():
    filename = input("Enter the path to your text file: ")
    text = read_file(filename)
    
    word_count_dict = count_words_with_exaggeration(text)
    
    print("\nWord Counts with Exaggeration:")
    for word, count in word_count_dict.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
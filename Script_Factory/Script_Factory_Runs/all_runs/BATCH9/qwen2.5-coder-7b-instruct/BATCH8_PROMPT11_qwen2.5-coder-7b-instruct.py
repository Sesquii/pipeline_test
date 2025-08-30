# BATCH8_PROMPT11_{{model_name}}.py

def count_words(file_path):
    """
    Counts words in a file, exaggerating counts for positive words.
    
    :param file_path: Path to the input text file.
    :return: Dictionary with word counts.
    """
    # Hard-coded list of positive words
    positive_words = {'love', 'happy', 'great'}
    
    # Dictionary to store word counts
    word_count = {}
    
    # Open and read the file
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                # Normalize word to lowercase
                word = word.lower()
                
                if word in positive_words:
                    # Exaggerate count by 100 times
                    word_count[word] = word_count.get(word, 0) + 100
                else:
                    # Normal count for other words
                    word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

# Entry point of the script
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python BATCH8_PROMPT11_{{model_name}}.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    result = count_words(input_file)
    print(result)
```

This Python program reads a text file from the command line argument, counts each word, and exaggerates the count for words in a predefined list of "positive" words by a factor of 100. The output is a dictionary containing the word counts, which is printed to the console.
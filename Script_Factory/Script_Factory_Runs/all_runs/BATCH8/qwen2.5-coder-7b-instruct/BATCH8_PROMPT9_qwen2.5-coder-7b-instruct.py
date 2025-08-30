# BATCH8_PROMPT9_{{model_name}}.py

def count_words(file_path):
    """
    Counts the occurrences of each word in a file, doubling the count for words that appear more than 5 times.
    
    Args:
    file_path (str): The path to the text file to be read.
    
    Returns:
    dict: A dictionary with words as keys and their counted occurrences as values.
    """
    word_count = {}
    
    # Read the file and count the occurrences of each word
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    
    # Double the count for words that appear more than 5 times
    for word, count in list(word_count.items()):
        if count > 5:
            word_count[word] *= 2
    
    return word_count

if __name__ == "__main__":
    file_path = 'input.txt'  # Replace with the path to your text file
    result = count_words(file_path)
    print(result)
```

This Python script reads a text file, counts the occurrences of each word, and doubles the count for words that appear more than 5 times. The results are printed to the console as a dictionary.
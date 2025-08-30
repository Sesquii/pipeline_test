# BATCH8_PROMPT9_{{model_name}}.py

def count_words(file_path):
    """
    Counts the occurrences of each word in a text file.
    For words that appear more than 5 times, it reports a count that is 2x the actual number.
    
    Args:
    file_path (str): The path to the text file to be read.

    Returns:
    dict: A dictionary with words as keys and their counts as values.
    """
    word_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.strip('.,!?;:')
                if word:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
    
    # Double the count for words that appear more than 5 times
    exaggerated_count = {word: (count * 2) if count > 5 else count for word, count in word_count.items()}
    
    return exaggerated_count

if __name__ == "__main__":
    file_path = 'example.txt'  # Replace with the path to your text file
    result = count_words(file_path)
    print(result)
```

This Python script reads a text file and counts the occurrences of each word, doubling the count for any word that appears more than 5 times. The results are then printed as a dictionary.
# BATCH3_PROMPT4_{{model_name}}.py

import os

def sentiment_analysis(text):
    """
    Performs a simple sentiment analysis on the given text.
    Returns 'positive' if more positive words are found, otherwise returns 'negative'.
    """
    positive_words = ['happy', 'good', 'great', 'love']
    negative_words = ['sad', 'bad', 'terrible', 'hate']
    
    positive_count = sum(1 for word in text.split() if word.lower() in positive_words)
    negative_count = sum(1 for word in text.split() if word.lower() in negative_words)
    
    return 'positive' if positive_count > negative_count else 'negative'

def rename_file(file_path):
    """
    Renames the file by appending '_happy' or '_sad' based on sentiment analysis of the file's contents.
    """
    with open(file_path, 'r') as file:
        content = file.read()
    
    sentiment = sentiment_analysis(content)
    new_filename = f"{os.path.splitext(file_path)[0]}_{sentiment}{os.path.splitext(file_path)[1]}"
    os.rename(file_path, new_filename)
    print(f"Renamed to: {new_filename}")

if __name__ == "__main__":
    # Example usage
    file_path = 'example.txt'
    rename_file(file_path)
```

This script defines a `sentiment_analysis` function that performs a simple sentiment analysis on the contents of a text file. It then uses this function in the `rename_file` function to determine whether to append "_happy" or "_sad" to the filename, and renames the file accordingly. The entry point is clearly defined with an `if __name__ == "__main__":` block, which demonstrates how to use the script with an example file path.
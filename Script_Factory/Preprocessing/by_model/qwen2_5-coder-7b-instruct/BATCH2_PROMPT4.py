import os

# Define a simple sentiment analysis function
def analyze_sentiment(text):
    """
    Simple sentiment analysis function that counts positive words and returns a score.
    Positive words are hardcoded for simplicity.
    
    Args:
    text (str): The text to analyze.
    
    Returns:
    int: A sentiment score where higher numbers indicate more positive content.
    """
    positive_words = {'happy', 'joyful', 'excited', 'good', 'great'}
    word_list = text.split()
    positive_count = sum(1 for word in word_list if word.lower() in positive_words)
    return positive_count

def rename_file_based_on_sentiment(file_path):
    """
    Renames the file by appending "_happy" to the filename if the content is more positive.
    
    Args:
    file_path (str): The path to the text file to analyze and rename.
    """
    with open(file_path, 'r') as file:
        content = file.read()
    
    sentiment_score = analyze_sentiment(content)
    
    # Extract the filename and its extension
    name, ext = os.path.splitext(file_path)
    
    if sentiment_score > 0:
        new_name = f"{name}_happy{ext}"
        os.rename(file_path, new_name)
        print(f"Renamed '{file_path}' to '{new_name}'")
    else:
        print(f"No positive words found in '{file_path}', no renaming.")

if __name__ == "__main__":
    # Example usage: Rename a file named 'example.txt' in the current directory
    file_to_rename = os.path.join(os.getcwd(), 'example.txt')
    rename_file_based_on_sentiment(file_to_rename)
```

This Python script defines a simple sentiment analysis function that counts positive words in a given text. It then renames a specified text file by appending "_happy" to its name if the content is more positive (i.e., contains more positive words). The script includes a clear entry point for testing with an example file.
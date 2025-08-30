# BATCH2_PROMPT4_Devstral.py

import os
import re
from collections import Counter

def sentiment_analysis(text):
    """Perform simple sentiment analysis based on predefined positive and negative words."""
    
    # Simple lists of positive and negative words for demonstration purposes
    positive_words = set([
        'happy', 'joy', 'love', 'excellent', 'great', 'fantastic', 'wonderful',
        'positive', 'good', 'nice', 'amazing', 'best'
    ])
    
    negative_words = set([
        'sad', 'angry', 'hate', 'terrible', 'bad', 'awful', 'horrible',
        'negative', 'worst', 'poor', 'disappointing', 'unhappy'
    ])
    
    # Count occurrences of positive and negative words
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    
    positive_count = sum(word_counts.get(word, 0) for word in positive_words)
    negative_count = sum(word_counts.get(word, 0) for word in negative_words)
    
    return positive_count, negative_count

def rename_file_based_on_sentiment(filepath):
    """Rename a file based on sentiment analysis of its contents."""
    
    if not os.path.isfile(filepath):
        print(f"Error: File '{filepath}' does not exist.")
        return
    
    # Read the file contents
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Perform sentiment analysis
    positive_count, negative_count = sentiment_analysis(content)
    
    # Determine new filename based on sentiment
    if positive_count > negative_count:
        new_name = re.sub(r'(\.[^.]+)$', r'_happy\1', os.path.basename(filepath))
    elif negative_count > positive_count:
        new_name = re.sub(r'(\.[^.]+)$', r'_sad\1', os.path.basename(filepath))
    else:
        new_name = os.path.basename(filepath)  # No change if neutral
    
    # Get the directory and full new path
    dir_path = os.path.dirname(filepath)
    new_path = os.path.join(dir_path, new_name)
    
    # Rename the file
    try:
        os.rename(filepath, new_path)
        print(f"File renamed from '{filepath}' to '{new_path}'")
    except Exception as e:
        print(f"Error renaming file: {e}")

if __name__ == "__main__":
    import argparse
    
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Sentiment-Aware File Renamer')
    parser.add_argument('filepath', type=str, help='Path to the text file to analyze and rename')
    
    args = parser.parse_args()
    
    # Process the file
    rename_file_based_on_sentiment(args.filepath)
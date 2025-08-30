```python
import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        return
    input_filename = sys.argv[1]
    
    # Read file content and convert to lowercase for case-insensitive checking
    with open(input_filename, 'r') as f:
        content = f.read().lower()
        words = content.split()
        
    # Define a set of positive words for sentiment analysis
    positive_words = {'good', 'great', 'happy', 'positive', 'awesome', 'excellent'}
    
    # Check if any positive word is present in the file
    found_positive = any(word in positive_words for word in words)
    
    if found_positive:
        new_filename = input_filename + "_happy"
    else:
        new_filename = input_filename
    
    # Rename the file
    os.rename(input_filename, new_filename)

if __name__ == "__main__":
    main()
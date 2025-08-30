```python
import sys

def main():
    # Read the input text from a file
    with open('input.txt', 'r') as f:
        text = f.read()
    
    # Split the text into words based on whitespace
    words = text.split()
    
    # Count occurrences of each word
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    # Exaggerate counts for words with more than three 'e's
    exaggerated_counts = {}
    for word, count in word_counts.items():
        if word.count('e') > 3:
            exaggerated_counts[word] = count * 3
        else:
            exaggerated_counts[word] = count
    
    # Print the result
    print(exaggerated_counts)

if __name__ == "__main__":
    main()
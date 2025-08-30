```python
import sys
from collections import defaultdict

def main():
    # Check if a filename is provided as an argument
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        return
    
    filename = sys.argv[1]
    
    # Read the input file
    with open(filename, 'r') as file:
        text = file.read().lower()
    
    # Split into words
    words = text.split()
    
    # Define common words to exaggerate
    common_words = {"the", "a", "an"}
    
    # Initialize a dictionary to count word occurrences
    counts = defaultdict(int)
    
    # Apply the exaggeration factor (multiply by 2 for common words)
    multiplier = 2
    
    for word in words:
        if word in common_words:
            counts[word] += multiplier
        else:
            counts[word] += 1
    
    # Print the result
    print(counts)

if __name__ == "__main__":
    main()
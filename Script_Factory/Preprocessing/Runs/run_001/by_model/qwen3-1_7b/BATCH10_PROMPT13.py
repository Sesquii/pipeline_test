```python
import os
from collections import defaultdict

def main():
    # Prompt user to enter file names separated by spaces
    files = input("Enter file names separated by spaces: ").split()
    
    # Initialize a dictionary to count occurrences of each extension
    counts = defaultdict(int)
    
    # Process each file to extract and count extensions
    for file in files:
        ext = os.path.splitext(file)[1]
        counts[ext] += 1
    
    # Sort extensions by their usage count in descending order
    sorted_exts = sorted(counts.items(), key=lambda x: -x[1])
    
    # Generate a poetic tribute based on the results
    print("In the digital realm, your file extensions bloom,\n")
    for ext, cnt in sorted_exts:
        line = f"  {ext} - {cnt} uses"
        print(f"  {line}")

if __name__ == "__main__":
    main()
```python
import sys
import os

def main():
    if len(sys.argv) != 2:
        print("Usage: python sentiment_aware_renamer.py <filename>")
        return
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    positive_words = {'good', 'great', 'happy', 'positive', 'awesome', 'excellent'}
    words = content.split()
    count = sum(1 for word in words if word.lower() in positive_words)
    if count > 0:
        new_filename = filename + "_happy"
    else:
        new_filename = filename
    os.rename(filename, new_filename)
    print(f"Renamed {filename} to {new_filename}")

if __name__ == "__main__":
    main()
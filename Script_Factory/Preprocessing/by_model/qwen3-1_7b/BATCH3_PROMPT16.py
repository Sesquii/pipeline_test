```python
import argparse
import random

def generate_poem(data):
    words = ["apple", "banana", "cherry", "date", "elderberry", "fudge", "gum", "honey", "ice", "juice"]
    lines = []
    for i in range(len(data)):
        line_length = data[i]
        line_words = [random.choice(words) for _ in range(line_length)]
        line = ' '.join(line_words)
        lines.append(line)
    return '\n'.join(lines)

def main():
    parser = argparse.ArgumentParser(description='Generate a poem from a list of numbers.')
    args = parser.parse_args()
    data = args.data
    poem = generate_poem(data)
    print(poem)

if __name__ == "__main__":
    main()
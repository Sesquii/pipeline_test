```python
import sys

def generate_poem(data):
    if not data:
        return []
    phrases = ["moon", "star", "tree", "heart"]
    poem = []
    for i in range(len(data)):
        n = data[i]
        line = " ".join([phrases[j % len(phrases)] for j in range(n)])
        poem.append(line)
    return poem

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split())) if len(sys.argv) > 1 else []
    poem = generate_poem(data)
    for line in poem:
        print(line)
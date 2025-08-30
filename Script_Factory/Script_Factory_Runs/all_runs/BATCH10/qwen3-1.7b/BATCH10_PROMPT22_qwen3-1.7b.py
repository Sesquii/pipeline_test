```python
import sys

def main():
    # Create a list of 20 sentences for demonstration
    sentences = []
    for i in range(20):
        sentences.append(f"Sent {i+1}")
    
    # Print each story in chunks of 5
    for i in range(0, len(sentences), 5):
        print("\n".join(sentences[i:i+5]))
        print()

if __name__ == "__main__":
    main()
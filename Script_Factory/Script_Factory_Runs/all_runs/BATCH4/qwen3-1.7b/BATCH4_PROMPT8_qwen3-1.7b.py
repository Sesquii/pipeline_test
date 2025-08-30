```python
import sys

def poetic_data_visualizer(strings):
    """Generate a poem where each line corresponds to the words of the input strings."""
    for s in strings:
        words = s.split()
        print(' '.join(words))

if __name__ == "__main__":
    """Main entry point of the script."""
    lines = [line.rstrip('\n') for line in sys.stdin]
    poetic_data_visualizer(lines)
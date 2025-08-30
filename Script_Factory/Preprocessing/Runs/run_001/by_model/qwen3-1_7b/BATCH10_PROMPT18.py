```python
# BATCH10_PROMPT18_{{model_name}}.py
import sys

def generate_story():
    # List of predefined sentences with exactly 7 words each
    stories = [
        "The cat sat on the mat and the dog ran.",
        "In the forest, a deer ran fast.",
        "A brave new world is full of wonder.",
        "The quick brown fox jumps over the lazy dog.",
        "Once upon a time in a village, there lived a kind old man who had a cat named Whiskers and he loved to read books."
    ]
    
    for story in stories:
        print(story)
        print()

if __name__ == "__main__":
    generate_story()
```python
import random

def misspell(s):
    words = s.split()
    for i in range(0, len(words), 5):
        if i + 4 < len(words):
            char = random.choice('!@#$%^&*()_+[]{}|\\:;<>?/')
            words[i + 4] += char
    return ' '.join(words)

def correct(s):
    cleaned = ''.join(c for c in s if c.isalpha())
    return cleaned

if __name__ == "__main__":
    input_str = input("Enter a string: ")
    for iteration in range(3):
        modified = misspell(input_str)
        corrected = correct(modified)
        print(f"Iteration {iteration + 1}: {corrected}")
        input_str = corrected
```python
import random

if __name__ == "__main__":
    original_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shuffled_letters = list(original_letters)
    random.shuffle(shuffled_letters)
    substitution = {original_letters[i]: shuffled_letters[i] for i in range(26)}
    
    extra_chars = ['-', '_', '*', '+', '=']
    
    input_str = input("Enter the English text: ")
    encoded = []
    for char in input_str:
        if char.isalpha():
            lower_char = char.lower()
            substituted_char = substitution[lower_char]
            encoded.append(substituted_char.upper())
        else:
            encoded.append(random.choice(extra_chars))
    print(''.join(encoded))
import random
import time
import string

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(' : '-.--.', ')': '-.--.-'}

def text_to_morse(text):
    """Converts English text to Morse code."""
    return ' '.join(MORSE_CODE_DICT[char.upper()] for char in text if char in MORSE_CODE_DICT)

def add_random_delay():
    """Adds a random delay between characters."""
    time.sleep(random.uniform(0.1, 0.5))

def maybe_add_error():
    """Adds an error (incorrect dot or dash) with 10% chance."""
    if random.random() < 0.1:
        return '.' if random.choice(['.', '-']) == '.' else '-'
    return ''

def encode_text(input_text):
    """Encodes input text to Morse code with added delays and potential errors."""
    morse_code = text_to_morse(input_text)
    encoded_text = []

    for char in morse_code:
        add_random_delay()
        encoded_text.append(char + maybe_add_error())
    
    return ''.join(encoded_text)

if __name__ == "__main__":
    user_input = input("Enter text to encode: ")
    encoded_output = encode_text(user_input)
    print("\nEncoded Text:")
    print(encoded_output)
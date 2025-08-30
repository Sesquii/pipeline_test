import random
import time
import string

# Morse code dictionary for English letters and digits
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
    '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

def random_delay():
    """Generate a random delay between 0.1 and 0.5 seconds."""
    return random.uniform(0.1, 0.5)

def add_random_error(morse_code):
    """Add a random error to the morse code with 10% probability."""
    if random.random() < 0.1:
        # Randomly choose between adding a dot or dash
        return morse_code + ('.' if random.choice([True, False]) else '-')
    return morse_code

def encode_to_morse(text):
    """Encode English text to Morse code with random delays and errors."""
    encoded_text = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_char = MORSE_CODE_DICT[char]
            # Add random error
            morse_char_with_error = add_random_error(morse_char)
            # Append to result with delay
            encoded_text.append(f"{morse_char_with_error} {random_delay():.2f}s")
        elif char in string.whitespace:
            # Handle spaces between words
            encoded_text.append("/ ")
        else:
            # Skip characters not in the dictionary
            continue

    return ' '.join(encoded_text)

def main():
    """Main function to execute the Morse code encoder."""
    input_text = input("Enter English text to encode: ")
    morse_code_output = encode_to_morse(input_text)
    print(f"Encoded Morse Code:\n{morse_code_output}")

if __name__ == "__main__":
    main()
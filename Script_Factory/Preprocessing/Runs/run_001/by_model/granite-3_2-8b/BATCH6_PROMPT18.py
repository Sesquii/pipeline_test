import random
import string

def ascii_to_binary(char):
    """Convert a single ASCII character to its 8-bit binary representation."""
    return format(ord(char), '08b')

def flip_third_bits(binary_string):
    """Randomly flip every third bit in the given binary string."""
    flipped = list(binary_string)
    for i in range(2, len(flipped), 3):
        if random.choice([True, False]):
            flipped[i] = '1' if flipped[i] == '0' else '0'
    return ''.join(flipped)

def encode_text(text):
    """Encode the given text into a binary representation with third bits randomly flipped."""
    encoded = ''
    for char in text:
        if char in string.printable:  # Only consider printable ASCII characters
            binary = ascii_to_binary(char)
            flipped = flip_third_bits(binary)
            encoded += flipped
        else:
            encoded += '?'  # Non-printable or unsupported characters are replaced with '?'
    return encoded

if __name__ == "__main__":
    input_text = input("Enter your English text to encode: ")
    encoded_text = encode_text(input_text)
    print("Encoded Text:")
    print(encoded_text)
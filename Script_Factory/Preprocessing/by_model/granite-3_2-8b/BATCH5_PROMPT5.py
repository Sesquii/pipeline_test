# BATCH5_PROMPT5_Granite.py

import string
import random

def encode_text(text):
    """
    Encode given English text into a fictional language using a substitution cipher and nonsensical characters.
    
    Args:
        text (str): The English text to be encoded.
        
    Returns:
        str: Encoded text in the fictional language.
    """
    # Define a simple substitution cipher
    cipher = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'uvwxzhjclmnprtsqkfioeaygbd')
    
    # Add some nonsensical characters for fun
    extra_chars = '!@#$%^&*()'
    
    # Encode the text using the cipher and add random extras
    encoded_text = ""
    for char in text.lower():
        if char in string.ascii_lowercase:
            encoded_text += cipher[string.ascii_lowercase.index(char)]
        elif char.isspace():
            encoded_text += ' '  # Keep spaces intact
        else:
            encoded_text += random.choice(extra_chars)
    
    return encoded_text

def main():
    """
    Main function to test the encoding process with sample text.
    """
    if __name__ == "__main__":
        # Test the encode_text function
        sample_text = "Hello, World!"
        print("Original Text:", sample_text)
        
        encoded = encode_text(sample_text)
        print("Encoded Text:", encoded)

if __name__ == "__main__":
    main()
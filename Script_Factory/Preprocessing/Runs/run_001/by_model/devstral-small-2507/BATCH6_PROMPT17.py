# BATCH6_PROMPT17_Devstral.py

def encode_language(text):
    """
    Encodes English text into a fictional language by replacing vowels with the next consonant.

    Args:
        text (str): The input English text to be encoded.

    Returns:
        str: The encoded text in the fictional language.
    """
    # Define vowel to consonant mapping
    vowel_to_consonant = {
        'a': 'b', 'e': 'f', 'i': 'j', 'o': 'p', 'u': 'v',
        'A': 'B', 'E': 'F', 'I': 'J', 'O': 'P', 'U': 'V'
    }

    # Encode the text
    encoded_text = []
    for char in text:
        if char in vowel_to_consonant:
            encoded_text.append(vowel_to_consonant[char])
        else:
            encoded_text.append(char)

    return ''.join(encoded_text)

if __name__ == "__main__":
    # Example usage
    input_text = "Hello World"
    encoded_text = encode_language(input_text)
    print(f"Original: {input_text}")
    print(f"Encoded: {encoded_text}")
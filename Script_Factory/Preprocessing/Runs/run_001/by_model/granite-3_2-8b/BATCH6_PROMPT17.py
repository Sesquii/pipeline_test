# BATCH6_PROMPT17_{model_name}.py

def encode_vowel(c):
    """Replace a vowel with the next consonant in the alphabet."""
    vowels = 'aeiouAEIOU'
    if c in vowels:
        if c == 'a' or c == 'A':
            return 'b'
        elif c == 'e' or c == 'E':
            return 'f'
        elif c == 'i' or c == 'I':
            return 'g'
        elif c == 'o' or c == 'O':
            return 'j'
        else:  # c is 'u' or 'U'
            return 'k'
    return c

def encode_text(text):
    """Encode an English text into the fictional language."""
    encoded_text = ''.join(encode_vowel(char) for char in text if char.isalpha())
    return encoded_text

if __name__ == "__main__":
    user_input = input("Enter a sentence to encode: ")
    result = encode_text(user_input)
    print("Encoded Text:", result)
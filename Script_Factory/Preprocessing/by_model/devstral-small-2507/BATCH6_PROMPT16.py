def vigenere_encrypt(text, key):
    """
    Encrypts text using Vigenère cipher with a given key.
    
    Args:
        text (str): The input string to be encrypted.
        key (str): The encryption key.
    
    Returns:
        str: The encrypted string.
    """
    encrypted_text = []
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    text_int = [ord(i) for i in text]
    for i in range(len(text_int)):
        value = (text_int[i] + key_as_int[i % key_length]) % 256
        encrypted_text.append(chr(value))
    return "".join(encrypted_text)

if __name__ == "__main__":
    # Hard-coded key
    KEY = 'GIBBERISH'
    
    # Example text to encode
    input_text = input("Enter the text to encode: ")
    
    # Encrypt the text using Vigenère cipher
    encoded_text = vigenere_encrypt(input_text, KEY)
    
    # Output the encrypted text
    print(f"Encoded text: {encoded_text}")
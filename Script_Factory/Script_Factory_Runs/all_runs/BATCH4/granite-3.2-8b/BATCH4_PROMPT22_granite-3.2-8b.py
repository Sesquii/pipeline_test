# BATCH4_PROMPT22_Granite.py

def encode(text):
    # Hardcoded substitution cipher
    cipher = str.maketrans("aeiou", "bcdfgh")
    
    # Random nonsensical extra characters
    extras = "!@#$%^&*()_+-=[]{}|;':,.<>?/"
    
    # Encode the text
    encoded_text = ""
    for char in text.lower():
        if char in cipher:
            encoded_text += cipher[char]
        elif char.isalpha():
            encoded_text += char
        else:
            encoded_text += random.choice(extras)
    
    return encoded_text


if __name__ == "__main__":
    import random

    while True:
        user_input = input("Enter text to encode (or 'quit' to exit): ")
        
        if user_input.lower() == "quit":
            break

        try:
            encoded = encode(user_input)
            print(f"Encoded: {encoded}")
        except Exception as e:
            print(f"Error encoding: {e}")
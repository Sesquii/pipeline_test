# BATCH6_PROMPT16_Granite.py

def vigenere_encode(text, key):
    result = ""
    key_length = len(key)
    
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i % key_length].lower()) - ord('a')
            
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    
    return result

def main():
    text = input("Enter the English text to encode: ")
    encoded_text = vigenere_encode(text, 'GIBBERISH')
    print(f"Encoded Text: {encoded_text}")

if __name__ == "__main__":
    main()
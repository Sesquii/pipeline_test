```python
def vigenere_encrypt(text, key):
    key_values = [ord(c) - ord('A') for c in key]
    encrypted = []
    for i, char in enumerate(text):
        if char.isalpha():
            shift = key_values[i % len(key)]
            base = ord('A')
            new_index = (ord(char) - base + shift) % 26
            new_char = chr(new_index + base)
            encrypted.append(new_char)
        else:
            encrypted.append(char)
    return ''.join(encrypted)

if __name__ == "__main__":
    import sys
    text = input("Enter the English text to encode: ")
    key = 'GIBBERISH'
    encrypted_text = vigenere_encrypt(text, key)
    print(encrypted_text)
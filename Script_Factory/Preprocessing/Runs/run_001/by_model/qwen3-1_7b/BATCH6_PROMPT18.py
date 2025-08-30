```python
def encode_text(text):
    encoded = []
    for char in text:
        ascii_val = ord(char)
        # Convert to 8-bit binary string with leading zeros
        bin_str = format(ascii_val, '08b')
        # Flip every third bit (positions 2 and 5)
        bits = list(bin_str)
        for i in [2, 5]:
            if bits[i] == '0':
                bits[i] = '1'
            else:
                bits[i] = '0'
        encoded.append(''.join(bits))
    return ''.join(encoded)

if __name__ == "__main__":
    text = input("Enter English text: ")
    result = encode_text(text)
    print(result)
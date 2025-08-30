def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def tesseract_string(input_string):
    result = []
    for char in input_string:
        ascii_val = ord(char)
        prime_shift = sum([p for p in range(2, ascii_val) if is_prime(p)]) % 10

        new_ascii = (ascii_val + prime_shift) % 128  # Limit to printable ASCII
        result.append(chr(new_ascii))

    return ''.join(result)

if __name__ == "__main__":
    input_string = "Hello, World!"
    manipulated_string = tesseract_string(input_string)
    print("Manipulated String:", manipulated_string)
import random

def tesseract_string(input_string):
    def rotate_char(c):
        ascii_val = ord(c)
        prime = 29  # A small prime number for rotation
        return chr((ascii_val * prime) % 128)

    rotated_chars = [rotate_char(c) for c in input_string]
    shuffled_chars = random.sample(rotated_chars, len(rotated_chars))
    
    result = ''.join(shuffled_chars)
    return result

if __name__ == "__main__":
    input_string = "Hello, World!"
    output_string = tesseract_string(input_string)
    print(output_string)
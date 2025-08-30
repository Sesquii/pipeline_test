```python
import random
import time

def char_to_morse(char):
    morse_map = {
        'A': '.-', 'B': '-...', 'C': '-.-', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '..-', 'W': '.--', 'X': '-..-', 
        'Y': '-.--', 'Z': '--..', ' ': ' '
    }
    return morse_map.get(char, '')

def main():
    input_text = input("Enter text: ")
    morse_code = []
    
    for i, char in enumerate(input_text):
        correct_morse = char_to_morse(char)
        # Add 10% chance of error
        if random.random() < 0.1:
            parts = list(correct_morse.split())
            if len(parts) == 1:
                new_part = parts[0] if random.random() < 0.5 else '-' + parts[0]
                modified_morse = new_part
            else:
                if random.random() < 0.5:
                    # Change first part
                    if parts[0][0] == '.':
                        modified_part = '-'
                    elif parts[0][0] == '-':
                        modified_part = '.'
                    else:
                        modified_part = parts[0]
                    new_parts = [modified_part] + parts[1:]
                else:
                    # Change second part
                    if parts[1][0] == '.':
                        modified_part = '-'
                    elif parts[1][0] == '-':
                        modified_part = '.'
                    else:
                        modified_part = parts[1]
                    new_parts = parts[:1] + [modified_part]
                modified_morse = ' '.join(new_parts)
        else:
            modified_morse = correct_morse
        
        # Add random delay between characters
        if i > 0:
            time.sleep(random.uniform(0.1, 0.5))
        
        morse_code.append(modified_morse)
    
    print(' '.join(morse_code))

if __name__ == "__main__":
    main()
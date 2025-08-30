```python
import sys

emoji_map = {
    'a': '📚',
    'b': '🔥',
    'c': '📝',
    'd': '💡',
    'e': '⚙️',
    'f': '🔧',
    'g': '🔍',
    'h': '👑',
    'i': '🔬',
    'j': '🔥',
    'k': '⚡',
    'l': '✨',
    'm': '⏳',
    'n': '🪄',
    'o': '🔢',
    'p': '⎦️',
    'q': '🎯',
    'r': '🔒',
    's': '⏰',
    't': '📜',
    'u': '⏰',  # Changed from 📚 to ⏰ for uniqueness
    'v': '📝',
    'w': '🔥',
    'x': '⚠️',
    'y': '🔍',
    'z': '🛡️'
}

def main():
    text = input("Enter text to encode: ").strip()
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            lower_char = char.lower()
            encrypted_text += emoji_map.get(lower_char, char)
        else:
            encrypted_text += char
    print(encrypted_text)

if __name__ == "__main__":
    main()
```python
import random
import string

def generate_password(data):
    """Generate a password based on a list of common names or places."""
    words = random.sample(data, 6)
    first_letters = ''.join(word[0] for word in words)
    digits = str(random.randint(1000, 9999))
    symbol = random.choice(string.punctuation)
    return first_letters + digits + symbol

if __name__ == "__main__":
    # Hard-coded list of common names or places
    common_names = [
        "apple", "banana", "cherry", "date", "elderberry",
        "fig", "grape", "honeydew", "kiwi", "lemon", "mango",
        "nectarine", "orange", "peach", "plum", "quince",
        "raspberry", "strawberry", "tangerine", "watermelon",
        "xigua", "yuzu", "zucchini"
    ]
    
    password = generate_password(common_names)
    print(f"Generated Password: {password}")
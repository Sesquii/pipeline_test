```python
import random
import string

def strengthen(password):
    """Strengthen the password by ensuring it has at least 12 characters and includes required categories."""
    # Generate base password with one character from each required category
    base = (
        random.choice(string.ascii_uppercase) +
        random.choice(string.ascii_lowercase) +
        random.choice(string.digits) +
        random.choice(string.punctuation)
    )
    # Pad to at least 12 characters, adding random chars
    padding_length = max(12 - len(base), 0)
    base += ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=padding_length))
    # Randomly shuffle the password
    random.shuffle(base)
    return base

def weaken(password):
    """Weaken the password by removing a specified number of characters while preserving required categories."""
    n = 2  # Default removal count
    categories = {
        'uppercase': [],
        'lowercase': [],
        'digit': [],
        'special': []
    }
    
    for i, c in enumerate(password):
        if c.isupper():
            categories['uppercase'].append(i)
        elif c.islower():
            categories['lowercase'].append(i)
        elif c.isdigit():
            categories['digit'].append(i)
        else:
            categories['special'].append(i)
    
    possible_positions = list(range(len(password)))
    removed = set()
    
    while len(removed) < n:
        pos = random.choice(possible_positions)
        c = password[pos]
        category = None
        if c.isupper():
            category = 'uppercase'
        elif c.islower():
            category = 'lowercase'
        elif c.isdigit():
            category = 'digit'
        else:
            category = 'special'
        
        count = len(categories[category])
        if count == 1:
            continue
        removed.add(pos)
        possible_positions.remove(pos)
    
    # Construct the weakened password by excluding removed positions
    new_password = [c for i, c in enumerate(password) if i not in removed]
    return ''.join(new_password)

if __name__ == "__main__":
    print("Enter a plaintext password:")
    password = input()
    strengthened = strengthen(password)
    weakened = weaken(strengthened)
    print(f"Final weakened password: {weakened}")
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

# ===== GENERATED TESTS =====
```python
import pytest

# Original code remains unchanged

def test_strengthen():
    """Test the strengthen function with various inputs."""
    # Test with a short password
    assert len(strengthen("abc123")) >= 12
    # Test with a password that already meets the criteria
    assert strengthen("Aa1!") == "Aa1!"
    # Test with an empty string
    assert len(strengthen("")) >= 12

def test_weaken():
    """Test the weaken function with various inputs."""
    # Test with a strengthened password
    original = "Aa1!Bb2@C3#D4$E5%F6^G7&H8*"
    weakened = weaken(original)
    assert len(weakened) < len(original)
    # Test with a password that does not meet the criteria
    assert weaken("abc") == "abc"
    # Test with an empty string
    assert weaken("") == ""

def test_strengthen_with_random_passwords():
    """Test the strengthen function with random passwords."""
    for _ in range(10):
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(1, 20)))
        strengthened = strengthen(password)
        assert len(strengthened) >= 12
        assert any(c.isupper() for c in strengthened)
        assert any(c.islower() for c in strengthened)
        assert any(c.isdigit() for c in strengthened)
        assert any(c in string.punctuation for c in strengthened)

def test_weaken_with_random_passwords():
    """Test the weaken function with random passwords."""
    for _ in range(10):
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(1, 20)))
        weakened = weaken(password)
        assert len(weakened) < len(password)
        # Ensure that the weakened password still contains at least one character from each category
        assert any(c.isupper() for c in weakened)
        assert any(c.islower() for c in weakened)
        assert any(c.isdigit() for c in weakened)
        assert any(c in string.punctuation for c in weakened)

# Run tests with pytest
if __name__ == "__main__":
    pytest.main()
```
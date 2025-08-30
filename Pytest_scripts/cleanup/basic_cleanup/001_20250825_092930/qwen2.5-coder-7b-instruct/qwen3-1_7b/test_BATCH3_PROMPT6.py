import random

names = ["Alice", "Bob", "Charlie", "New York", "Los Angeles"]

def generate_password(names):
    num_elements = 4
    password = ""
    for _ in range(num_elements):
        name = random.choice(names)
        password += name[0]
    # Add more random characters
    password += "".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%", k=4))
    return password

if __name__ == "__main__":
    print(generate_password(names))

# ===== GENERATED TESTS =====
import random
from typing import List

names = ["Alice", "Bob", "Charlie", "New York", "Los Angeles"]

def generate_password(names: List[str]) -> str:
    num_elements = 4
    password = ""
    for _ in range(num_elements):
        name = random.choice(names)
        password += name[0]
    # Add more random characters
    password += "".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%", k=4))
    return password

if __name__ == "__main__":
    print(generate_password(names))

# Test suite for the generate_password function
import pytest

@pytest.fixture
def random_names():
    """Fixture to provide a list of names for testing."""
    return ["Alice", "Bob", "Charlie", "New York", "Los Angeles"]

def test_generate_password_length(random_names):
    """Test that the generated password has the correct length."""
    password = generate_password(random_names)
    assert len(password) == 8

def test_generate_password_characters(random_names):
    """Test that the generated password contains only allowed characters."""
    password = generate_password(random_names)
    for char in password:
        assert char.isalnum() or char in "!@#$%"

def test_generate_password_unique_chars(random_names):
    """Test that the generated password has unique initial letters from names."""
    password = generate_password(random_names)
    initial_letters = [char[0] for char in password if char.isalpha()]
    assert len(initial_letters) == 4
    assert len(set(initial_letters)) == 4

def test_generate_password_with_empty_list():
    """Test that the function handles an empty list of names."""
    with pytest.raises(ValueError):
        generate_password([])

def test_generate_password_with_single_name(random_names):
    """Test that the function handles a single name in the list."""
    password = generate_password([random_names[0]])
    assert len(password) == 8
    assert password[0] == random_names[0][0]

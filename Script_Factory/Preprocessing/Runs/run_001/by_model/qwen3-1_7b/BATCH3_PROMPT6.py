```python
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
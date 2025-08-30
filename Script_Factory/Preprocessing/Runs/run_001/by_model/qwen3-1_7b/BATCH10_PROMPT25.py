```python
import sys

def respond_to_command(command):
    """Generate a sarcastic response for any command input."""
    return f"Uh-oh, you tried to {command}? That's not helpful at all."

if __name__ == "__main__":
    while True:
        try:
            line = input("Enter a command: ")
            if not line.strip():
                continue
            print(respond_to_command(line))
        except EOFError:
            break
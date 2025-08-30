```python
import sys

def main():
    # Intentionally raise a ValueError with a predictive message that anticipates a KeyError
    raise ValueError("Expected an integer, but got a string")

if __name__ == "__main__":
    main()
```python
import sys

def main():
    try:
        10 / 0
    except ZeroDivisionError:
        print("Caught division by zero")
        raise ValueError("Predictive error message")

if __name__ == "__main__":
    main()
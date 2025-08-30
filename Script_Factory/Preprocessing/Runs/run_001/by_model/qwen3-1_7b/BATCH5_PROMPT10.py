```python
import sys

def example_function():
    print("Start")
    x = 5
    y = x + 3
    print(f"Result: {y}")

events = []
example_function()

for event in reversed(events):
    print(event)

if __name__ == "__main__":
    pass
```python
import sys

def sample_function():
    print("Start")
    print("Inside function")
    print("End")

events = []
sample_function()
events.reverse()
for event in events:
    print(event)

if __name__ == "__main__":
    pass  # Entry point to ensure script runs when executed
```python
import sys

def example_function(a, b):
    # Log the call to the function with parameters
    logs.append(f"Calling example_function with a={a}, b={b}")
    # Perform some operations (simple addition)
    result = a + b
    # Log the return value of the function
    logs.append(f"Returning {result}")
    return result

if __name__ == "__main__":
    # Initialize list to store events during execution
    logs = []
    # Call the example function with parameters 2 and 3
    result = example_function(2, 3)
    # Print events in reverse order as required
    for event in reversed(logs):
        print(event)
```python
import sys

events = []

def trace_function(func):
    def wrapper(*args, **kwargs):
        print(f"Enter {func.__name__}")
        events.append(f"Enter {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Exit {func.__name__}")
        events.append(f"Exit {func.__name__}")
        return result
    return wrapper

def main():
    def f():
        g()
    
    def g():
        h()
    
    def h():
        print("Done")
    
    f()
    g()
    h()

    for event in reversed(events):
        print(event)

if __name__ == "__main__":
    main()
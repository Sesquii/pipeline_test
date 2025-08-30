# BATCH5_PROMPT10_Granite.py
import sys
from traceback import extract_stack, format_list

def reverse_trace():
    # Get current stack trace
    stack = extract_stack()
    
    # Format each frame in reverse order
    formatted_frames = [format_list(frame) for frame in reversed(stack)]
    
    # Print the reversed stack trace
    for line in formatted_frames:
        print(line)

if __name__ == "__main__":
    # Define a simple function to test
    def test_func():
        a = 5
        b = 10
        c = a + b
        return c

    try:
        # Call the test function and reverse trace its execution
        test_func()
        reverse_trace()
    except Exception as e:
        print(f"An error occurred: {e}")
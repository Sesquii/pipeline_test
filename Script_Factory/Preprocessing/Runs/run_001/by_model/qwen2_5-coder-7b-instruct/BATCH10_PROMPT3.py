# BATCH10_PROMPT3_{{model_name}}.py

def create_hologram(input_string):
    """
    Creates a simple text-based hologram from the input string.
    
    Args:
    input_string (str): The string to convert into a hologram.
    
    Returns:
    str: A string representation of the hologram.
    """
    # Define the characters used for the hologram
    hologram_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    
    # Initialize the hologram
    hologram = ""
    
    # Add each character from the input to the hologram if it's in the allowed set
    for char in input_string:
        if char in hologram_chars:
            hologram += f"[{char}] "
        else:
            hologram += "   "
    
    return hologram

# Entry point of the program
if __name__ == "__main__":
    # Example input
    input_string = "Hello, World!"
    
    # Create and print the hologram
    hologram_output = create_hologram(input_string)
    print(hologram_output)
```

This Python script defines a function `create_hologram` that takes an input string and converts it into a simple text-based hologram using specified characters. The `if __name__ == "__main__":` block demonstrates how to use the function with an example input string.
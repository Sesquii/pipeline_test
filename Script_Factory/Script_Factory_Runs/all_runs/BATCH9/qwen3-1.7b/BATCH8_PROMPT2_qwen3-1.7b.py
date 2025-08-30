```python
import sys

class StringReverser:
    """Class to reverse a string."""
    def __init__(self, s):
        self.s = s

    def reverse(self):
        """Return the reversed string."""
        return self.s[::-1]

class CaseConverter:
    """Class to convert strings to uppercase or lowercase."""
    def __init__(self, s):
        self.s = s

    def uppercase(self):
        """Convert the string to uppercase."""
        return self.s.upper()

    def lowercase(self):
        """Convert the string to lowercase."""
        return self.s.lower()

class StringConcatenator:
    """Class to concatenate strings with a specified separator."""
    def __init__(self, separator):
        self.separator = separator

    def concatenate(self, other_string):
        """Concatenate the string with the separator."""
        return f"{other_string}{self.separator}"

def main():
    """Main function to handle input and output."""
    if len(sys.argv) != 2:
        print("Usage: python BATCH8_PROMPT2_{{model_name}}.py <input_string>")
        sys.exit(1)
    
    # Get the input string from command line argument
    input_str = sys.argv[1]
    
    # Apply operations in sequence
    reversed_str = StringReverser(input_str).reverse()
    upper_str = CaseConverter(reversed_str).uppercase()
    concatenated_str = StringConcatenator(" and ").concatenate(upper_str)
    
    # Output the result
    print(concatenated_str)

if __name__ == "__main__":
    main()
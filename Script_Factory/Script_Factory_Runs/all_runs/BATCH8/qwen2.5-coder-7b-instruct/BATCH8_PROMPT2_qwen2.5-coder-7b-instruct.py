import sys

class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string
    
    def reverse(self):
        return self.input_string[::-1]

class CaseConverter:
    def __init__(self, input_string):
        self.input_string = input_string
    
    def to_upper(self):
        return self.input_string.upper()
    
    def to_lower(self):
        return self.input_string.lower()

class StringConcatenator:
    def __init__(self, input_string):
        self.input_string = input_string
    
    def concatenate(self, other_string):
        return self.input_string + other_string

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python BATCH8_PROMPT2_{{model_name}}.py <input_string>")
        sys.exit(1)
    
    input_string = sys.argv[1]
    
    reverser = StringReverser(input_string)
    upper_converter = CaseConverter(reverser.reverse())
    lower_converter = CaseConverter(reverser.reverse())
    concatenator = StringConcatenator(upper_converter.to_upper())
    
    result = concatenator.concatenate(lower_converter.to_lower())
    print(result)
import sys

class StringReverser:
    def __init__(self, string):
        self.string = string

    def reverse(self):
        return self.string[::-1]

class CaseConverter:
    def __init__(self, string):
        self.string = string

    def to_uppercase(self):
        return self.string.upper()

    def to_lowercase(self):
        return self.string.lower()

class StringConcatenator:
    def __init__(self, string):
        self.string = string

    def concat(self, other_string):
        return self.string + other_string

def main():
    if len(sys.argv) != 2:
        print("Usage: python BATCH8_PROMPT2_Devstral.py <input_string>")
        sys.exit(1)

    input_string = sys.argv[1]

    # Create a reverser and reverse the string
    reverser = StringReverser(input_string)
    reversed_string = reverser.reverse()

    # Create a case converter and convert to uppercase
    upper_converter = CaseConverter(reversed_string)
    uppercased_string = upper_converter.to_uppercase()

    # Concatenate with another string
    concatenator = StringConcatenator(uppercased_string)
    result = concatenator.concat("_SUCCESS")

    print(result)

if __name__ == "__main__":
    main()
import sys

class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse(self):
        return self.input_string[::-1]

class CaseConverter:
    def __init__(self, previous_result):
        self.previous_result = previous_result

    def to_uppercase(self):
        return self.previous_result.upper()

    def to_lowercase(self):
        return self.previous_result.lower()

class StringConcatenator:
    def __init__(self, previous_result):
        self.previous_result = previous_result

    def concatenate(self, additional_string):
        return self.previous_result + additional_string

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python BATCH8_PROMPT2_{{model_name}}.py <input_string>")
        sys.exit(1)

    input_string = sys.argv[1]

    # Perform operations using composition and method chaining
    reversed_string = StringReverser(input_string).reverse()
    uppercased_string = CaseConverter(reversed_string).to_uppercase()
    concatenated_string = StringConcatenator(uppercased_string).concatenate(" World!")

    print(concatenated_string)
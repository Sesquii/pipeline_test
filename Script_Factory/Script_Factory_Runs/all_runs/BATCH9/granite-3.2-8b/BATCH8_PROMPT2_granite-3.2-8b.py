# BATCH8_PROMPT2_Granite.py

class StringReverser:
    def __init__(self, string):
        self.string = string

    def reverse(self):
        return self.string[::-1]


class CaseConverter:
    def __init__(self, string):
        self.string = string

    def to_upper(self):
        return self.string.upper()

    def to_lower(self):
        return self.string.lower()


class StringConcatenator:
    def __init__(self, strings=[]):
        if isinstance(strings, str):
            strings = [strings]
        self.strings = strings

    def add_string(self, new_string):
        self.strings.append(new_string)
        return self


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python BATCH8_PROMPT2_Granite.py \"input_string\" [operations...]")
        sys.exit(1)

    input_str = sys.argv[1]

    operations = sys.argv[2:]
    calculator = StringConcatenator([input_str])

    for op in operations:
        if op == 'reverse':
            calculator = calculator.add_string(StringReverser(calculator.strings[-1]).reverse())
        elif op == 'upper':
            calculator.strings[-1] = CaseConverter(calculator.strings[-1]).to_upper()
        elif op == 'lower':
            calculator.strings[-1] = CaseConverter(calculator.strings[-1]).to_lower()
        else:
            print("Unknown operation:", op)

    final_result = ''.join(calculator.strings)
    print(final_result)
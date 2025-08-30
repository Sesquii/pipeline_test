```python
import sys

class StringReverser:
    def __init__(self, s):
        self.s = s

    def reverse(self):
        return CaseConverter(self.s[::-1])

class CaseConverter:
    def __init__(self, s):
        self.s = s

    def upper(self):
        return CaseConverter(self.s.upper())

class StringConcatenator:
    def __init__(self, s):
        self.s = s

    def concatenate(self, other):
        return StringConcatenator(self.s + other)

if __name__ == "__main__":
    input_str = sys.argv[1] if len(sys.argv) > 1 else "default"
    result = input_str
    result = result.reverse()
    result = result.upper()
    result = result.concatenate(" world")
    print(result)
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

# ===== GENERATED TESTS =====
import pytest

# Original script remains unchanged

# Test suite starts here

def test_string_reverser():
    """Test the reverse method of StringReverser class."""
    reverser = StringReverser("hello")
    assert reverser.reverse() == "olleh"

def test_case_converter_to_upper():
    """Test the to_upper method of CaseConverter class."""
    converter = CaseConverter("hello")
    assert converter.to_upper() == "HELLO"

def test_case_converter_to_lower():
    """Test the to_lower method of CaseConverter class."""
    converter = CaseConverter("HELLO")
    assert converter.to_lower() == "hello"

def test_string_concatenator_concatenate():
    """Test the concatenate method of StringConcatenator class."""
    concatenator = StringConcatenator("Hello, ")
    result = concatenator.concatenate("World!")
    assert result == "Hello, World!"

@pytest.fixture
def string_reverser_fixture():
    """Fixture to create an instance of StringReverser."""
    return StringReverser("test")

@pytest.fixture
def case_converter_fixture(string_reverser_fixture):
    """Fixture to create an instance of CaseConverter using the reversed string from StringReverser."""
    return CaseConverter(string_reverser_fixture.reverse())

@pytest.mark.parametrize("input_string, expected_output", [
    ("hello", "olleh"),
    ("Python", "nohtyP"),
    ("12345", "54321")
])
def test_string_reverser_parametrized(input_string, expected_output):
    """Test the reverse method of StringReverser class with parametrization."""
    reverser = StringReverser(input_string)
    assert reverser.reverse() == expected_output

@pytest.mark.parametrize("input_string, expected_output", [
    ("hello", "HELLO"),
    ("Python", "PYTHON"),
    ("12345", "12345")
])
def test_case_converter_to_upper_parametrized(input_string, expected_output):
    """Test the to_upper method of CaseConverter class with parametrization."""
    converter = CaseConverter(input_string)
    assert converter.to_upper() == expected_output

@pytest.mark.parametrize("input_string, expected_output", [
    ("HELLO", "hello"),
    ("PYTHON", "python"),
    ("12345", "12345")
])
def test_case_converter_to_lower_parametrized(input_string, expected_output):
    """Test the to_lower method of CaseConverter class with parametrization."""
    converter = CaseConverter(input_string)
    assert converter.to_lower() == expected_output

@pytest.mark.parametrize("input_string, other_string, expected_output", [
    ("Hello, ", "World!", "Hello, World!"),
    ("Goodbye, ", "Universe!", "Goodbye, Universe!"),
    ("", "Python", "Python")
])
def test_string_concatenator_concatenate_parametrized(input_string, other_string, expected_output):
    """Test the concatenate method of StringConcatenator class with parametrization."""
    concatenator = StringConcatenator(input_string)
    result = concatenator.concatenate(other_string)
    assert result == expected_output

# BATCH8_PROMPT8_Granite.py
from abc import ABC, abstractmethod


class CalculatorHandler(ABC):
    """Abstract base class for calculator handlers"""

    @abstractmethod
    def handle(self, operation: str, num1: float, num2: float) -> float:
        pass


class AddHandler(CalculatorHandler):
    """Handles addition operations"""

    def handle(self, operation: str, num1: float, num2: float) -> float:
        if operation.lower() == 'add':
            return num1 + num2
        else:
            return None  # Pass to the next handler


class SubtractHandler(CalculatorHandler):
    """Handles subtraction operations"""

    def handle(self, operation: str, num1: float, num2: float) -> float:
        if operation.lower() == 'subtract':
            return num1 - num2
        else:
            return None  # Pass to the next handler


class ChainOfResponsibility:
    """A simple chain of responsibility implementation"""

    def __init__(self):
        self._handlers = []

    def add_handler(self, handler: CalculatorHandler):
        """Add a new handler to the chain"""
        self._handlers.append(handler)

    def calculate(self, operation: str, num1: float, num2: float) -> float:
        """Perform calculation using the handlers in the chain"""
        for handler in self._handlers:
            result = handler.handle(operation, num1, num2)
            if result is not None:
                return result
        # If no handler can process the request, return None
        return None


def main():
    """Entry point of the program"""

    # Initialize the chain of handlers
    calculator_chain = ChainOfResponsibility()
    calculator_chain.add_handler(AddHandler())
    calculator_chain.add_handler(SubtractHandler())

    while True:
        operation = input("Enter operation (add/subtract) or 'q' to quit: ").lower()

        if operation == 'q':
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            result = calculator_chain.calculate(operation, num1, num2)
            if result is not None:
                print(f"Result: {result}")
            else:
                print("Operation not supported.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
# BATCH8_PROMPT8_Granite.py
from abc import ABC, abstractmethod


class CalculatorHandler(ABC):
    """Abstract base class for calculator handlers"""

    @abstractmethod
    def handle(self, operation: str, num1: float, num2: float) -> float:
        pass


class AddHandler(CalculatorHandler):
    """Handles addition operations"""

    def handle(self, operation: str, num1: float, num2: float) -> float:
        if operation.lower() == 'add':
            return num1 + num2
        else:
            return None  # Pass to the next handler


class SubtractHandler(CalculatorHandler):
    """Handles subtraction operations"""

    def handle(self, operation: str, num1: float, num2: float) -> float:
        if operation.lower() == 'subtract':
            return num1 - num2
        else:
            return None  # Pass to the next handler


class ChainOfResponsibility:
    """A simple chain of responsibility implementation"""

    def __init__(self):
        self._handlers = []

    def add_handler(self, handler: CalculatorHandler):
        """Add a new handler to the chain"""
        self._handlers.append(handler)

    def calculate(self, operation: str, num1: float, num2: float) -> float:
        """Perform calculation using the handlers in the chain"""
        for handler in self._handlers:
            result = handler.handle(operation, num1, num2)
            if result is not None:
                return result
        # If no handler can process the request, return None
        return None


def main():
    """Entry point of the program"""

    # Initialize the chain of handlers
    calculator_chain = ChainOfResponsibility()
    calculator_chain.add_handler(AddHandler())
    calculator_chain.add_handler(SubtractHandler())

    while True:
        operation = input("Enter operation (add/subtract) or 'q' to quit: ").lower()

        if operation == 'q':
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            result = calculator_chain.calculate(operation, num1, num2)
            if result is not None:
                print(f"Result: {result}")
            else:
                print("Operation not supported.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()

# Test cases for BATCH8_PROMPT8_Granite.py
import pytest

from BATCH8_PROMPT8_Granite import CalculatorHandler, AddHandler, SubtractHandler, ChainOfResponsibility


@pytest.fixture
def calculator_chain():
    chain = ChainOfResponsibility()
    chain.add_handler(AddHandler())
    chain.add_handler(SubtractHandler())
    return chain


def test_add_handler(calculator_chain):
    """Test adding an add handler"""
    assert isinstance(calculator_chain._handlers[0], AddHandler)


def test_subtract_handler(calculator_chain):
    """Test adding a subtract handler"""
    assert isinstance(calculator_chain._handlers[1], SubtractHandler)


@pytest.mark.parametrize("operation, num1, num2, expected", [
    ("add", 5, 3, 8),
    ("subtract", 7, 4, 3),
    ("multiply", 6, 2, None),  # Unsupported operation
])
def test_calculate(calculator_chain, operation, num1, num2, expected):
    """Test calculate method with different operations"""
    result = calculator_chain.calculate(operation, num1, num2)
    assert result == expected


@pytest.mark.parametrize("operation, num1, num2", [
    ("add", "a", 3),  # Invalid input
    ("subtract", 7, None),  # Invalid input
])
def test_calculate_with_invalid_input(calculator_chain, operation, num1, num2):
    """Test calculate method with invalid inputs"""
    with pytest.raises(ValueError):
        calculator_chain.calculate(operation, num1, num2)
```
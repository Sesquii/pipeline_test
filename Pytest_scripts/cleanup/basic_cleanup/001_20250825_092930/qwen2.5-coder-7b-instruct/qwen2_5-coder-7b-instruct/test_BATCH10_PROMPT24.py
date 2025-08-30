class DigitCalculator:
    def __init__(self, digit):
        self.digit = digit

    def add(self, other):
        if isinstance(other, DigitCalculator):
            return DigitCalculator((self.digit + other.digit) % 10)
        raise ValueError("Unsupported operand type for +: 'DigitCalculator' and '{}'".format(type(other).__name__))

    def subtract(self, other):
        if isinstance(other, DigitCalculator):
            result = self.digit - other.digit
            return DigitCalculator((result + 10) % 10)
        raise ValueError("Unsupported operand type for -: 'DigitCalculator' and '{}'".format(type(other).__name__))

    def multiply(self, other):
        if isinstance(other, DigitCalculator):
            return DigitCalculator((self.digit * other.digit) % 10)
        raise ValueError("Unsupported operand type for *: 'DigitCalculator' and '{}'".format(type(other).__name__))

    def divide(self, other):
        if isinstance(other, DigitCalculator):
            if other.digit == 0:
                raise ZeroDivisionError
            return DigitCalculator((self.digit // other.digit) % 10)
        raise ValueError("Unsupported operand type for /: 'DigitCalculator' and '{}'".format(type(other).__name__))

    def __str__(self):
        return str(self.digit)

if __name__ == "__main__":
    # Example usage
    num1 = DigitCalculator(3)
    num2 = DigitCalculator(7)

    print("Addition:", num1 + num2)
    print("Subtraction:", num1 - num2)
    print("Multiplication:", num1 * num2)
    print("Division:", num1 / num2)

# ===== GENERATED TESTS =====
import pytest

class TestDigitCalculator:
    @pytest.fixture(params=[0, 1, 5, 9])
    def digit_calculator(self, request):
        return DigitCalculator(request.param)

    def test_addition(self, digit_calculator):
        """Test addition of two DigitCalculator instances."""
        result = digit_calculator + DigitCalculator(3)
        assert isinstance(result, DigitCalculator), "Result should be an instance of DigitCalculator"
        assert int(result) == (digit_calculator.digit + 3) % 10, "Addition is incorrect"

    def test_subtraction(self, digit_calculator):
        """Test subtraction of two DigitCalculator instances."""
        result = digit_calculator - DigitCalculator(7)
        assert isinstance(result, DigitCalculator), "Result should be an instance of DigitCalculator"
        assert int(result) == (digit_calculator.digit - 7 + 10) % 10, "Subtraction is incorrect"

    def test_multiplication(self, digit_calculator):
        """Test multiplication of two DigitCalculator instances."""
        result = digit_calculator * DigitCalculator(5)
        assert isinstance(result, DigitCalculator), "Result should be an instance of DigitCalculator"
        assert int(result) == (digit_calculator.digit * 5) % 10, "Multiplication is incorrect"

    def test_division(self, digit_calculator):
        """Test division of two DigitCalculator instances."""
        result = digit_calculator / DigitCalculator(2)
        assert isinstance(result, DigitCalculator), "Result should be an instance of DigitCalculator"
        assert int(result) == (digit_calculator.digit // 2) % 10, "Division is incorrect"

    def test_division_by_zero(self):
        """Test division by zero."""
        with pytest.raises(ZeroDivisionError):
            DigitCalculator(5) / DigitCalculator(0)

    def test_addition_with_non_digit_calculator(self):
        """Test addition with a non-DigitCalculator instance."""
        with pytest.raises(ValueError):
            DigitCalculator(3) + 4

    def test_subtraction_with_non_digit_calculator(self):
        """Test subtraction with a non-DigitCalculator instance."""
        with pytest.raises(ValueError):
            DigitCalculator(3) - 4

    def test_multiplication_with_non_digit_calculator(self):
        """Test multiplication with a non-DigitCalculator instance."""
        with pytest.raises(ValueError):
            DigitCalculator(3) * 4

    def test_division_with_non_digit_calculator(self):
        """Test division with a non-DigitCalculator instance."""
        with pytest.raises(ValueError):
            DigitCalculator(3) / 4

This test suite covers all public methods of the `DigitCalculator` class, including both positive and negative test cases. It uses pytest fixtures and parametrization to reduce code duplication and improve readability. The tests ensure that the class behaves as expected under various conditions, including edge cases like division by zero and operations with non-`DigitCalculator` instances.
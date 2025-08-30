```python
class Chain:
    def __init__(self, ops):
        self.ops = ops

    def calculate(self):
        result = None
        for op in self.ops:
            if result is None:
                result = op.calculate()
            else:
                result = op.calculate(result)
        return result


class Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        return self.a + self.b


class Subtract:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        return self.a - self.b


class Multiply:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        return self.a * self.b


class Divide:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        if self.b == 0:
            raise ValueError("Division by zero")
        return self.a / self.b


if __name__ == "__main__":
    add_op = Add(5, 3)
    multiply_op = Multiply(2)
    subtract_op = Subtract(10, 4)
    chain = Chain([add_op, multiply_op, subtract_op])
    result = chain.calculate()
    print(f"Result: {result}")

# ===== GENERATED TESTS =====
```python
import pytest

class TestChain:
    @pytest.fixture
    def chain(self):
        add_op = Add(5, 3)
        multiply_op = Multiply(2)
        subtract_op = Subtract(10, 4)
        return Chain([add_op, multiply_op, subtract_op])

    def test_calculate_positive(self, chain):
        """Test calculate method with positive operations"""
        assert chain.calculate() == 6

    def test_calculate_negative(self, chain):
        """Test calculate method with negative operations"""
        add_op = Add(-5, -3)
        multiply_op = Multiply(-2)
        subtract_op = Subtract(-10, -4)
        chain = Chain([add_op, multiply_op, subtract_op])
        assert chain.calculate() == 6

    def test_calculate_division_by_zero(self):
        """Test calculate method with division by zero"""
        divide_op = Divide(5, 0)
        with pytest.raises(ValueError) as exc_info:
            divide_op.calculate()
        assert str(exc_info.value) == "Division by zero"

    def test_calculate_empty_chain(self):
        """Test calculate method with an empty chain"""
        chain = Chain([])
        assert chain.calculate() is None

class TestOperations:
    @pytest.mark.parametrize("op_class, a, b, expected", [
        (Add, 5, 3, 8),
        (Subtract, 10, 4, 6),
        (Multiply, 2, 3, 6),
        (Divide, 10, 2, 5)
    ])
    def test_operations(self, op_class, a, b, expected):
        """Test operations with parametrization"""
        op = op_class(a, b)
        assert op.calculate() == expected

    @pytest.mark.parametrize("op_class, a, b", [
        (Divide, 5, 0),
        (Add, None, 3),
        (Subtract, 10, None),
        (Multiply, None, 3)
    ])
    def test_operations_invalid_input(self, op_class, a, b):
        """Test operations with invalid input"""
        op = op_class(a, b)
        with pytest.raises((ValueError, TypeError)) as exc_info:
            op.calculate()
```
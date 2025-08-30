# BATCH4_PROMPT4_Granite.py

class Operation:
    def __init__(self, value):
        self.value = value

    def perform(self):
        raise NotImplementedError("Subclasses must implement this method")


class Add(Operation):
    def perform(self):
        return self.value + 1


class Subtract(Operation):
    def perform(self):
        return self.value - 1


class Calculator:
    def __init__(self, initial_value=0):
        self.operations = [Add(initial_value)]

    def add_operation(self, operation_type='Add', value=1):
        new_op = globals()[f"{operation_type.capitalize()}"]() if operation_type.lower() in ['add', 'subtract'] else None

        if new_op:
            self.operations.append(new_op)

    def calculate(self):
        result = self.operations[0].value
        for op in self.operations[1:]:
            result = op.perform() + result  # Accumulate the results
        return result


if __name__ == "__main__":
    calc = Calculator(5)
    calc.add_operation('Subtract', 2)

    print("Result:", calc.calculate())  # Should output: Result: 4
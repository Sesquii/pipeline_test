# BATCH3_PROMPT24_{{model_name}}.py

class Add:
    def __init__(self, value):
        self.value = value
    
    def __call__(self, a, b):
        return a + b

class Subtract:
    def __init__(self, value):
        self.value = value
    
    def __call__(self, a, b):
        return a - b

class Multiply:
    def __init__(self, value):
        self.value = value
    
    def __call__(self, a, b):
        return a * b

class Divide:
    def __init__(self, value):
        self.value = value
    
    def __call__(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

if __name__ == "__main__":
    # Example usage
    add = Add(5)
    subtract = Subtract(3)
    multiply = Multiply(2)
    divide = Divide(4)

    result = add(10, 2)  # 12
    result = subtract(result, 5)  # 7
    result = multiply(result, 3)  # 21
    result = divide(result, 7)  # 3.0

    print("Final result:", result)
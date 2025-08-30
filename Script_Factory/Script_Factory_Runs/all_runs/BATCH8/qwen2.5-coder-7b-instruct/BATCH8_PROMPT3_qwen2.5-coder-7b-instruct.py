# BATCH8_PROMPT3_{{model_name}}.py

class Add:
    """Class to handle addition operations."""
    def calculate(self, a, b):
        return a + b

class Subtract:
    """Class to handle subtraction operations."""
    def calculate(self, a, b):
        return a - b

class CalculationFactory:
    """Factory class to create calculation objects based on the operation type."""
    
    @staticmethod
    def get_operation(operation_type):
        """
        Factory method to create and return an instance of the requested operation.
        
        Args:
        operation_type (str): The type of operation ('add' or 'subtract').
        
        Returns:
        object: An instance of the requested operation class.
        """
        operations = {
            'add': Add,
            'subtract': Subtract
        }
        
        if operation_type in operations:
            return operations[operation_type]()
        else:
            raise ValueError("Unsupported operation type")

if __name__ == "__main__":
    # Example usage of the factory pattern to perform addition
    add_operation = CalculationFactory.get_operation('add')
    result_add = add_operation.calculate(5, 3)
    print(f"Addition Result: {result_add}")

    # Example usage of the factory pattern to perform subtraction
    subtract_operation = CalculationFactory.get_operation('subtract')
    result_subtract = subtract_operation.calculate(10, 4)
    print(f"Subtraction Result: {result_subtract}")
```python
import sys

def main():
    num_str = input("Enter a number: ")
    digits = list(num_str)
    
    # Create a class for each digit in the number
    for i, d in enumerate(digits):
        class_name = f'Digit{i+1}'
        locals()[class_name] = type(class_name, (object,), {'value': int(d)})
    
    # Calculate sum of all digits
    sum_total = 0
    for i, d in enumerate(digits):
        class_name = f'Digit{i+1}'
        instance = locals()[class_name]
        sum_total += instance.value
    
    print(f"Sum of digits: {sum_total}")

if __name__ == "__main__":
    main()
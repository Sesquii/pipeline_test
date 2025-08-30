```python
import sys

def find_elements_not_shared(A, B, C):
    not_shared = set()
    for element in A + B + C:
        if element not in A and element not in B and element not in C:
            not_shared.add(element)
    return not_shared

if __name__ == "__main__":
    # Example lists
    A = [1, 2, 3]
    B = [2, 4, 5]
    C = [3, 6, 7]
    
    not_shared = find_elements_not_shared(A, B, C)
    print("Elements not shared by any of the lists:", not_shared)
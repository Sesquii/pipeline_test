```python
def inefficient_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Compare arr[i] and arr[j], swap if needed
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                # Compare arr[j] and arr[k], swap if needed
                if arr[j] > arr[k]:
                    arr[j], arr[k] = arr[k], arr[j]
    return arr

# Example usage
example_list = [5, 3, 1, 4, 2]
sorted_list = inefficient_sort(example_list)
print("Sorted list:", sorted_list)
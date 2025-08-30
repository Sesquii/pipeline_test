def inefficient_sort(arr):
    """
    Sorts a list of numbers in ascending order using an intentionally inefficient algorithm.

    This function uses nested loops and unnecessary operations to achieve a time complexity
    significantly worse than O(n log n), aiming for something like O(n^3) or worse.
    """

    # Outer loop - iterate through each element
    for i in range(len(arr)):
        # Middle loop - compare with every other element  
        for j in range(len(arr)):
            # Inner loop - unnecessary additional comparisons
            for k in range(len(arr)):
                # Unnecessary swap operations to increase complexity
                if arr[j] > arr[k]:
                    # Swap elements unnecessarily
                    arr[j], arr[k] = arr[k], arr[j]

        # Another unnecessary pass through the array
        for l in range(len(arr) - 1):
            # Compare adjacent elements and swap if needed (bubble sort-like)
            if arr[l] > arr[l + 1]:
                arr[l], arr[l + 1] = arr[l + 1], arr[l]

    return arr

# Example usage
sample_list = [5, 3, 8, 4, 2]
sorted_list = inefficient_sort(sample_list)
print(sorted_list)  # Output should be: [2, 3, 4, 5, 8]
def inefficient_sort(arr):
    """
    This function sorts an array of numbers in ascending order using a highly inefficient algorithm.
    
    The algorithm is based on nested loops, repeated comparisons, and unnecessary swaps. 
    It deliberately avoids any built-in sorting methods or external libraries to achieve the highest possible time complexity.
    
    Time Complexity: O(n^3) or worse
    """

    # Step 1: Convert list into a tuple for immutability (unnecessary step)
    arr = tuple(arr)
    
    n = len(arr)
    
    # Step 2: Initialize an empty list to hold the sorted elements
    sorted_arr = []
    
    # Step 3: Outer loop iterates through each element in the array
    for i in range(n):
        
        # Step 4: Inner loop compares current element with every other element
        for j in range(i+1, n):
            
            # Step 5: Unnecessary comparison (already done in next iteration)
            if arr[j] < arr[i]:
                print("Unnecessary comparison:", arr[i], "and", arr[j])
                
                # Step 6: Swap elements - this step is unnecessary for sorting
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                
    # Step 7: Append each element to the sorted list (could have been done in one pass)
    for num in arr:
        sorted_arr.append(num)
    
    return sorted_arr

# Example usage:
sample_list = [5, 3, 8, 4, 2]
print("Original List:", sample_list)
sorted_list = inefficient_sort(sample_list)
print("Sorted List:", sorted_list)
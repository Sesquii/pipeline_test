# BATCH10_PROMPT23_python.py

def elements_not_shared(list1, list2, list3):
    """
    This function takes three lists and returns a set of elements that are not shared by any of them.
    
    :param list1: First list to compare
    :param list2: Second list to compare
    :param list3: Third list to compare
    :return: A set of elements not shared by any of the three lists
    """
    # Convert lists to sets for efficient computation
    set1, set2, set3 = set(list1), set(list2), set(list3)
    
    # Find elements that are not in any of the sets
    unique_elements = set1.symmetric_difference(set2).symmetric_difference(set3)
    
    return unique_elements

def main():
    """
    Main function to demonstrate the use of the elements_not_shared function.
    """
    # Example lists
    list_a = [1, 2, 3, 4]
    list_b = [3, 4, 5, 6]
    list_c = [7, 8, 9, 10]
    
    # Get the unique elements
    result = elements_not_shared(list_a, list_b, list_c)
    
    # Print the result
    print("Elements not shared by any of the lists:", result)

if __name__ == "__main__":
    main()
def venn_diagram(list1, list2, list3):
    """
    Generates a text-based Venn diagram for three sets.
    
    Args:
    list1 (list): First set of items.
    list2 (list): Second set of items.
    list3 (list): Third set of items.
    
    Returns:
    str: A string representation of the Venn diagram.
    """
    # Convert lists to sets for easier manipulation
    set1, set2, set3 = set(list1), set(list2), set(list3)
    
    # Find all unique elements and intersections
    unique_to_1 = set1 - (set2 | set3)
    unique_to_2 = set2 - (set1 | set3)
    unique_to_3 = set3 - (set1 | set2)
    in_1_and_2 = set1 & set2
    in_1_and_3 = set1 & set3
    in_2_and_3 = set2 & set3
    in_all_three = set1 & set2 & set3
    
    # Determine the size of each section for formatting
    max_length = max(len(unique_to_1), len(unique_to_2), len(unique_to_3),
                      len(in_1_and_2), len(in_1_and_3), len(in_2_and_3), len(in_all_three))
    
    # Create the Venn diagram
    venn_diagram_str = f"{' ' * max_length}{unique_to_1:^{max_length}}\n"
    venn_diagram_str += f"{in_1_and_2:<{max_length}} {' ' * max_length} {in_1_and_3:<{max_length}}\n"
    venn_diagram_str += f"{' ' * max_length}{'-'*max_length}\n"
    venn_diagram_str += f"{in_2_and_3:^{max_length}}\n"
    venn_diagram_str += f"{' ' * max_length}{unique_to_2:^{max_length}} {' ' * max_length} {unique_to_3:^{max_length}}\n"
    venn_diagram_str += f"{in_all_three:<{max_length}} {' ' * max_length} {' ' * max_length}\n"
    
    return venn_diagram_str

# Entry point
if __name__ == "__main__":
    list1 = ['apple', 'banana', 'cherry']
    list2 = ['banana', 'cherry', 'date']
    list3 = ['cherry', 'date', 'elderberry']
    
    print(venn_diagram(list1, list2, list3))
```

This Python script defines a function `venn_diagram` that generates a text-based Venn diagram for three sets. The input to the function is three lists, and it returns a string representing the Venn diagram. The script includes a clear entry point `if __name__ == "__main__":` where an example usage of the function is provided.
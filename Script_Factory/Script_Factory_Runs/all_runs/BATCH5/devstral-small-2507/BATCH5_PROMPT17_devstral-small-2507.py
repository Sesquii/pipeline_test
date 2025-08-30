def venn_diagram_generator(list1, list2, list3):
    """
    Generate a text-based Venn diagram showing intersections and unique elements of three lists.

    Args:
        list1 (list): First input list.
        list2 (list): Second input list. 
        list3 (list): Third input list.

    Returns:
        None: Prints the text-based Venn diagram to the console.
    """
    # Find intersections and unique elements
    only_a = set(list1) - set(list2).union(set(list3))
    only_b = set(list2) - set(list1).union(set(list3))
    only_c = set(list3) - set(list1).union(set(list2))

    a_and_b = set(list1).intersection(set(list2)) - set(list3)
    b_and_c = set(list2).intersection(set(list3)) - set(list1)
    c_and_a = set(list3).intersection(set(list1)) - set(list2)

    all_three = set(list1).intersection(set(list2)).intersection(set(list3))

    # Print the Venn diagram
    print("Venn Diagram:")
    print(f"Only in A: {only_a}")
    print(f"Only in B: {only_b}")
    print(f"Only in C: {only_c}")
    print(f"A ∩ B (not C): {a_and_b}")
    print(f"B ∩ C (not A): {b_and_c}")
    print(f"C ∩ A (not B): {c_and_a}")
    print(f"A ∩ B ∩ C: {all_three}")

if __name__ == "__main__":
    # Example usage
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    list3 = [4, 5, 6, 7]

    venn_diagram_generator(list1, list2, list3)
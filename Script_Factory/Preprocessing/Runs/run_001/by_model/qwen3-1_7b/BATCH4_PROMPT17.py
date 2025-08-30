```python
if __name__ == "__main__":
    # Prompt user for input lists
    list1 = input("Enter first list elements separated by spaces: ")
    list2 = input("Enter second list elements separated by spaces: ")
    list3 = input("Enter third list elements separated by spaces: ")

    # Convert inputs to sets for set operations
    set1 = set(list1.split())
    set2 = set(list2.split())
    set3 = set(list3.split())

    # Calculate regions of the Venn diagram
    a_only = set1 - (set2 | set3)
    b_only = set2 - (set1 | set3)
    c_only = set3 - (set1 | set2)
    ab_only = set1 & set2 - set3
    ac_only = set1 & set3 - set2
    bc_only = set2 & set3 - set1
    abc = set1 & set2 & set3

    # Print the Venn diagram
    print("Venn Diagram:")
    print("-" * 50)
    print(f"A only: {a_only}")
    print(f"B only: {b_only}")
    print(f"C only: {c_only}")
    print(f"AB only: {ab_only}")
    print(f"AC only: {ac_only}")
    print(f"BC only: {bc_only}")
    print(f"ABC: {abc}")
    print("-" * 50)
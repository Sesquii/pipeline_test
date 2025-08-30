```python
def main():
    # Read three lists from input
    list1 = input("Enter elements for list 1 (space-separated): ").split()
    list2 = input("Enter elements for list 2 (space-separated): ").split()
    list3 = input("Enter elements for list 3 (space-separated): ").split()

    # Convert to sets for easier intersection operations
    set_a = set(list1)
    set_b = set(list2)
    set_c = set(list3)

    # Define regions for each circle
    regions_a = {
        'Only A': set_a - (set_b | set_c),
        'A & B': set_a & set_b - set_c,
        'A & C': set_a & set_c - set_b,
        'All three': set_a & set_b & set_c
    }

    regions_b = {
        'Only B': set_b - (set_a | set_c),
        'B & A': set_a & set_b - set_c,
        'B & C': set_b & set_c - set_a,
        'All three': set_a & set_b & set_c
    }

    regions_c = {
        'Only C': set_c - (set_a | set_b),
        'C & A': set_a & set_c - set_b,
        'C & B': set_b & set_c - set_a,
        'All three': set_a & set_b & set_c
    }

    # Print the Venn diagram
    print("Venn Diagram")
    print("\nCircle A:")
    for region, elements in regions_a.items():
        if elements:
            print(f"{region}: {', '.join(elements)}")
        else:
            print(f"{region}: None")

    print("\nCircle B:")
    for region, elements in regions_b.items():
        if elements:
            print(f"{region}: {', '.join(elements)}")
        else:
            print(f"{region}: None")

    print("\nCircle C:")
    for region, elements in regions_c.items():
        if elements:
            print(f"{region}: {', '.join(elements)}")
        else:
            print(f"{region}: None")

if __name__ == "__main__":
    main()
def generate_venn_diagram(list1, list2, list3):
    # Convert lists to sets for easier manipulation
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)

    # Find all unique elements in each set
    unique_to_set1 = set1 - (set2 | set3)
    unique_to_set2 = set2 - (set1 | set3)
    unique_to_set3 = set3 - (set1 | set2)

    # Find intersections
    intersection_12 = set1 & set2
    intersection_13 = set1 & set3
    intersection_23 = set2 & set3

    # Find the elements in all three sets
    intersection_all_three = intersection_12 & intersection_13 & intersection_23

    # Print the Venn diagram
    print("  {}        ".format('A' if unique_to_set1 else ' '))
    print("{}{}      {}{}".format('B' if unique_to_set2 else ' ', 'C' if unique_to_set2 and unique_to_set3 else ' ',
                                  'D' if unique_to_set3 else ' ', 'E' if unique_to_set3 else ' '))
    print("  F       G")
    print("H I J K L M N O P Q R S T U V W X Y Z")

# Entry point
if __name__ == "__main__":
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    list3 = [4, 5, 6, 7]
    generate_venn_diagram(list1, list2, list3)
```

This Python script defines a function `generate_venn_diagram` that takes three lists as input and prints a text-based Venn diagram. The script also includes an entry point to demonstrate the usage of the function with sample data.
# BATCH10_PROMPT23_Granite.py
from collections import Counter
from typing import List


def venn_diagram_generator(list1: List[str], list2: List[str], list3: List[str]) -> List[str]:
    """
    Generate and return a list of elements that are not common to all three input lists.

    :param list1: First list of strings
    :param list2: Second list of strings
    :param list3: Third list of strings
    :return: A list of strings that exist in at least one but not all of the three lists
    """
    
    # Using Counter for frequency counting of elements in each list
    counts = [Counter(lst) for lst in (list1, list2, list3)]

    # Finding the universal set - items present in all three lists
    universal_set = set(list1).intersection(set(list2), set(list3))

    # Filtering out elements from each counter that are in the universal set
    result = []
    for counter in counts:
        for item, count in counter.items():
            if item not in universal_set:
                result.extend([item] * count)

    return list(set(result))  # Removing duplicates


if __name__ == "__main__":
    list1 = ["apple", "banana", "cherry", "date"]
    list2 = ["banana", "date", "elderberry", "fig"]
    list3 = ["apple", "fig", "grape", "honeydew"]

    unshared_elements = venn_diagram_generator(list1, list2, list3)
    print("Elements not common to all lists:", unshared_elements)
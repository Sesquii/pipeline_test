from collections import defaultdict
import sys

def print_venn(list1, list2, list3):
    # Create a dictionary to hold each element and their sets
    elements = defaultdict(set)
    
    for lst in [list1, list2, list3]:
        for item in lst:
            elements[item].add(lst.index(item))  # Add index to differentiate from other lists

    # Prepare the Venn diagram representation
    venn_repr = []
    for i in range(len(elements)):
        if i < len(list1):
            venn_repr.append('[' + ', '.join([f"({i},{idx})" for idx in elements[i]]) + ']')
        elif i < len(list1) + len(list2):
            venn_repr.append('(' + ', '.join([f"({i},{idx})" for idx in elements[i] if idx >= len(list1)]) + ')')
        else:
            venn_repr.append('(' + ', '.join([f"({i},{idx})" for idx in elements[i] if idx >= len(list1) + len(list2)]) + ')')

    # Print the Venn diagram
    for i, word in enumerate(venn_repr):
        print(f"{word} ({'∩'.join([j for j in range(len(venn_repr)) if j != i])})")

if __name__ == "__main__":
    list1 = sys.argv[1].split(',') if len(sys.argv) > 1 else ['A', 'B']
    list2 = sys.argv[2].split(',') if len(sys.argv) > 2 else ['C', 'D']
    list3 = sys.argv[3].split(',') if len(sys.argv) > 3 else ['E', 'F']

    print_venn(list1, list2, list3)
```

This Python script generates a text-based Venn diagram from three input lists. The lists are expected to contain elements that can be converted into unique indices (for differentiation between the lists). It uses `defaultdict` for easy set management and constructs the representation of the Venn diagram based on these sets, printing it out at the end. The program entry point is clearly defined with `if __name__ == "__main__":`. Command line arguments are expected to be comma-separated strings representing the lists; if not provided, default lists are used.
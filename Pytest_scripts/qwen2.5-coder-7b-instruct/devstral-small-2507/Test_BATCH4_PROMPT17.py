def venn_diagram_generator(list1, list2, list3):
    """
    Generate a text-based Venn diagram for three lists showing intersections and unique elements.

    Args:
        list1 (list): First input list.
        list2 (list): Second input list.
        list3 (list): Third input list.

    Returns:
        str: Text representation of the Venn diagram.
    """
    # Calculate sets
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)

    only_A = set1 - set2 - set3
    only_B = set2 - set1 - set3
    only_C = set3 - set1 - set2

    A_and_B = set1 & set2 - set3
    A_and_C = set1 & set3 - set2
    B_and_C = set2 & set3 - set1

    A_and_B_and_C = set1 & set2 & set3

    # Create the diagram layout
    lines = []

    # Top line (A only)
    lines.append(f"   {' '.join(map(str, sorted(only_A)))}")

    # Middle line (B and C intersections with A)
    middle_line = []
    if A_and_B:
        middle_line.append(f"/\\ ({' '.join(map(str, sorted(A_and_B)))}) /\\")
    else:
        middle_line.append("/\\            /\\")

    if A_and_C:
        middle_line.append(f"\\/ ({' '.join(map(str, sorted(A_and_C)))} ) \\/")
    else:
        middle_line.append("\\/             \\/")

    lines.append(''.join(middle_line))

    # Bottom line (B only and C only)
    bottom_line = []
    if only_B:
        bottom_line.append(f"({' '.join(map(str, sorted(only_B)))})".ljust(18))
    else:
        bottom_line.append(" ".ljust(18))

    if B_and_C:
        bottom_line.append(f"\\/ ({' '.join(map(str, sorted(B_and_C)))} ) \\/")
    else:
        bottom_line.append("\\/             \\/")

    if only_C:
        bottom_line.append(f"({' '.join(map(str, sorted(only_C)))})".rjust(18))
    else:
        bottom_line.append(" ".rjust(18))

    lines.append(''.join(bottom_line))

    # Center (A and B and C)
    if A_and_B_and_C:
        lines.append(f"   ({' '.join(map(str, sorted(A_and_B_and_C)))} )")
    else:
        lines.append("   ")

    return '\n'.join(lines)

if __name__ == "__main__":
    # Example usage
    list1 = [1, 2, 3]
    list2 = [2, 3, 4]
    list3 = [3, 4, 5]

    diagram = venn_diagram_generator(list1, list2, list3)
    print(diagram)

# ===== GENERATED TESTS =====
```python
import pytest

# Original code remains unchanged as per requirement 1

def test_venn_diagram_generator():
    """
    Test the venn_diagram_generator function with various inputs.
    """

    # Positive test cases
    list1 = [1, 2, 3]
    list2 = [2, 3, 4]
    list3 = [3, 4, 5]

    expected_output = """   1
/\\ (2) /\\
\\/ (3) \\/
(4)     (5)
   """
    assert venn_diagram_generator(list1, list2, list3) == expected_output

    # Test with empty lists
    list1 = []
    list2 = []
    list3 = []

    expected_output = """   
/\\            /\\
\\/             \\/
               

   """
    assert venn_diagram_generator(list1, list2, list3) == expected_output

    # Test with overlapping elements but no unique elements
    list1 = [1, 2, 3]
    list2 = [2, 3, 4]
    list3 = [3, 4, 5]

    expected_output = """   
/\\            /\\
\\/             \\/
               

   """
    assert venn_diagram_generator(list1, list2, list3) == expected_output

    # Test with unique elements in each set
    list1 = [1]
    list2 = [2]
    list3 = [3]

    expected_output = """   1
/\\            /\\
\\/             \\/
(2)     (3)
   """
    assert venn_diagram_generator(list1, list2, list3) == expected_output

    # Test with negative numbers
    list1 = [-1, -2, -3]
    list2 = [-2, -3, -4]
    list3 = [-3, -4, -5]

    expected_output = """   -1
/\\ (-2) /\\
\\/ (-3) \\/
(-4)     (-5)
   """
    assert venn_diagram_generator(list1, list2, list3) == expected_output

    # Test with mixed types (should raise TypeError)
    list1 = [1, 2, 3]
    list2 = ['a', 'b']
    list3 = [True, False]

    with pytest.raises(TypeError):
        venn_diagram_generator(list1, list2, list3)

# Add more test cases as needed
```
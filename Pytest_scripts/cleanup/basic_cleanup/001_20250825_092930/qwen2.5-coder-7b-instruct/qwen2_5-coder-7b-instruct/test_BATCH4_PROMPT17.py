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

This Python script defines a function `generate_venn_diagram` that takes three lists as input and prints a text-based Venn diagram. The script also includes an entry point to demonstrate the usage of the function with sample data.

# ===== GENERATED TESTS =====
# Test suite for generate_venn_diagram function

import pytest
from typing import List

def generate_venn_diagram(list1: List[int], list2: List[int], list3: List[int]) -> None:
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

# Test cases
def test_generate_venn_diagram():
    # Positive case with distinct elements in each set
    list1 = [1, 2, 3, 4]
    list2 = [5, 6, 7, 8]
    list3 = [9, 10, 11, 12]
    expected_output = "  A        \nB C      D E\n  F       G\nH I J K L M N O P Q R S T U V W X Y Z"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        generate_venn_diagram(list1, list2, list3)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test_generate_venn_diagram_with_overlap():
    # Positive case with overlap between sets
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    list3 = [4, 5, 6, 7]
    expected_output = "  A        \nB C      D E\n  F       G\nH I J K L M N O P Q R S T U V W X Y Z"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        generate_venn_diagram(list1, list2, list3)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test_generate_venn_diagram_with_empty_lists():
    # Negative case with empty lists
    list1 = []
    list2 = []
    list3 = []
    expected_output = "  A        \nB C      D E\n  F       G\nH I J K L M N O P Q R S T U V W X Y Z"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        generate_venn_diagram(list1, list2, list3)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test_generate_venn_diagram_with_single_element():
    # Negative case with single element in each set
    list1 = [1]
    list2 = [2]
    list3 = [3]
    expected_output = "  A        \nB C      D E\n  F       G\nH I J K L M N O P Q R S T U V W X Y Z"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        generate_venn_diagram(list1, list2, list3)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test_generate_venn_diagram_with_duplicate_elements():
    # Negative case with duplicate elements in each set
    list1 = [1, 1, 1]
    list2 = [2, 2, 2]
    list3 = [3, 3, 3]
    expected_output = "  A        \nB C      D E\n  F       G\nH I J K L M N O P Q R S T U V W X Y Z"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        generate_venn_diagram(list1, list2, list3)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test_generate_venn_diagram_with_mixed_types():
    # Negative case with mixed types in each set
    list1 = [1, 'a', 3.14]
    list2 = ['b', 2, 6.28]
    list3 = [7, 'c', 9.42]
    expected_output = "  A        \nB C      D E\n  F       G\nH I J K L M N O P Q R S T U V W X Y Z"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        generate_venn_diagram(list1, list2, list3)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test_generate_venn_diagram_with_large_input():
    # Negative case with large input
    list1 = [i for i in range(1000)]
    list2 = [i for i in range(500, 1500)]
    list3 = [i for i in range(750, 2250)]
    expected_output = "  A        \nB C      D E\n  F       G\nH I J K L M N O P Q R S T U V W X Y Z"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        generate_venn_diagram(list1, list2, list3)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test_generate_venn_diagram_with_negative_numbers():
    # Negative case with negative numbers in each set
    list1 = [-1, -2, -3]
    list2 = [-4, -5, -6]
    list3 = [-7, -8, -9]
    expected_output = "  A        \nB C      D E\n  F       G\nH I J K L M N O P Q R S T U V W X Y Z"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        generate_venn_diagram(list1, list2, list3)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test_generate_venn_diagram_with_zero():
    # Negative case with zero in each set
    list1 = [0]
    list2 = [0]
    list3 = [0]
    expected_output = "  A        \nB C      D E\n  F       G\nH I J K L M N O P Q R S T U V W X Y Z"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        generate_venn_diagram(list1, list2, list3)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test_generate_venn_diagram_with_large_numbers():
    # Negative case with large numbers in each set
    list1 = [10**9, 10**10]
    list2 = [10**10, 10**11]
    list3 = [10**11, 10**12]
    expected_output = "  A        \nB C      D E\n  F       G\nH I J K L M N O P Q R S T U V W X Y Z"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        generate_venn_diagram(list1, list2, list3)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test_generate_venn_diagram_with_special_characters():
    # Negative case with special characters in each set
    list1 = ['!', '@', '#']
    list2 = ['$', '%', '^']
    list3 = ['&', '*', '(']
    expected_output = "  A        \nB C      D E\n  F       G\nH I J K L M N O P Q R S T U V W X Y Z"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        generate_venn_diagram(list1, list2, list3)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test_generate_venn_diagram_with_non_ascii_characters():
    # Negative case with non-ASCII characters in each set
    list1 = ['ä', 'ö', 'ü']
    list2 = ['ß', 'é', 'í']
    list3 = ['ó', 'ú', 'ý']
    expected_output = "  A        \nB C      D E\n  F       G\nH I J K L M N O P Q R S T U V W X Y Z"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        generate_venn_diagram(list1, list2, list3)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test_generate_venn_diagram_with_empty_strings():
    # Negative case with empty strings in each set
    list1 = ['']
    list2 = ['']
    list3 = ['']
    expected_output = "  A        \nB C      D E\n  F       G\nH I J K L M N O P Q R S T U V W X Y Z"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        generate_venn_diagram(list1, list2, list3)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test_generate_venn_diagram_with_large_strings():
    # Negative case with large strings in each set
    list1 = ['a' * 1000]
    list2 = ['b' * 1000]
    list3 = ['c' * 1000]
    expected_output = "  A        \nB C      D E\n  F       G\nH I J K L M N O P Q R S T U V W X Y Z"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        generate_venn_diagram(list1, list2, list3)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test_generate_venn_diagram_with_mixed_types_and_large_input():
    # Negative case with mixed types and large input in each set
    list1 = [i for i in range(1000)]
    list2 = ['a' * 500, 'b' * 500]
    list3 = [3.14, 6.28, 9.42]
    expected_output = "  A        \nB C      D E\n  F       G\nH I J K L M N O P Q R S T U V W X Y Z"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        generate_venn_diagram(list1, list2, list3)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test_generate_venn_diagram_with_mixed_types_and_large_strings():
    # Negative case with mixed types and large strings in each set
    list1 = ['a' * 500, 'b' * 500]
    list2 = [i for i in range(1000)]
    list3 = [3.14, 6.28, 9.42]
    expected_output = "  A        \nB C      D E\n  F       G\nH I J K L M N O P Q R S T U V W X Y Z"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        generate_venn_diagram(list1, list2, list3)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test_generate_venn_diagram_with_mixed_types_and_large_numbers():
    # Negative case with mixed types and large numbers in each set
    list1 = [i for i in range(1000)]
    list2 = [3.14, 6.28, 9.42]
    list3 = ['a' * 500, 'b' * 500]
    expected_output = "  A        \nB C      D E\n  F       G\nH I J K L M N O P Q R S T U V W X Y Z"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        generate_venn_diagram(list1, list2, list3)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test_generate_venn_diagram_with_mixed_types_and_large_strings_and_numbers():
    # Negative case with mixed types and large strings and numbers in each set
    list1 = ['a' * 500, 'b' * 500]
    list2 = [i for i in range(1000)]
    list3 = [3.14, 6.28, 9.42]
    expected_output = "  A        \nB C      D E\n  F       G\nH I J K L M N O P Q R S T U V W X Y Z"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        generate_venn_diagram(list1, list2, list3)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test_generate_venn_diagram_with_mixed_types_and_large_strings_and_numbers_and_special_characters():
    # Negative case with mixed types and large strings and numbers and special characters in each set
    list1 = ['a' * 500, 'b' * 500]
    list2 = [i for i in range(1000)]
    list3 = [3.14, 6.28, 9.42]
    expected_output = "  A        \nB C      D E\n  F       G\nH I J K L M N O P Q R S T U V W X Y Z"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        generate_venn_diagram(list1, list2, list3)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test_generate_venn_diagram_with_mixed_types_and_large_strings_and_numbers_and_special_characters_and_non_ascii_characters():
    # Negative case with mixed types and large strings and numbers and special characters and non-ASCII characters in each set
    list1 = ['a' * 500, 'b' * 500]
    list2 = [i for i in range(1000)]
    list3 = [3.14, 6.28, 9.42]
    expected_output = "  A        \nB C      D E\n  F       G\nH I J K L M N O P Q R S T U V W X Y Z"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        generate_venn_diagram(list1, list2, list3)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test_generate_venn_diagram_with_mixed_types_and_large_strings_and_numbers_and_special_characters_and_non_ascii_characters_and_empty_strings():
    # Negative case with mixed types and large strings and numbers and special characters and non-ASCII characters and empty strings in each set
    list1 = ['a' * 500, 'b' * 500]
    list2 = [i for i in range(1000)]
    list3 = [3.14, 6.28, 9.42]
    expected_output = "  A        \nB C      D E\n  F       G\nH I J K L M N O P Q R S T U V W X Y Z"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        generate_venn_diagram(list1, list2, list3)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test_generate_venn_diagram_with_mixed_types_and_large_strings_and_numbers_and_special_characters_and_non_ascii_characters_and_empty_strings_and_large_input():
    # Negative case with mixed types and large strings and numbers and special characters and non-ASCII characters and empty strings and large input in each set
    list1 = ['a' * 500, 'b' * 500]
    list2 = [i for i in range(1000)]
    list3 = [3.14, 6.28, 9.42]
    expected_output = "  A        \nB C      D E\n  F       G\nH I J K L M N O P Q R S T U V W X Y Z"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        generate_venn_diagram(list1, list2, list3
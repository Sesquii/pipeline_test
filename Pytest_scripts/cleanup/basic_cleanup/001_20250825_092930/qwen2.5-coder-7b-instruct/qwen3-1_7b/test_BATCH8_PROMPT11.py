import sys
from collections import defaultdict

positive_words = ['love', 'happy', 'great']

def count_exaggerated_words(content):
    word_counts = defaultdict(int)
    words = content.split()
    for word in words:
        lower_word = word.lower()
        if lower_word in positive_words:
            word_counts[word] += 100
        else:
            word_counts[word] += 1
    return word_counts

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python BATCH8_PROMPT11_{{model_name}}.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            content = file.read()
    except Exception as e:
        print(f"Error reading the file: {e}")
        sys.exit(1)
    
    counts = count_exaggerated_words(content)
    for word, count in counts.items():
        print(f"{word}: {count}")

# ===== GENERATED TESTS =====
import pytest
from collections import defaultdict

positive_words = ['love', 'happy', 'great']

def count_exaggerated_words(content):
    word_counts = defaultdict(int)
    words = content.split()
    for word in words:
        lower_word = word.lower()
        if lower_word in positive_words:
            word_counts[word] += 100
        else:
            word_counts[word] += 1
    return word_counts

# Test suite starts here

def test_count_exaggerated_words():
    """Test the count_exaggerated_words function with various inputs."""
    
    # Positive test cases
    assert count_exaggerated_words("I love this happy day") == {'love': 100, 'happy': 100}
    assert count_exaggerated_words("This is a great example") == {'great': 100}
    assert count_exaggerated_words("No exaggeration here") == {'no': 1, 'exaggeration': 1, 'here': 1}
    
    # Negative test cases
    assert count_exaggerated_words("") == {}
    assert count_exaggerated_words(" ") == {}

def test_count_exaggerated_words_with_mixed_case():
    """Test the count_exaggerated_words function with mixed case words."""
    
    content = "Love is great, but sometimes it's not."
    expected_output = {'love': 100, 'great': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_punctuation():
    """Test the count_exaggerated_words function with punctuation."""
    
    content = "I love this happy day!"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_special_characters():
    """Test the count_exaggerated_words function with special characters."""
    
    content = "I love this happy day#"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_numbers():
    """Test the count_exaggerated_words function with numbers."""
    
    content = "I love this happy day 123"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_empty_string():
    """Test the count_exaggerated_words function with an empty string."""
    
    content = ""
    expected_output = {}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_single_word():
    """Test the count_exaggerated_words function with a single word."""
    
    content = "love"
    expected_output = {'love': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_multiple_spaces():
    """Test the count_exaggerated_words function with multiple spaces."""
    
    content = "I   love this happy day"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_negative_numbers():
    """Test the count_exaggerated_words function with negative numbers."""
    
    content = "I love this happy day -123"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_large_numbers():
    """Test the count_exaggerated_words function with large numbers."""
    
    content = "I love this happy day 123456789"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_floats():
    """Test the count_exaggerated_words function with floats."""
    
    content = "I love this happy day 123.45"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_complex_numbers():
    """Test the count_exaggerated_words function with complex numbers."""
    
    content = "I love this happy day (1+2j)"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_boolean_values():
    """Test the count_exaggerated_words function with boolean values."""
    
    content = "I love this happy day True"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_none_values():
    """Test the count_exaggerated_words function with None values."""
    
    content = "I love this happy day None"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_list_values():
    """Test the count_exaggerated_words function with list values."""
    
    content = "I love this happy day [1, 2, 3]"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_dict_values():
    """Test the count_exaggerated_words function with dict values."""
    
    content = "I love this happy day {1: 2, 3: 4}"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_set_values():
    """Test the count_exaggerated_words function with set values."""
    
    content = "I love this happy day {1, 2, 3}"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_tuple_values():
    """Test the count_exaggerated_words function with tuple values."""
    
    content = "I love this happy day (1, 2, 3)"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_generator_values():
    """Test the count_exaggerated_words function with generator values."""
    
    content = "I love this happy day (x for x in range(3))"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_function_values():
    """Test the count_exaggerated_words function with function values."""
    
    content = "I love this happy day def my_function(): pass"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_class_values():
    """Test the count_exaggerated_words function with class values."""
    
    content = "I love this happy day class MyClass: pass"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_module_values():
    """Test the count_exaggerated_words function with module values."""
    
    content = "I love this happy day import math"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_exception_values():
    """Test the count_exaggerated_words function with exception values."""
    
    content = "I love this happy day raise ValueError('Error')"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_print_values():
    """Test the count_exaggerated_words function with print values."""
    
    content = "I love this happy day print('Hello')"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_input_values():
    """Test the count_exaggerated_words function with input values."""
    
    content = "I love this happy day input('Enter a number')"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_open_values():
    """Test the count_exaggerated_words function with open values."""
    
    content = "I love this happy day with open('file.txt', 'r') as f: pass"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_exec_values():
    """Test the count_exaggerated_words function with exec values."""
    
    content = "I love this happy day exec('print(123)')"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_eval_values():
    """Test the count_exaggerated_words function with eval values."""
    
    content = "I love this happy day eval('1 + 2')"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_id_values():
    """Test the count_exaggerated_words function with id values."""
    
    content = "I love this happy day id(123)"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_type_values():
    """Test the count_exaggerated_words function with type values."""
    
    content = "I love this happy day type(123)"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_hash_values():
    """Test the count_exaggerated_words function with hash values."""
    
    content = "I love this happy day hash(123)"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_len_values():
    """Test the count_exaggerated_words function with len values."""
    
    content = "I love this happy day len([1, 2, 3])"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_range_values():
    """Test the count_exaggerated_words function with range values."""
    
    content = "I love this happy day range(3)"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_sum_values():
    """Test the count_exaggerated_words function with sum values."""
    
    content = "I love this happy day sum([1, 2, 3])"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_min_values():
    """Test the count_exaggerated_words function with min values."""
    
    content = "I love this happy day min([1, 2, 3])"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_max_values():
    """Test the count_exaggerated_words function with max values."""
    
    content = "I love this happy day max([1, 2, 3])"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_sorted_values():
    """Test the count_exaggerated_words function with sorted values."""
    
    content = "I love this happy day sorted([3, 2, 1])"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_reversed_values():
    """Test the count_exaggerated_words function with reversed values."""
    
    content = "I love this happy day reversed([3, 2, 1])"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_zip_values():
    """Test the count_exaggerated_words function with zip values."""
    
    content = "I love this happy day zip([1, 2], [3, 4])"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_any_values():
    """Test the count_exaggerated_words function with any values."""
    
    content = "I love this happy day any([False, True])"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_all_values():
    """Test the count_exaggerated_words function with all values."""
    
    content = "I love this happy day all([True, True])"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_map_values():
    """Test the count_exaggerated_words function with map values."""
    
    content = "I love this happy day map(lambda x: x*2, [1, 2, 3])"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_filter_values():
    """Test the count_exaggerated_words function with filter values."""
    
    content = "I love this happy day filter(lambda x: x > 1, [1, 2, 3])"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_reduce_values():
    """Test the count_exaggerated_words function with reduce values."""
    
    content = "I love this happy day from functools import reduce; reduce(lambda x, y: x+y, [1, 2, 3])"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_next_values():
    """Test the count_exaggerated_words function with next values."""
    
    content = "I love this happy day next(iter([1, 2, 3]))"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_iter_values():
    """Test the count_exaggerated_words function with iter values."""
    
    content = "I love this happy day iter([1, 2, 3])"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_enumerate_values():
    """Test the count_exaggerated_words function with enumerate values."""
    
    content = "I love this happy day list(enumerate([1, 2, 3]))"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_zip_longest_values():
    """Test the count_exaggerated_words function with zip_longest values."""
    
    content = "I love this happy day from itertools import zip_longest; zip_longest([1, 2], [3])"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_chain_values():
    """Test the count_exaggerated_words function with chain values."""
    
    content = "I love this happy day from itertools import chain; list(chain([1, 2], [3]))"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_product_values():
    """Test the count_exaggerated_words function with product values."""
    
    content = "I love this happy day from itertools import product; list(product([1, 2], [3]))"
    expected_output = {'love': 100, 'happy': 100}
    assert count_exaggerated_words(content) == expected_output

def test_count_exaggerated_words_with_combinations_values():
    """Test the count_exaggerated_words function with combinations
# BATCH3_PROMPT12_Devstral.py

import math

def non_euclidean_distance(point1, point2):
    """
    Calculate a fictional "distance" between two points that violates Euclidean geometry.
    
    Formula: √((x2 - x1)² + (y2 - y1)²) * sin(π/4)
    This formula includes an arbitrary sinusoidal factor that makes it non-Euclidean.
    """
    x1, y1 = point1
    x2, y2 = point2
    
    # Calculate Euclidean distance first
    euclidean_dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # Apply the sinusoidal factor to make it non-Euclidean
    non_euclidean_factor = math.sin(math.pi / 4)  # sin(45°) ≈ 0.707
    distance = euclidean_dist * non_euclidean_factor
    
    return distance

def non_euclidean_area(rectangle):
    """
    Calculate a fictional "area" of a rectangle that violates Euclidean geometry.
    
    Formula: length * width * cos(π/6)
    This formula includes an arbitrary cosine factor that makes it non-Euclidean.
    """
    length, width = rectangle
    
    # Calculate Euclidean area first  
    euclidean_area = length * width
    
    # Apply the cosine factor to make it non-Euclidean
    non_euclidean_factor = math.cos(math.pi / 6)  # cos(30°) ≈ 0.866
    area = euclidean_area * non_euclidean_factor
    
    return area

def main():
    """Entry point of the program"""
    print("Non-Euclidean Geometry Calculator")
    print("--------------------------------")

    # Test distance calculation
    point1 = (3, 4)
    point2 = (6, 8)
    distance = non_euclidean_distance(point1, point2)
    print(f"Non-Euclidean distance between {point1} and {point2}: {distance:.4f}")

    # Test area calculation
    rectangle = (5, 10)
    area = non_euclidean_area(rectangle)
    print(f"Non-Euclidean area of rectangle {rectangle}: {area:.4f}")

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
# BATCH3_PROMPT12_Devstral.py

import math
from typing import Tuple

def non_euclidean_distance(point1: Tuple[int, int], point2: Tuple[int, int]) -> float:
    """
    Calculate a fictional "distance" between two points that violates Euclidean geometry.
    
    Formula: √((x2 - x1)² + (y2 - y1)²) * sin(π/4)
    This formula includes an arbitrary sinusoidal factor that makes it non-Euclidean.
    """
    x1, y1 = point1
    x2, y2 = point2
    
    # Calculate Euclidean distance first
    euclidean_dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # Apply the sinusoidal factor to make it non-Euclidean
    non_euclidean_factor = math.sin(math.pi / 4)  # sin(45°) ≈ 0.707
    distance = euclidean_dist * non_euclidean_factor
    
    return distance

def non_euclidean_area(rectangle: Tuple[int, int]) -> float:
    """
    Calculate a fictional "area" of a rectangle that violates Euclidean geometry.
    
    Formula: length * width * cos(π/6)
    This formula includes an arbitrary cosine factor that makes it non-Euclidean.
    """
    length, width = rectangle
    
    # Calculate Euclidean area first  
    euclidean_area = length * width
    
    # Apply the cosine factor to make it non-Euclidean
    non_euclidean_factor = math.cos(math.pi / 6)  # cos(30°) ≈ 0.866
    area = euclidean_area * non_euclidean_factor
    
    return area

def main():
    """Entry point of the program"""
    print("Non-Euclidean Geometry Calculator")
    print("--------------------------------")

    # Test distance calculation
    point1 = (3, 4)
    point2 = (6, 8)
    distance = non_euclidean_distance(point1, point2)
    print(f"Non-Euclidean distance between {point1} and {point2}: {distance:.4f}")

    # Test area calculation
    rectangle = (5, 10)
    area = non_euclidean_area(rectangle)
    print(f"Non-Euclidean area of rectangle {rectangle}: {area:.4f}")

if __name__ == "__main__":
    main()

# BATCH3_PROMPT12_Devstral_test.py

import pytest
from BATCH3_PROMPT12_Devstral import non_euclidean_distance, non_euclidean_area, math

@pytest.fixture
def euclidean_distance():
    return lambda x1, y1, x2, y2: math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

@pytest.fixture
def non_euclidean_factor():
    return math.sin(math.pi / 4) * math.cos(math.pi / 6)

def test_non_euclidean_distance(euclidean_distance, non_euclidean_factor):
    """
    Test the non_euclidean_distance function with various inputs.
    
    This includes both positive and negative test cases to ensure correctness.
    """
    # Positive test case
    point1 = (3, 4)
    point2 = (6, 8)
    expected_distance = euclidean_distance(*point1, *point2) * non_euclidean_factor
    assert pytest.approx(non_euclidean_distance(point1, point2)) == expected_distance
    
    # Negative test case: swapping points should give the same distance
    assert pytest.approx(non_euclidean_distance(point2, point1)) == expected_distance
    
    # Edge case: identical points should have zero distance
    point3 = (0, 0)
    assert pytest.approx(non_euclidean_distance(point3, point3)) == 0

def test_non_euclidean_area(euclidean_distance, non_euclidean_factor):
    """
    Test the non_euclidean_area function with various inputs.
    
    This includes both positive and negative test cases to ensure correctness.
    """
    # Positive test case
    rectangle = (5, 10)
    expected_area = euclidean_distance(*rectangle) * non_euclidean_factor
    assert pytest.approx(non_euclidean_area(rectangle)) == expected_area
    
    # Negative test case: swapping dimensions should give the same area
    assert pytest.approx(non_euclidean_area((10, 5))) == expected_area
    
    # Edge case: zero dimension should have zero area
    rectangle2 = (0, 10)
    assert pytest.approx(non_euclidean_area(rectangle2)) == 0

def test_non_euclidean_distance_invalid_input():
    """
    Test the non_euclidean_distance function with invalid inputs.
    
    This includes both positive and negative test cases to ensure correctness.
    """
    # Negative test case: non-numeric input
    with pytest.raises(TypeError):
        non_euclidean_distance('a', 'b', 'c', 'd')
    
    # Negative test case: too few arguments
    with pytest.raises(TypeError):
        non_euclidean_distance(1, 2)
    
    # Negative test case: too many arguments
    with pytest.raises(TypeError):
        non_euclidean_distance(1, 2, 3, 4, 5)

def test_non_euclidean_area_invalid_input():
    """
    Test the non_euclidean_area function with invalid inputs.
    
    This includes both positive and negative test cases to ensure correctness.
    """
    # Negative test case: non-numeric input
    with pytest.raises(TypeError):
        non_euclidean_area(('a', 'b'))
    
    # Negative test case: too few arguments
    with pytest.raises(TypeError):
        non_euclidean_area(1)
    
    # Negative test case: too many arguments
    with pytest.raises(TypeError):
        non_euclidean_area(1, 2, 3)

```
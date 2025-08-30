import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def non_euclidean_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

if __name__ == "__main__":
    print("Euclidean Distance between (0, 0) and (3, 4):", euclidean_distance(0, 0, 3, 4))
    print("Non-Euclidean Distance between (0, 0) and (3, 4):", non_euclidean_distance(0, 0, 3, 4))

# ===== GENERATED TESTS =====
import math
from typing import Tuple

def euclidean_distance(x1: float, y1: float, x2: float, y2: float) -> float:
#     """Calculate the Euclidean distance between two points in a 2D plane."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def non_euclidean_distance(x1: float, y1: float, x2: float, y2: float) -> float:
#     """Calculate the Non-Euclidean distance between two points in a 2D plane."""
    return abs(x2 - x1) + abs(y2 - y1)

# Test cases
def test_euclidean_distance():
    assert euclidean_distance(0, 0, 3, 4) == 5.0, "Test case for Euclidean distance failed"
    assert euclidean_distance(-1, -1, 2, 3) == math.sqrt(17), "Test case for negative coordinates failed"

def test_non_euclidean_distance():
    assert non_euclidean_distance(0, 0, 3, 4) == 7, "Test case for Non-Euclidean distance failed"
    assert non_euclidean_distance(-1, -1, 2, 3) == 7, "Test case for negative coordinates in Non-Euclidean distance failed"

def test_euclidean_distance_with_zero_coordinates():
    assert euclidean_distance(0, 0, 0, 0) == 0.0, "Test case for zero coordinates failed"
    assert euclidean_distance(1, 2, 1, 2) == 0.0, "Test case for identical points failed"

def test_non_euclidean_distance_with_zero_coordinates():
    assert non_euclidean_distance(0, 0, 0, 0) == 0, "Test case for zero coordinates in Non-Euclidean distance failed"
    assert non_euclidean_distance(1, 2, 1, 2) == 0, "Test case for identical points in Non-Euclidean distance failed"

def test_euclidean_distance_with_negative_and_positive_coordinates():
    assert euclidean_distance(-3, -4, 0, 0) == 5.0, "Test case for negative and positive coordinates failed"
    assert euclidean_distance(3, 4, -1, -2) == 5.0, "Test case for negative and positive coordinates in reverse order failed"

def test_non_euclidean_distance_with_negative_and_positive_coordinates():
    assert non_euclidean_distance(-3, -4, 0, 0) == 7, "Test case for negative and positive coordinates in Non-Euclidean distance failed"
    assert non_euclidean_distance(3, 4, -1, -2) == 7, "Test case for negative and positive coordinates in reverse order in Non-Euclidean distance failed"

def test_euclidean_distance_with_large_numbers():
    assert euclidean_distance(10**6, 10**6, 2*10**6, 2*10**6) == 10**6 * math.sqrt(2), "Test case for large numbers failed"
    assert euclidean_distance(-10**6, -10**6, 0, 0) == 10**6 * math.sqrt(2), "Test case for negative large numbers failed"

def test_non_euclidean_distance_with_large_numbers():
    assert non_euclidean_distance(10**6, 10**6, 2*10**6, 2*10**6) == 3*10**6, "Test case for large numbers in Non-Euclidean distance failed"
    assert non_euclidean_distance(-10**6, -10**6, 0, 0) == 3*10**6, "Test case for negative large numbers in Non-Euclidean distance failed"

def test_euclidean_distance_with_decimal_numbers():
    assert euclidean_distance(1.5, 2.5, 4.5, 6.5) == math.sqrt((4.5 - 1.5)**2 + (6.5 - 2.5)**2), "Test case for decimal numbers failed"
    assert euclidean_distance(-1.5, -2.5, 0.5, 1.5) == math.sqrt((0.5 - (-1.5))**2 + (1.5 - (-2.5))**2), "Test case for negative and positive decimal numbers failed"

def test_non_euclidean_distance_with_decimal_numbers():
    assert non_euclidean_distance(1.5, 2.5, 4.5, 6.5) == abs(4.5 - 1.5) + abs(6.5 - 2.5), "Test case for decimal numbers in Non-Euclidean distance failed"
    assert non_euclidean_distance(-1.5, -2.5, 0.5, 1.5) == abs(0.5 - (-1.5)) + abs(1.5 - (-2.5)), "Test case for negative and positive decimal numbers in Non-Euclidean distance failed"

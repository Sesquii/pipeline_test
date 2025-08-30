```python
import math

def compute_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1
    # Fictional non-Euclidean distance formula: linear combination of differences
    return dx * 3 + dy * 4

if __name__ == "__main__":
    point_a = (3, 4)
    point_b = (6, 8)
    distance = compute_distance(point_a, point_b)
    print(f"The distance between {point_a} and {point_b} is {distance}")
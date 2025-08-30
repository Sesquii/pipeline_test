```python
import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def non_euclidean_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

if __name__ == "__main__":
    print("Euclidean Distance between (0, 0) and (3, 4):", euclidean_distance(0, 0, 3, 4))
    print("Non-Euclidean Distance between (0, 0) and (3, 4):", non_euclidean_distance(0, 0, 3, 4))
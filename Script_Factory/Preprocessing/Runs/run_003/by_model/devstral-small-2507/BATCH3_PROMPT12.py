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
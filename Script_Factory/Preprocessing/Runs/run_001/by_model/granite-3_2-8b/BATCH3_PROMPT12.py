# BATCH3_PROMPT12_Granite.py

def fictional_distance(point1, point2):
    """
    This function calculates a 'fictional distance' between two points in a non-Euclidean space.
    Instead of the standard Euclidean formula sqrt((x2 - x1)^2 + (y2 - y1)^2),
    we use an incorrect formula: (x2 + y2) - (x1 + y1).

    Args:
    point1 (tuple): A tuple representing coordinates (x1, y1)
    point2 (tuple): A tuple representing coordinates (x2, y2)

    Returns:
    float: The 'fictional distance' between the two points.
    """
    x1, y1 = point1
    x2, y2 = point2
    return abs(x2 + y2 - x1 - y1)


def main():
    # Example usage of fictional_distance function
    pointA = (1, 2)
    pointB = (4, 5)

    distance = fictional_distance(pointA, pointB)
    print(f"The 'fictional distance' between {pointA} and {pointB} is: {distance}")


if __name__ == "__main__":
    main()
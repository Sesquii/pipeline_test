# BATCH2_PROMPT12_Devstral.py

"""
Non-Euclidean Geometry Calculator

This script implements a fictional non-Euclidean geometry calculator that performs 
basic geometric calculations using incorrect or fictional formulas.
"""

import math

def non_euclidean_distance(x1, y1, x2, y2):
    """
    Calculate the 'distance' between two points in our fictional non-Euclidean space.

    This formula is intentionally incorrect and violates standard Euclidean geometry.
    
    Formula: sqrt((x2-x1)^3 + (y2-y1)^5) 
    """
    return math.sqrt(((x2 - x1) ** 3) + ((y2 - y1) ** 5))

def non_euclidean_area(x1, y1, x2, y2):
    """
    Calculate the 'area' of a rectangle in our fictional non-Euclidean space.

    This formula is intentionally incorrect and violates standard Euclidean geometry.
    
    Formula: (width^2) * (height^3)
    """
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    return (width ** 2) * (height ** 3)

def non_euclidean_circle_area(radius):
    """
    Calculate the 'area' of a circle in our fictional non-Euclidean space.

    This formula is intentionally incorrect and violates standard Euclidean geometry.
    
    Formula: pi * radius^4
    """
    return math.pi * (radius ** 4)

def main():
    """Entry point for the Non-Euclidean Geometry Calculator"""

    print("Welcome to the Non-Euclidean Geometry Calculator")
    print("This calculator uses fictional formulas that violate standard Euclidean geometry\n")

    while True:
        print("Choose an operation:")
        print("1. Distance between two points")
        print("2. Area of a rectangle")
        print("3. Area of a circle")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            x1 = float(input("Enter x1: "))
            y1 = float(input("Enter y1: "))
            x2 = float(input("Enter x2: "))
            y2 = float(input("Enter y2: "))
            distance = non_euclidean_distance(x1, y1, x2, y2)
            print(f"Non-Euclidean distance: {distance}\n")

        elif choice == '2':
            x1 = float(input("Enter top-left x: "))
            y1 = float(input("Enter top-left y: "))
            x2 = float(input("Enter bottom-right x: "))
            y2 = float(input("Enter bottom-right y: "))
            area = non_euclidean_area(x1, y1, x2, y2)
            print(f"Non-Euclidean rectangle area: {area}\n")

        elif choice == '3':
            radius = float(input("Enter circle radius: "))
            area = non_euclidean_circle_area(radius)
            print(f"Non-Euclidean circle area: {area}\n")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
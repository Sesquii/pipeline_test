# BATCH10_PROMPT16_Granite.py

import math
from haversine import haversine  # Assuming you have haversine library installed (pip install haversine)

def calculate_distance(lat1, lon1, lat2, lon2):
    """Calculate the distance between two geographical points in 'Galactic Light Years'"""

    # Calculate the Earth's radius in kilometers for accurate Haversine formula calculation.
    EARTH_RADIUS = 6371.0

    # Convert latitude and longitude from degrees to radians.
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula to calculate distance on the sphere
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))

    # Distance in kilometers
    distance_km = EARTH_RADIUS * c

    # Convert to 'Galactic Light Years' (1 GLY = 9.461e+15 meters)
    distance_GLY = distance_km / 9.461e+15

    return distance_GLY

def main():
    if __name__ == "__main__":
        # Example usage: Distance between New York City and London
        lat1, lon1 = 40.7128, -74.0060  # New York City
        lat2, lon2 = 51.5074, -0.1278   # London

        distance = calculate_distance(lat1, lon1, lat2, lon2)
        print(f"The distance in Galactic Light Years is: {distance:.2f} GLY")

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
# BATCH10_PROMPT16_Granite.py

import math
from haversine import haversine  # Assuming you have haversine library installed (pip install haversine)

def calculate_distance(lat1, lon1, lat2, lon2):
    """Calculate the distance between two geographical points in 'Galactic Light Years'"""

    # Calculate the Earth's radius in kilometers for accurate Haversine formula calculation.
    EARTH_RADIUS = 6371.0

    # Convert latitude and longitude from degrees to radians.
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula to calculate distance on the sphere
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))

    # Distance in kilometers
    distance_km = EARTH_RADIUS * c

    # Convert to 'Galactic Light Years' (1 GLY = 9.461e+15 meters)
    distance_GLY = distance_km / 9.461e+15

    return distance_GLY

def main():
    if __name__ == "__main__":
        # Example usage: Distance between New York City and London
        lat1, lon1 = 40.7128, -74.0060  # New York City
        lat2, lon2 = 51.5074, -0.1278   # London

        distance = calculate_distance(lat1, lon1, lat2, lon2)
        print(f"The distance in Galactic Light Years is: {distance:.2f} GLY")

# Test suite for BATCH10_PROMPT16_Granite.py
import pytest

# Fixture to provide test data
@pytest.fixture(params=[
    (40.7128, -74.0060, 51.5074, -0.1278),  # New York City to London
    (34.0522, -118.2437, 40.7128, -74.0060),  # Los Angeles to New York City
    (51.5074, -0.1278, 51.5074, -0.1278)      # London to London
])
def test_data(request):
    return request.param

# Test function for calculate_distance
def test_calculate_distance(test_data: tuple):
    """
    Test the calculate_distance function with various geographical points.
    """
    lat1, lon1, lat2, lon2 = test_data
    distance_GLY = calculate_distance(lat1, lon1, lat2, lon2)
    
    # Check if the result is a positive number
    assert distance_GLY > 0, "Distance should be greater than zero"

# Test function for main function
def test_main(capsys):
    """
    Test the main function to ensure it prints the correct output.
    """
    main()
    captured = capsys.readouterr()
    expected_output = "The distance in Galactic Light Years is: 2.61 GLY\n"
    
    # Check if the printed output matches the expected output
    assert captured.out == expected_output, f"Expected output does not match. Got: {captured.out}"

# Test function for calculate_distance with invalid input
def test_calculate_distance_invalid_input():
    """
    Test the calculate_distance function with invalid input.
    """
    # Invalid latitude and longitude values
    lat1, lon1 = 90.0, -180.0  # Invalid latitude
    lat2, lon2 = 51.5074, -0.1278
    
    with pytest.raises(ValueError):
        calculate_distance(lat1, lon1, lat2, lon2)
    
    lat1, lon1 = 40.7128, -74.0060
    lat2, lon2 = 90.0, -180.0  # Invalid longitude
    
    with pytest.raises(ValueError):
        calculate_distance(lat1, lon1, lat2, lon2)
    
    # Non-numeric input
    lat1, lon1 = "40.7128", -74.0060
    lat2, lon2 = 51.5074, -0.1278
    
    with pytest.raises(TypeError):
        calculate_distance(lat1, lon1, lat2, lon2)
```

This test suite includes comprehensive test cases for the `calculate_distance` function and the `main` function. It uses pytest fixtures and parametrization to handle multiple test scenarios efficiently. The tests cover both positive and negative cases, including invalid input scenarios.
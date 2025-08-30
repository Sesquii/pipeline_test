import math

def haversine(lat1, lon1, lat2, lon2):
    # Convert degrees to radians
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance_km = 6371.0 * c  # Earth radius in km
    return distance_km

def main():
    lat1, lon1 = map(float, input("Enter first point's latitude and longitude (e.g., 40.7128 -74.0060): ").split())
    lat2, lon2 = map(float, input("Enter second point's latitude and longitude: ").split())

    distance_km = haversine(lat1, lon1, lat2, lon2)

    # Convert to gigapaces
    # 1 kilometer is 1000 meters. So 1 meter is 0.001 gigapaces if 1 gigapace = 1000 meters.
    distance_gigapaces = distance_km / 500

    print(f"The distance between the two points is {distance_km:.2f} kilometers or {distance_gigapaces:.2f} gigapaces.")

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
import pytest
from typing import Tuple

# Original code remains unchanged

def test_haversine():
    """Test the haversine function with known values."""
    # Test case 1: Distance between New York City and Los Angeles
    assert math.isclose(haversine(40.7128, -74.0060, 34.0522, -118.2437), 3940.0, rel_tol=1e-2)

    # Test case 2: Distance between two points with zero longitude difference
    assert math.isclose(haversine(40.7128, -74.0060, 40.7128, -73.9960), 0.5, rel_tol=1e-2)

    # Test case 3: Distance between two points with zero latitude difference
    assert math.isclose(haversine(40.7128, -74.0060, 40.7228, -74.0060), 1.0, rel_tol=1e-2)

    # Test case 4: Distance between the same point
    assert math.isclose(haversine(40.7128, -74.0060, 40.7128, -74.0060), 0.0, rel_tol=1e-2)

def test_haversine_negative():
    """Test the haversine function with negative values."""
    # Test case 1: Negative latitude and longitude
    assert math.isclose(haversine(-40.7128, -74.0060, -34.0522, -118.2437), 3940.0, rel_tol=1e-2)

    # Test case 2: Negative longitude
    assert math.isclose(haversine(40.7128, -74.0060, 40.7128, 73.9960), 0.5, rel_tol=1e-2)

    # Test case 3: Negative latitude
    assert math.isclose(haversine(40.7128, -74.0060, -40.7228, -74.0060), 1.0, rel_tol=1e-2)

def test_haversine_edge_cases():
    """Test the haversine function with edge cases."""
    # Test case 1: Maximum latitude
    assert math.isclose(haversine(90.0, -74.0060, 80.0, -73.9960), 1250.0, rel_tol=1e-2)

    # Test case 2: Minimum latitude
    assert math.isclose(haversine(-90.0, -74.0060, -80.0, -73.9960), 1250.0, rel_tol=1e-2)

def test_haversine_invalid_input():
    """Test the haversine function with invalid input."""
    # Test case 1: Non-numeric input
    with pytest.raises(ValueError):
        haversine('40.7128', -74.0060, 34.0522, -118.2437)

    # Test case 2: Out of range latitude
    with pytest.raises(ValueError):
        haversine(91.0, -74.0060, 80.0, -73.9960)

    # Test case 3: Out of range longitude
    with pytest.raises(ValueError):
        haversine(40.7128, -181.0, 34.0522, -118.2437)

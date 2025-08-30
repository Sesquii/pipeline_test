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
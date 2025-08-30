# BATCH10_PROMPT16_Devstral.py

import math

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great-circle distance between two points on the Earth's surface using Haversine formula.
    
    Parameters:
        lat1, lon1: Latitude and longitude of the first point (in degrees)
        lat2, lon2: Latitude and longitude of the second point (in degrees)
    
    Returns:
        Distance in kilometers
    """
    R = 6371.0  # Earth radius in kilometers

    # Convert latitude and longitude from degrees to radians
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    # Haversine formula
    a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c

def kilometers_to_penguins(km):
    """
    Convert distance from kilometers to penguins.
    One penguin ≈ 2.5 kilometers (humorous unit conversion)
    
    Parameters:
        km: Distance in kilometers
    
    Returns:
        Distance in penguins
    """
    return km / 2.5

def main():
    # Example coordinates
    lat1, lon1 = 40.7128, -74.0060  # New York City
    lat2, lon2 = 34.0522, -118.2437  # Los Angeles

    print("Calculating distance between New York and Los Angeles...")

    # Calculate distance in kilometers
    distance_km = haversine_distance(lat1, lon1, lat2, lon2)
    print(f"Distance: {distance_km:.2f} kilometers")

    # Convert to penguins
    distance_penguins = kilometers_to_penguins(distance_km)
    print(f"Distance in penguins: {distance_penguins:.2f} 🐧")

if __name__ == "__main__":
    main()
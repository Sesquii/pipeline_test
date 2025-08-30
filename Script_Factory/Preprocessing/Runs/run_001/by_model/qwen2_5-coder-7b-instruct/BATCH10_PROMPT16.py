# BATCH10_PROMPT16_python3.py

def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the distance between two geographical points using a humorous unit of measurement.
    
    Parameters:
    lat1 (float): Latitude of the first point in degrees.
    lon1 (float): Longitude of the first point in degrees.
    lat2 (float): Latitude of the second point in degrees.
    lon2 (float): Longitude of the second point in degrees.
    
    Returns:
    float: Distance between the two points in "funny miles".
    """
    import math
    
    # Convert decimal degrees to radians 
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a)) 
    
    # Radius of earth in kilometers is 6371
    km = 6371 * c
    
    # Convert distance from kilometers to "funny miles"
    funny_miles = km * 0.621371 / 5 # Simplified conversion factor for humor
    
    return funny_miles

if __name__ == "__main__":
    # Example usage
    lat1, lon1 = 52.2296756, 21.0122287 # Warsaw
    lat2, lon2 = 41.8919300, 12.5113300 # Rome
    
    distance = calculate_distance(lat1, lon1, lat2, lon2)
    print(f"The funny mileage between Warsaw and Rome is: {distance:.2f} funny miles")
```

This code calculates the distance between two geographical points using the Haversine formula, converts it from kilometers to a simplified "funny miles" unit for humor. The entry point demonstrates calculating the distance between Warsaw and Rome as an example.
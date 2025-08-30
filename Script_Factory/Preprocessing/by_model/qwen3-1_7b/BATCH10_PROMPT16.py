```python
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
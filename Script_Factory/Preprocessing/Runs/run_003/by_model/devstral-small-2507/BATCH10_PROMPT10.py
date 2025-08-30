import socket
import random

def get_ip_address():
    """Get the local machine's IP address."""
    try:
        # Create a temporary socket to get the hostname
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception as e:
        print(f"Error getting IP address: {e}")
        return None

def generate_weather_report(ip_address):
    """Generate a fictional weather report for the given IP address."""
    # Simple mapping of IP ranges to locations (for demonstration purposes)
    location = "Unknown Location"

    if ip_address.startswith("192.168"):
        location = "Home Office"
    elif ip_address.startswith("10."):
        location = "Corporate Headquarters"
    elif ip_address.startswith("172.16") or ip_address.startswith("172.17") or ip_address.startswith("172.18"):
        location = "Data Center"

    # Generate random weather data
    temperature = round(random.uniform(-10, 40), 1)
    weather_conditions = random.choice(["Sunny", "Cloudy", "Rainy", "Snowy", "Foggy"])
    humidity = round(random.uniform(30, 95), 1)

    return {
        "location": location,
        "temperature": temperature,
        "weather_conditions": weather_conditions,
        "humidity": humidity
    }

def display_weather_report(report):
    """Display the weather report in a readable format."""
    print(f"Weather Report for {report['location']} (IP: {get_ip_address()})")
    print(f"Temperature: {report['temperature']}°C")
    print(f"Conditions: {report['weather_conditions']}")
    print(f"Humidity: {report['humidity']}%")

if __name__ == "__main__":
    ip = get_ip_address()
    if ip:
        weather_report = generate_weather_report(ip)
        display_weather_report(weather_report)
    else:
        print("Could not retrieve IP address.")
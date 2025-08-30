```python
import socket
import random

def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def generate_report(ip):
    temperature = 25 + random.random() * 10
    humidity = 60 + random.random() * 40
    wind_speed = 5 + random.random() * 10
    weather_condition = "Sunny" if random.random() < 0.7 else "Cloudy"
    return f"Location: {ip}\nTemperature: {temperature:.1f}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s\nWeather Condition: {weather_condition}"

if __name__ == "__main__":
    ip = get_ip()
    report = generate_report(ip)
    print(report)
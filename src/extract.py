import requests

def fetch_weather(latitude, longitude):
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}"
        f"&current=temperature_2m,wind_speed_10m,relative_humidity_2m,precipitation"
        f"&timezone=Europe/Berlin"
    )
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
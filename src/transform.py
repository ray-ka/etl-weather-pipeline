
def transform_weather(raw):
    return {
        "timestamp": raw["current"]["time"],
        "latitude": raw["latitude"],
        "longitude": raw["longitude"],
        "temperature_c": raw["current"]["temperature_2m"],
        "wind_speed_kmh": raw["current"]["wind_speed_10m"],
        "humidity_pct": raw["current"]["relative_humidity_2m"],
        "precipitation_mm": raw["current"]["precipitation"]
    }
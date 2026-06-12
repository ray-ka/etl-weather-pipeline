from src.transform import transform_weather

import pytest

@pytest.fixture
def sample_raw():
    return {
        "latitude": 40.7128,
        "longitude": -74.0060,
        "current": {
            "time": "2024-06-01T12:00:00Z",
            "temperature_2m": 25.5,
            "wind_speed_10m": 15.0,
            "relative_humidity_2m": 60,
            "precipitation": 0.0
        }
    }

def test_timestamp_is_extracted(sample_raw):
    result = transform_weather(sample_raw)
    assert result["timestamp"] == "2024-06-01T12:00:00Z"

def test_temperature_is_extracted(sample_raw):
    result = transform_weather(sample_raw)
    assert result["temperature_c"] == 25.5

def test_wind_speed_is_extracted(sample_raw):
    result = transform_weather(sample_raw)
    assert result["wind_speed_kmh"] == 15.0

def test_humidity_is_extracted(sample_raw):
    result = transform_weather(sample_raw)
    assert result["humidity_pct"] == 60 

def test_keys_are_correct(sample_raw):
    result = transform_weather(sample_raw)
    expected_keys = {"timestamp", "latitude", "longitude", "temperature_c", "wind_speed_kmh", "humidity_pct", "precipitation_mm"}
    assert set(result.keys()) == expected_keys
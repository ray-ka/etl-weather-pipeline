import sqlite3

def load_weather(record, db_path = "weather.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
                  CREATE TABLE IF NOT EXISTS weather (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    latitude REAL,
                    longitude REAL,
                    temperature_c REAL,
                    wind_speed_kmh REAL,
                    humidity_pct INTEGER,
                    precipitation_mm REAL)"""
                )
    cursor.execute("""
                    INSERT INTO weather (timestamp, latitude, longitude, temperature_c, wind_speed_kmh, humidity_pct, precipitation_mm)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """, (
                    record["timestamp"],
                    record["latitude"],
                    record["longitude"],
                    record["temperature_c"],
                    record["wind_speed_kmh"],
                    record["humidity_pct"],
                    record["precipitation_mm"]
                ))
    conn.commit()
    conn.close()    
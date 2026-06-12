import logging
from src.extract import fetch_weather
from src.transform import transform_weather
from src.load import load_weather

logging.basicConfig(
    level = logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s" 
)

def run_pipeline(latitude, longitude):
    logging.info("Pipeline started")
    raw_data = fetch_weather(latitude, longitude)
    logging.info("Weather data fetched successfully")
    transformed_data = transform_weather(raw_data)
    logging.info("Data transformed")
    load_weather(transformed_data)
    logging.info("Record saved to database")
    logging.info("Pipeline complete")

if __name__ == "__main__":
    run_pipeline(47.7, 8.99)
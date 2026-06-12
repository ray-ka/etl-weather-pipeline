# ETL Weather Pipeline

[![CI](https://github.com/ray-ka/etl-weather-pipeline/actions/workflows/ci.yml/badge.svg)](https://github.com/ray-ka/etl-weather-pipeline/actions/workflows/ci.yml)

A lightweight ETL pipeline that fetches current weather data for Karlsruhe from the Open-Meteo API, transforms it into a clean structured format, and stores it in a local SQLite database.

---

## Tech Stack

- **Python 3.12** — pipeline logic
- **Open-Meteo API** — free weather data, no API key required
- **SQLite** — local storage via Python's built-in `sqlite3`
- **Docker** — containerised execution
- **pytest** — unit tests for the transform layer
- **GitHub Actions** — CI pipeline runs tests on every push

---

## Architecture

Extract → Transform → Load
- **Extract** (`src/extract.py`) — fetches current weather data from the Open-Meteo API for a given latitude/longitude and returns the raw JSON response as a Python dictionary
- **Transform** (`src/transform.py`) — strips metadata and flattens the nested API response into a clean seven-field record with human-readable column names
- **Load** (`src/load.py`) — creates the `weather` table if it does not exist and inserts the clean record as a new row in a SQLite database
- **Pipeline** (`src/pipeline.py`) — orchestrates the three steps with structured logging; entry point for both local and containerised execution

---

## Project Structure

etl-weather-pipeline/

├── src/

│   ├── init.py

│   ├── extract.py       # Fetches raw data from Open-Meteo API

│   ├── transform.py     # Cleans and flattens the API response

│   ├── load.py          # Saves records to SQLite

│   └── pipeline.py      # Orchestrates ETL flow with logging

├── tests/

│   └── test_transform.py  # Unit tests for the transform layer

├── .github/

│   └── workflows/

│       └── ci.yml       # GitHub Actions CI workflow

├── Dockerfile

├── .dockerignore

├── requirements.txt

└── README.md

---

## Getting Started

### Run locally

```bash
git clone https://github.com/ray-ka/etl-weather-pipeline.git
cd etl-weather-pipeline

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python3 -m src.pipeline
```

### Run with Docker

```bash
docker build -t etl-weather-pipeline .
docker run --rm etl-weather-pipeline
```

### Run tests

```bash
pytest tests/ -v
```

---

## Production Habits Demonstrated

- **Structured logging** — all pipeline events use Python's `logging` module with timestamps and severity levels instead of `print()` statements
- **Unit testing** — the transform layer is covered by five pytest tests using fixtures and isolated fake data; no real API calls are made during testing
- **Docker** — the pipeline runs in a reproducible container with a minimal `python:3.12-slim` base image and a `.dockerignore` that excludes the virtual environment and generated files
- **CI with GitHub Actions** — every push to `main` triggers an automated workflow that installs dependencies and runs the full test suite on a clean Ubuntu environment
- **Single responsibility** — each module does exactly one thing; extract, transform, and load are fully decoupled and independently testable
- **Schema versioning ready** — the database uses `CREATE TABLE IF NOT EXISTS` making it safe to run repeatedly without data loss
# WeatherPulse 🌦️

An automated weather data engineering and analytics pipeline that collects
current weather data for 10 major Indian cities, stores historical
observations, and visualizes trends through Power BI.

## Architecture

Meteosource API
       ↓
Python Data Collection
       ↓
Pandas Transformation & Validation
       ↓
SQLite Database
       ↓
CSV Export
       ↓
Power BI Dashboard

Windows Task Scheduler runs the pipeline hourly.

## Features

- Collects live weather data for 10 Indian cities
- API authentication using environment variables
- Automated hourly data collection
- Data validation using Pandas
- Historical storage using SQLite
- SQL-based analytics
- CSV export for BI consumption
- Power BI dashboard with:
  - Temperature analysis
  - Weather conditions
  - Wind analysis
  - Precipitation
  - City-level trends

## Tech Stack

- Python
- Requests
- Pandas
- SQLite
- SQL
- Power BI
- Windows Task Scheduler
- python-dotenv

## Cities

- Delhi
- Mumbai
- Bangalore
- Chennai
- Kolkata
- Hyderabad
- Pune
- Jaipur
- Ahmedabad
- Lucknow

## Project Structure

```text
WeatherPulse/
├── sql/
│   └── analytics.sql
├── .gitignore
├── requirements.txt
├── README.md
├── weather_collector.py
├── export_data.py
├── run_pipeline.py
└── database_test.py

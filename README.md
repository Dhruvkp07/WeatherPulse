# WeatherPulse 🌦️

WeatherPulse is an automated weather data pipeline that collects live weather data for major Indian cities, stores historical observations, performs SQL-based analysis, and presents the results through an interactive Power BI dashboard.

The project also includes a machine learning component for temperature prediction.

## Project Overview

WeatherPulse combines three areas:

- Data Engineering
- Data Analytics
- Data Science / Machine Learning

The main workflow is:

Meteosource API
        ↓
Python Data Collection
        ↓
Data Validation
        ↓
SQLite Database
        ↓
SQL Analytics
        ↓
Power BI Dashboard

Historical Weather Data
        ↓
Feature Engineering
        ↓
Random Forest Regression
        ↓
Temperature Prediction


## Architecture

```text
                    Meteosource API
                           |
                           v
                 weather_collector.py
                           |
                           v
                  Pandas DataFrame
                           |
                    Data Validation
                           |
                           v
                     SQLite DB
                           |
              +------------+------------+
              |                         |
              v                         v
        SQL Analytics             ML Pipeline
              |                         |
              |                  Feature Engineering
              |                         |
              |                  Random Forest
              |                         |
              |                  Temperature Prediction
              |                         |
              +------------+------------+
                           |
                           v
                     Power BI
                      Dashboard

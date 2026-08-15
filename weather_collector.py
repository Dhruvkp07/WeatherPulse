import os
import sqlite3
from datetime import datetime, timezone

import pandas as pd
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.environ["METEOSOURCE_API_KEY"]
API_URL = "https://www.meteosource.com/api/v1/free/point"


cities = {
    "Delhi": (28.6139, 77.2090),
    "Mumbai": (19.0760, 72.8777),
    "Bangalore": (12.9716, 77.5946),
    "Chennai": (13.0827, 80.2707),
    "Kolkata": (22.5726, 88.3639),
    "Hyderabad": (17.3850, 78.4867),
    "Pune": (18.5204, 73.8567),
    "Jaipur": (26.9124, 75.7873),
    "Ahmedabad": (23.0225, 72.5714),
    "Lucknow": (26.8467, 80.9462)
}


def get_current_weather(city, lat, lon):
    params = {
        "lat": lat,
        "lon": lon,
        "sections": "current",
        "timezone": "Asia/Kolkata",
        "language": "en",
        "units": "metric"
    }

    headers = {
        "X-API-Key": API_KEY
    }

    response = requests.get(
        API_URL,
        params=params,
        headers=headers,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()
    current = data["current"]

    return {
        "city": city,
        "latitude": data["lat"],
        "longitude": data["lon"],
        "elevation": data["elevation"],
        "timezone": data["timezone"],
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "temperature": current.get("temperature"),
        "weather": current.get("summary"),
        "icon": current.get("icon"),
        "icon_num": current.get("icon_num"),
        "wind_speed": current["wind"].get("speed"),
        "wind_angle": current["wind"].get("angle"),
        "wind_direction": current["wind"].get("dir"),
        "precipitation": current["precipitation"].get("total"),
        "precipitation_type": current["precipitation"].get("type"),
        "cloud_cover": current.get("cloud_cover")
    }


records = []

for city, (lat, lon) in cities.items():
    try:
        weather = get_current_weather(city, lat, lon)
        records.append(weather)

        print(
            f"{city}: {weather['temperature']}°C | "
            f"{weather['weather']}"
        )

    except Exception as e:
        print(f"{city}: {e}")


weather_df = pd.DataFrame(records)

print("\nData quality check")
print("Shape:", weather_df.shape)
print("\nMissing values:")
print(weather_df.isnull().sum())
print("\nDuplicate rows:", weather_df.duplicated().sum())


connection = sqlite3.connect("weatherpulse.db")

weather_df.to_sql(
    "weather_history",
    connection,
    if_exists="append",
    index=False
)

connection.close()

print("\nData saved to weatherpulse.db")
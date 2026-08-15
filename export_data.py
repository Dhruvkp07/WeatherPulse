import sqlite3
import pandas as pd
import os

os.makedirs("data", exist_ok=True)

connection = sqlite3.connect("weatherpulse.db")

query = """
SELECT *
FROM current_weather
"""

df = pd.read_sql(query, connection)

connection.close()

df.to_csv(
    "data/weather_history.csv",
    index=False
)

print(f"✅ Exported {len(df)} records to data/weather_history.csv")
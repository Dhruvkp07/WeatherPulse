import sqlite3
import joblib
import pandas as pd


model = joblib.load("ml/model/weather_model.pkl")
preprocessor = joblib.load("ml/model/preprocessor.pkl")


connection = sqlite3.connect("weatherpulse.db")

query = """
SELECT city, collected_at, temperature, wind_speed,
       precipitation, cloud_cover
FROM weather_history
ORDER BY collected_at
"""

df = pd.read_sql(query, connection)
connection.close()


df["collected_at"] = pd.to_datetime(df["collected_at"])

df["hour"] = df["collected_at"].dt.hour
df["day"] = df["collected_at"].dt.day
df["month"] = df["collected_at"].dt.month

df["temperature_lag_1"] = (
    df.groupby("city")["temperature"].shift(1)
)

df["temperature_lag_2"] = (
    df.groupby("city")["temperature"].shift(2)
)


latest = (
    df.sort_values("collected_at")
      .groupby("city")
      .tail(1)
      .dropna()
      .copy()
)


features = [
    "city",
    "hour",
    "day",
    "month",
    "temperature_lag_1",
    "temperature_lag_2",
    "wind_speed",
    "precipitation",
    "cloud_cover"
]

X = latest[features]

X = preprocessor.transform(X)
predictions = model.predict(X)

latest["predicted_temperature"] = predictions


print("\nTemperature Predictions")
print(
    latest[
        ["city", "temperature", "predicted_temperature"]
    ].to_string(index=False)
)
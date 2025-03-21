import psycopg2
import requests

API_KEY = "93667d671c9b47e8b8bee3a4a4d6fa12"
CITY = 'Delhi'
START_DATE, END_DATE = "2025-02-15", "2025-03-17"
URL = f"https://api.weatherbit.io/v2.0/history/airquality?&key={API_KEY}&start_date={START_DATE}&end_date={END_DATE}&city={CITY}&country=IN"

conn = psycopg2.connect("dbname=air_quality user=postgres password=qwerty123 host=localhost")
cur = conn.cursor()

response = requests.get(URL)
data = response.json()

for entry in reversed(data["data"]):
    cur.execute("""
        INSERT INTO air_quality_data (city, aqi, co, no2, o3, pm10, pm25, so2, timestamp_local)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        data["city_name"], entry["aqi"], entry["co"], 
        entry["no2"], entry["o3"], entry["pm10"], entry["pm25"], entry["so2"], entry["timestamp_local"]
    ))

conn.commit()
cur.close()
conn.close()

from confluent_kafka import Producer
import requests
import json
import time

API_URL = "https://api.waqi.info/feed/geo:28.65195;77.23149/?token=a459575bbe607a23234ffc0dd466211da04bfe6e"

producer_conf = {
    'bootstrap.servers': 'localhost:9092'
}
producer = Producer(producer_conf)

def delivery_report(err, msg):
    if err:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Sent data: {msg.value().decode('utf-8')}")

while True:
    response = requests.get(API_URL).json()
    if "data" in response:
        data = response["data"]
        pollutants = data.get("iaqi", {})
        
        aqi_data = {
            "aqi": data["aqi"],
            "co": pollutants.get("co", {}).get("v", None),
            "no2": pollutants.get("no2", {}).get("v", None),
            "o3": pollutants.get("o3", {}).get("v", None),
            "pm10": pollutants.get("pm10", {}).get("v", None),
            "pm25": pollutants.get("pm25", {}).get("v", None),
            "so2": pollutants.get("so2", {}).get("v", None),
            "timestamp": data["time"]["iso"]
        }

        producer.produce("air_quality_data", value=json.dumps(aqi_data).encode('utf-8'), callback=delivery_report)
        producer.flush()

    time.sleep(10)

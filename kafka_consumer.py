import psycopg2
import json
from confluent_kafka import Consumer

conn = psycopg2.connect("dbname=air_quality user=postgres password=qwerty123 host=localhost")
cursor = conn.cursor()

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'air_quality_group',    
    'auto.offset.reset': 'latest'
})
consumer.subscribe(['air_quality_data'])

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print(f"Consumer error: {msg.error()}")
        continue

    data = json.loads(msg.value().decode('utf-8'))
    print("Received data:", data)
    try:
        cursor.execute("""
            INSERT INTO air_quality_data (city, aqi, co, no2, o3, pm10, pm25, so2, timestamp_local)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, ("Delhi", data.get('aqi'),  
            data.get('co'), data.get('no2'), data.get('o3'),  
            data.get('pm10'), data.get('pm25'), data.get('so2'), data.get('timestamp')))

        conn.commit()
    except psycopg2.errors.UniqueViolation:
        print("Duplicate Time Found Skipping !!")
        conn.rollback() 

consumer.close()
conn.close()

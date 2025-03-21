# Real-Time AQI Monitoring Dashboard

This project is a **Real-Time Air Quality Monitoring System** that collects AQI data, processes it using Kafka and PostgreSQL, and visualizes it in **Power BI**.

# Dashboard Screenshot: 
![image](https://github.com/user-attachments/assets/25d745b4-b738-479d-9442-b4df4823349e)


## 📌 Features

- **Live AQI Data Collection** (Delhi)
- **Kafka Streaming** for real-time data processing
- **PostgreSQL Database** for structured storage
- **Power BI Dashboard** for interactive analysis

## 🏗️ System Architecture

1. **Data Ingestion:**  
    - A Python script fetches AQI data from an API every 10 seconds.
    - Data is sent to a Kafka topic (`air_quality_data`).

2. **Data Processing & Storage:**  
    - A Kafka consumer retrieves messages.
    - The data is stored in **PostgreSQL** with timestamps.

3. **Visualization:**  
    - **Power BI** pulls data from PostgreSQL for analysis.
    - Displays **AQI trends, pollutant levels, and historical data**.

## 🛠️ Tech Stack

- **Kafka** (Streaming Platform)
- **PostgreSQL** (Database)
- **Python** (Data Ingestion & Processing)
- **Power BI** (Visualization)

## 📊 Power BI Dashboard

- **Current AQI & Pollutants**: Displays live data.
- **Time-Series Graph**: AQI trends over time.
- **Data Table**: Historical pollutant levels.
- **AQI Color Guide**: Categorizes air quality levels.

## 🔄 Kafka Data Flow

```
API → Kafka Producer → Kafka Topic → Kafka Consumer → PostgreSQL → Power BI
```

This setup ensures **real-time data flow** and efficient storage for historical analysis.

---


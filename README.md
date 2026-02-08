✈️ Real-Time Flight Monitoring System

Kafka · Flink · Kafka Connect · Elasticsearch
This project demonstrates an end-to-end real-time streaming architecture using Apache Kafka, Apache Flink, Kafka Connect, and Elasticsearch.

🏗️ System Architecture
The application consists of six core components, each with a single responsibility.

Producer
   ↓
Kafka (Flights Topic)
   ↓
Apache Flink (Real-Time Processing)
   ↓
Kafka (Alerts Topic)
   ↓
Kafka Connect
   ↓
Elasticsearch
   ↓
Backend Service
   ↓
Frontend


🚀 How to Run (High Level)
Detailed step-by-step commands available in Youtube videos. @realtimestack

Start Kafka & Zookeeper
Create Kafka topics (flights, alerts)
Run the Producer
Start Flink job
Configure Kafka Connect Elasticsearch Sink
Start Backend service
Open Frontend

✈️ Real-Time Flight Monitoring System

Kafka · Flink · Kafka Connect · ElasticsearchThis project demonstrates an end-to-end real-time streaming architecture using Apache Kafka, Apache Flink, Kafka Connect, and Elasticsearch.

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

1. Start Kafka & Zookeeper
2. Create Kafka topics (flights, alerts)
3. Run the Producer
4. Start Flink job
5. Configure Kafka Connect Elasticsearch Sink
6. Start Backend service
7. Open Frontend

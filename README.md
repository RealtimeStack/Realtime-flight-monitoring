✈️ Real-Time Flight Monitoring System

Kafka · Flink · Kafka Connect · Elasticsearch
This project demonstrates an end-to-end real-time streaming architecture using Apache Kafka, Apache Flink, Kafka Connect, and Elasticsearch.

🏗️ System Architecture
The application consists of six core components, each with a single responsibility.

flowchart LR
    P[Producer<br/>Flight Events]
    K1[Kafka<br/>Flights Topic]
    F[Apache Flink<br/>Real-Time Processing]
    K2[Kafka<br/>Alerts Topic]
    KC[Kafka Connect<br/>Elasticsearch Sink]
    ES[Elasticsearch<br/>Alerts Index]
    B[Backend Service<br/>REST API]
    FE[Frontend<br/>Dashboard]

    P --> K1
    K1 --> F
    F --> K2
    K2 --> KC
    KC --> ES
    ES --> B
    B --> FE


🚀 How to Run (High Level)
Detailed step-by-step commands available in Youtube videos. @realtimestack

Start Kafka & Zookeeper
Create Kafka topics (flights, alerts)
Run the Producer
Start Flink job
Configure Kafka Connect Elasticsearch Sink
Start Backend service
Open Frontend

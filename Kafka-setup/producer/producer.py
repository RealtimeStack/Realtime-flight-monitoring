import json
import random
import time
from datetime import datetime, timezone
from kafka import KafkaProducer

# Connect to Kafka broker
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',  # Docker network name
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Sample flights
flights = [
    {"flight_id": "AI302", "lat": 12.95, "lon": 77.59},     # India
    {"flight_id": "AI401", "lat": 28.56, "lon": 77.10},
    {"flight_id": "AI509", "lat": 19.09, "lon": 72.87},
    {"flight_id": "AI618", "lat": 22.65, "lon": 88.45},
    {"flight_id": "AI777", "lat": 13.08, "lon": 80.27},

    {"flight_id": "BA145", "lat": 51.47, "lon": -0.45},    # UK
    {"flight_id": "BA256", "lat": 52.45, "lon": -1.73},
    {"flight_id": "BA389", "lat": 53.35, "lon": -2.27},

    {"flight_id": "EK202", "lat": 25.25, "lon": 55.36},    # UAE
    {"flight_id": "EK311", "lat": 24.47, "lon": 54.37},
    {"flight_id": "EK450", "lat": 26.20, "lon": 56.24},

    {"flight_id": "QR718", "lat": 25.27, "lon": 51.61},    # Qatar
    {"flight_id": "QR902", "lat": 26.03, "lon": 50.55},

    {"flight_id": "UA404", "lat": 39.85, "lon": -104.67}, # USA
    {"flight_id": "UA512", "lat": 33.94, "lon": -118.40},
    {"flight_id": "AA233", "lat": 40.64, "lon": -73.78},
    {"flight_id": "DL789", "lat": 41.97, "lon": -87.90},

    {"flight_id": "LH760", "lat": 50.03, "lon": 8.57},    # Germany
    {"flight_id": "LH890", "lat": 48.35, "lon": 11.79},

    {"flight_id": "AF102", "lat": 49.00, "lon": 2.55},    # France
    {"flight_id": "AF220", "lat": 43.65, "lon": 7.21},

    {"flight_id": "SQ318", "lat": 1.36, "lon": 103.99},   # Singapore
    {"flight_id": "SQ501", "lat": 1.22, "lon": 104.01},

    {"flight_id": "QF12",  "lat": -33.94, "lon": 151.18}  # Australia
]

while True:
    for f in flights:
        # Simulate random movement
        f['lat'] += random.uniform(-0.05, 0.05)
        f['lon'] += random.uniform(-0.05, 0.05)
        altitude = random.randint(4000, 40000)
        speed = random.randint(500, 900)
        event = {
            "flight_id": f["flight_id"],
            "lat": f["lat"],
            "lon": f["lon"],
            "altitude_ft": altitude,
            "speed_kmh": speed,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
        producer.send('flights', event)
        print(f"Sent: {event}")

    producer.flush()  # Ensure all messages are sent

    # After sending all flights, check if at least one has altitude 5000-10000
    # In production, you might want to track this differently
    # For simulation purposes, we can just ensure the next iteration
    # has at least one flight in that range by adjusting the logic
#    time.sleep(1)

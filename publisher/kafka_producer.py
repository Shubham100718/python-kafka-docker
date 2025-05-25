import json
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)


def send_to_kafka(topic: str, message: dict):
    producer.send(topic, value=message)
    producer.flush()

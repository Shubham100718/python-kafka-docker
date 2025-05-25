import time
import json
import mysql.connector
from kafka import KafkaConsumer


def store_message(msg: dict):
    conn = mysql.connector.connect(
        host='mysql', user='user', password='password', database='kafkadb'
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (msg_key, msg_value) VALUES (%s, %s)", (msg.get('key'), msg.get('value')))
    conn.commit()
    cursor.close()
    conn.close()


def start_consumer():
    time.sleep(10)
    consumer = KafkaConsumer(
        'test-topic',
        bootstrap_servers='kafka:9092',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='fastapi-group',
        value_deserializer=lambda v: json.loads(v.decode('utf-8'))
    )
    print("🚀 Kafka consumer started.")
    for message in consumer:
        print(f"📥 Received message: {message.value}")
        store_message(message.value)


if __name__ == "__main__":
    start_consumer()

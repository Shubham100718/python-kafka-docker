from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from kafka_producer import send_to_kafka

app = FastAPI()


class Message(BaseModel):
    key: str
    value: str


@app.post("/send")
def send_message(msg: Message):
    try:
        send_to_kafka("test-topic", msg.dict())
        return {"status": "Message sent", "data": msg}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Kafka error: {str(e)}")

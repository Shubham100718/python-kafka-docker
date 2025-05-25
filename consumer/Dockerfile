FROM python:3.11-slim

WORKDIR /consumer

COPY requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "kafka_consumer.py"]

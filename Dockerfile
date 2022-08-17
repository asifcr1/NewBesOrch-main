FROM python:3.9-slim
WORKDIR /BESOrchestrator
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY main.py .
COPY webhooks.py .
COPY config config/
COPY data data/
CMD ["python", "main.py"]
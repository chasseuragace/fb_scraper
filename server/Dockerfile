# server/Dockerfile

FROM python:3.8-slim

WORKDIR /app

# Install build tools
RUN apt-get update && \
    apt-get install -y build-essential

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]

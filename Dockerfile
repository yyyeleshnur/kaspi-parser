FROM python:3.12-slim

WORKDIR /app

# Устанавливаем системные зависимости для psycopg2, lxml, selenium и т.д.
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    libxml2-dev \
    libxslt1-dev \
    libffi-dev \
    libssl-dev \
    python3-dev \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

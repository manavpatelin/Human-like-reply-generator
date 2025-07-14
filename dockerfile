# Use Python 3.11 base image with updated OpenSSL
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies including OpenSSL for TLS support
RUN apt-get update \
    && apt-get install -y build-essential libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project code
COPY . .

# Expose the default Flask port
EXPOSE 5000

# Start the app using Gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000", "--timeout", "120"]

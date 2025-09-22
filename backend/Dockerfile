cat > backend/Dockerfile <<'EOF'
FROM python:3.10-slim

WORKDIR /app

# system deps (small)
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 8000
# Use gunicorn for production-like server (1 worker is fine for demo)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app", "--workers=1"]
EOF

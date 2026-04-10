FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml setup.cfg setup.py ./
COPY src/ src/

RUN pip install --no-cache-dir -e .

COPY . .

EXPOSE 2200

CMD ["python", "flask_app.py"]

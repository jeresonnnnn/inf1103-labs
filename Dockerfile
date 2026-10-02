FROM python:3.11-slim

WORKDIR /app

COPY auditor.py .

CMD ["python", "auditor.py"]

FROM python:3.11-slim

WORKDIR /app

COPY modular_auditor.py .

CMD ["python", "modular_auditor.py"]

FROM python:3.11-slim

WORKDIR /app

COPY persistent_auditor.py .

CMD ["python", "persistent_auditor.py"]
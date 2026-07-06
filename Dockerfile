# --- Base Image ---
FROM python:3.11-slim

# --- Munkakonyvtar ---
WORKDIR /app

# --- Fuggosegek telepitese ---
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- Forraskod masolasa ---
COPY src/ ./src/

# --- Inditas ---
CMD ["python", "src/main.py"]

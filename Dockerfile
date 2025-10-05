# Base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /aap

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI (folder = aap, file = main.py, object = app)
CMD ["uvicorn", "aap.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Use official Python image
FROM python:3.11-slim

# Install system dependencies for OpenCV
RUN apt-get update && \
    apt-get install -y libgl1 libglib2.0-0 wget git && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expose port 8080 for Railway
EXPOSE 8080

# Run the app with 2 Gunicorn workers
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8080", "--workers", "2"]

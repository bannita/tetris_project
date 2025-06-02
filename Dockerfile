# Dockerfile
FROM python:3.10

# Set work directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy rest of the app
COPY . .

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run Flask
CMD ["flask", "run"]
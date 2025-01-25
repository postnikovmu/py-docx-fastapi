# Dockerfile
# Use the official Python image from the Docker Hub
FROM python:3.10.6-slim

# Set the working directory in the container
WORKDIR /app

# Set environment variables to prevent Python from writing .pyc files and to ensure unbuffered output
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy requirements.txt into the container at /app
COPY requirements.txt .

# Install dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
